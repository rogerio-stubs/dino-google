import pygame as pg

import loading as ld
import Server.dinosaur as dino
import Server.cactus as cac
import Server.bird as bd
import Server.background as bg


def screen():
    pg.init()
    delta_x, delta_y = (pg.display.Info().current_w, pg.display.Info().current_h)
    display = pg.display.set_mode([pg.display.Info().current_w, pg.display.Info().current_h])
    pg.display.set_caption("T-Rex Running")

    space_game, edge_start, edge_end, middle = ld.dimensions_game(delta_x, delta_y)
    # position_x, position_y = position_game(space_game)

    image_dino, images_cactus, image_bird, image_floor = ld.load_image("/assets/image_general.png")
    t_rex = dino.Dinosaur(edge_start+300, 350, image_dino)

    first_cactus = cac.Cactus(edge_end, 370, images_cactus)
    second_cactus = cac.Cactus(edge_start, 370, images_cactus)

    bird = bd.Bird(edge_end, 320, image_bird)

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

        # Como otimizar esse bloco
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

        if first_cactus.position_x < middle and obstacle_cactus is False:
            second_cactus.choose_image(edge_end, start_floor)
            obstacle_cactus = True

        if second_cactus.position_x < middle and obstacle_cactus is True:
            first_cactus.choose_image(edge_end, start_floor)
            obstacle_cactus = False

        if t_rex.collided(first_cactus):
            first_cactus.change_position()
            second_cactus.change_position()
            bird.change_position()
            start_floor.move()
            final_floor.move()

        pg.display.update()
        ld.render(display, t_rex, first_cactus, second_cactus, bird, start_floor, final_floor, space_game)
    pg.quit()

screen()
