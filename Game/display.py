import os
import pygame as pg

import Server.dinosaur as dino
import Server.cactus as cac
import Server.bird as bd

DIC_PATH = os.path.abspath(os.path.dirname(__file__))

CACTUS_DIMENSIONS = [[443, 0, 37, 72], [480, 0, 68, 72], [548, 0, 102, 72],
                     [651, 0, 51, 102], [702, 0, 102, 102], [803, 0, 150, 102]]

DINOSAUR_DIMENSIONS = [[1338, 0, 88, 96], [1514, 0, 88, 96], [1602, 0, 88, 96],
                       [1866, 0, 118, 96], [1984, 0, 120, 96]]

BIRD_DIMENSIONS = [[259, 0, 93, 84], [352, 0, 92, 84]]


def load_image(image_name):
    image_general = pg.image.load(DIC_PATH + image_name)
    images_dino = [image_general.subsurface(dimension) for dimension in DINOSAUR_DIMENSIONS]
    images_cactus = [image_general.subsurface(dimension) for dimension in CACTUS_DIMENSIONS]
    images_bird = [image_general.subsurface(dimension) for dimension in BIRD_DIMENSIONS]
    return images_dino, images_cactus, images_bird

def render(display, target_dino, target_cactus, target_bird):
    display.fill((255, 255, 255))
    display.blit(target_dino.current_image, [target_dino.position_x, target_dino.position_y])
    display.blit(target_cactus.current_image, [target_cactus.position_x, target_cactus.position_y])
    display.blit(target_bird.current_image, [target_bird.position_x, target_bird.position_y])
    pg.display.update()

def screen():
    pg.init()

    display = pg.display.set_mode((800, 800)) # largura / altura
    pg.display.set_caption("T-Rex Running")

    images_dino, images_cactus, images_bird = load_image("/assets/image_general.png")
    t_rex = dino.Dinosaur(200, 350, images_dino)
    cactus = cac.Cactus(750, 370, images_cactus)
    bird = bd.Bird(750, 320, images_bird)

    close = False
    is_jump = False
    is_down = False
    jump_count = 10
    count_frame_bird = 0
    count_frame_dino = 0

    # máximo dois elementos em tela
    # cactus + bird
    # cactu + cactu
    #  Alterar funcionamento do frame

    while close is not True:
        pg.time.delay(30)
        render(display, t_rex, cactus, bird)

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

    pg.quit()


screen()
