import os
import pygame as pg

import Server.dinosaur as dino
import Server.cactus as cac
import Server.bird as bd
import Server.background as bg

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 30)

DIC_PATH = os.path.abspath(os.path.dirname(__file__))

SQUARE_X, SQUARE_Y = 800, 800

RIGHT_SCREEN = SQUARE_X + 5

LEFT_SCREEN = SQUARE_X * -1

CACTUS_DIMENSIONS = [[446, 0, 34, 72], [480, 0, 68, 72], [548, 0, 102, 72],
                     [652, 0, 50, 102], [702, 0, 102, 102], [802, 0, 150, 102]]

DINOSAUR_DIMENSIONS = [[1338, 0, 88, 96], [1514, 0, 88, 96], [1602, 0, 88, 96],
                       [1866, 36, 118, 60], [1984, 36, 120, 60]]

BIRD_DIMENSIONS = [[260, 0, 93, 84], [352, 0, 92, 84]]

FLOOR_DIMENSIONS = [[2, 104, 2400, 26]]

def dimensions_game(delta_x, delta_y):
    # Melhorar nomes
    sides = (delta_x * 20) / 100
    bottom = (delta_y * 40) / 100
    width = delta_x - (2 * sides)
    height = delta_y - bottom
    edge_start = sides
    edge_end = width + sides
    return [sides, 10, width, height], edge_start, edge_end

def load_image(image_name):
    image_general = pg.image.load(DIC_PATH + image_name)
    image_dino = [image_general.subsurface(dimension) for dimension in DINOSAUR_DIMENSIONS]
    images_cactus = [image_general.subsurface(dimension) for dimension in CACTUS_DIMENSIONS]
    image_bird = [image_general.subsurface(dimension) for dimension in BIRD_DIMENSIONS]
    image_floor = [image_general.subsurface(dimension) for dimension in FLOOR_DIMENSIONS]
    return image_dino, images_cactus, image_bird, image_floor

def render(display, obj_dino, obj_f_cactus, obj_s_cactus, obj_bird, obj_s_floor, obj_f_floor, space_game):
    display.fill((255, 255, 255))
    display.blit(obj_s_floor.current_image, [obj_s_floor.position_x, obj_s_floor.position_y])
    display.blit(obj_f_floor.current_image, [obj_f_floor.position_x, obj_f_floor.position_y])
    display.blit(obj_dino.current_image, [obj_dino.position_x, obj_dino.position_y])
    display.blit(obj_f_cactus.current_image, [obj_f_cactus.position_x, obj_f_cactus.position_y])
    display.blit(obj_s_cactus.current_image, [obj_s_cactus.position_x, obj_s_cactus.position_y])
    display.blit(obj_bird.current_image, [obj_bird.position_x, obj_bird.position_y])
    pg.draw.rect(display, (0, 0, 0), space_game, 1)
    pg.display.update()

def screen():
    pg.init()
    delta_x, delta_y = (pg.display.Info().current_w, pg.display.Info().current_h)
    display = pg.display.set_mode([pg.display.Info().current_w, pg.display.Info().current_h])
    pg.display.set_caption("T-Rex Running")

    space_game, edge_start, edge_end = dimensions_game(delta_x, delta_y)

    image_dino, images_cactus, image_bird, image_floor = load_image("/assets/image_general.png")
    t_rex = dino.Dinosaur(edge_start+300, 350, image_dino)

    first_cactus = cac.Cactus(edge_end, 370, images_cactus)
    second_cactus = cac.Cactus(LEFT_SCREEN, 370, images_cactus)

    bird = bd.Bird(RIGHT_SCREEN, 320, image_bird)

    start_floor = bg.Background(0, 420, image_floor)
    final_floor = bg.Background(2400, 420, image_floor)

    close = False
    is_jump = False
    is_down = False
    obstacle_cactus = False
    jump_count = 10
    count_frame_bird = 0
    count_frame_dino = 0
    speed = 4
    game_time = 0

    while close is not True:
        pg.time.delay(5)

        start_floor.speed_up(speed)
        final_floor.speed_up(speed)
        bird.speed_up(speed)
        first_cactus.speed_up(speed)
        second_cactus.speed_up(speed)

        game_time += speed

        # print('game time ', game_time)
        # if game_time > 4000:
        #     game_time = 0
        #     print('velocidade', speed)
        #     speed += 5

        for event in pg.event.get():
            if event.type == pg.QUIT:
                close = True

        keys = pg.key.get_pressed()

        if keys[pg.K_UP]:
            is_jump = True

        if keys[pg.K_DOWN]:
            is_down = True

        if is_jump:
            if jump_count >= -10:
                t_rex.jump(jump_count)
                jump_count -= 1
            else:
                jump_count = 10
                is_jump = False
        elif is_down:
            if count_frame_dino > 3:
                t_rex.down()
                count_frame_dino = 0
            t_rex.coordinates(start_floor)
            count_frame_dino += 1
            is_down = False
        else:
            if count_frame_dino > 3:
                t_rex.walk()
                count_frame_dino = 0
            count_frame_dino += 1
            t_rex.coordinates(start_floor)

            if count_frame_bird > 15:
                bird.fly()
                count_frame_bird = 0
            count_frame_bird += 1

        if first_cactus.position_x < edge_start and obstacle_cactus is False:
            second_cactus.choose_image(edge_end, start_floor)
            obstacle_cactus = True

        if second_cactus.position_x < edge_start and obstacle_cactus is True:
            first_cactus.choose_image(edge_end, start_floor)
            obstacle_cactus = False

        first_cactus.change_position()
        second_cactus.change_position()
        bird.change_position()
        start_floor.move()
        final_floor.move()

        render(display, t_rex, first_cactus, second_cactus, bird, start_floor, final_floor, space_game)
    pg.quit()


screen()
