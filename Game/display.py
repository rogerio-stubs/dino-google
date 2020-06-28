import os
import pygame as pg

import Server.dinosaur as dino
import Server.cactus as cac

DIC_PATH = os.path.abspath(os.path.dirname(__file__))

CACTUS_DIMENSIONS = [[443, 0, 37, 72], [480, 0, 34, 72], [514, 0, 34, 72], [548, 0, 34, 72],
                     [582, 0, 34, 72], [616, 0, 35, 72], [651, 0, 51, 102], [702, 0, 49, 102],
                     [751, 0, 52, 102], [803, 0, 47, 102], [850, 0, 102, 102]]

DINOSAUR_DIMENSIONS = [[1338, 0, 88, 96], [1514, 0, 88, 96], [1602, 0, 88, 96],
                       [1866, 0, 118, 96], [1984, 0, 120, 96]]

BIRD_DIMENSIONS = [[259, 0, 93, 84], [352, 0, 92, 84]]


def load_image(image_name):
    image_general = pg.image.load(DIC_PATH + image_name)
    images_dino = [image_general.subsurface(dimension) for dimension in DINOSAUR_DIMENSIONS]
    images_cactus = [image_general.subsurface(dimension) for dimension in CACTUS_DIMENSIONS]
    images_bird = [image_general.subsurface(dimension) for dimension in BIRD_DIMENSIONS]
    return images_dino, images_cactus, images_bird

def render(display, target_dino):
    display.fill((255, 255, 255))
    display.blit(target_dino.current_image, [target_dino.position_x, target_dino.position_y])
    # display.blit(target_cactus.image, [target_cactus.position_x, target_cactus.position_y])
    pg.display.update()

def screen():
    pg.init()

    display = pg.display.set_mode((800, 800)) # largura / altura
    pg.display.set_caption("T-Rex Running")

    images_dino, images_cactus, images_bird = load_image("/assets/image_general.png")
    t_rex = dino.Dinosaur(200, 350, images_dino)
    cactus = cac.Cactus(750, 370, 5, images_cactus)
    

    close = False
    is_jump = False
    is_down = False
    jump_count = 10


    while close is not True:
        pg.time.delay(20)
        render(display, t_rex)

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
            t_rex.down()
            is_down = False
            print('baixo')
        else:
            t_rex.walk()

    pg.quit()


screen()
