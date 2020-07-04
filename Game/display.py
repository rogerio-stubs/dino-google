import os
import pygame as pg

import Server.dinosaur as dino
import Server.cactus as cac
import Server.bird as bd
import Server.background as bg

DIC_PATH = os.path.abspath(os.path.dirname(__file__))

CACTUS_DIMENSIONS = [[446, 0, 34, 72], [480, 0, 68, 72], [548, 0, 102, 72],
                     [652, 0, 50, 102], [702, 0, 102, 102], [802, 0, 150, 102]]

DINOSAUR_DIMENSIONS = [[1338, 0, 88, 96], [1514, 0, 88, 96], [1602, 0, 88, 96],
                       [1866, 36, 118, 60], [1984, 36, 120, 60]]

BIRD_DIMENSIONS = [[260, 0, 93, 84], [352, 0, 92, 84]]

FLOOR_DIMENSIONS = [[2, 104, 2400, 26]]

def load_image(image_name):
    image_general = pg.image.load(DIC_PATH + image_name)
    image_dino = [image_general.subsurface(dimension) for dimension in DINOSAUR_DIMENSIONS]
    images_cactus = [image_general.subsurface(dimension) for dimension in CACTUS_DIMENSIONS]
    image_bird = [image_general.subsurface(dimension) for dimension in BIRD_DIMENSIONS]
    image_floor = [image_general.subsurface(dimension) for dimension in FLOOR_DIMENSIONS]
    return image_dino, images_cactus, image_bird, image_floor

def render(display, target_dino, target_cactus, target_bird, target_start_floor, target_final_floor):
    display.fill((255, 255, 255))
    display.blit(target_start_floor.current_image, [target_start_floor.position_x, target_start_floor.position_y])
    display.blit(target_final_floor.current_image, [target_final_floor.position_x, target_final_floor.position_y])
    display.blit(target_dino.current_image, [target_dino.position_x, target_dino.position_y])
    display.blit(target_cactus.current_image, [target_cactus.position_x, target_cactus.position_y])
    display.blit(target_bird.current_image, [target_bird.position_x, target_bird.position_y])
    pg.display.update()

def screen():
    pg.init()

    display = pg.display.set_mode((800, 800)) # largura / altura
    pg.display.set_caption("T-Rex Running")

    image_dino, images_cactus, image_bird, image_floor = load_image("/assets/image_general.png")
    t_rex = dino.Dinosaur(200, 350, image_dino)
    cactus = cac.Cactus(750, 370, images_cactus)
    bird = bd.Bird(750, 320, image_bird)
    start_floor = bg.Background(0, 420, image_floor)    
    final_floor = bg.Background(2400, 420, image_floor)

    close = False
    is_jump = False
    is_down = False
    jump_count = 10
    count_frame_bird = 0
    count_frame_dino = 0

    while close is not True:
        pg.time.delay(30)

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
            count_frame_dino += 1
            is_down = False
        else:
            if count_frame_dino > 3:
                t_rex.walk()
                count_frame_dino = 0
            count_frame_dino += 1

            if count_frame_bird > 15:
                bird.fly()
                count_frame_bird = 0
            count_frame_bird += 1

        cactus.change_position()

        bird.change_position()
        start_floor.move()
        final_floor.move()
        render(display, t_rex, cactus, bird, start_floor, final_floor)
    pg.quit()


screen()
