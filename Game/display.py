import os
import pygame as pg

import Server.dinosaur as dino
import Server.cactus as cac

DIC_PATH = os.path.abspath(os.path.dirname(__file__))


def load_image(image_name):
    image = pg.image.load(DIC_PATH + image_name)
    image_size = image.get_rect()
    return image, image_size

def render(display, targer_dino, target_cactus):
    display.fill((255, 255, 255))
    display.blit(targer_dino.image, [targer_dino.position_x, targer_dino.position_y])
    # if target_cactus.show == True:
    display.blit(target_cactus.image, [target_cactus.position_x, target_cactus.position_y])
    pg.display.update()

def screen():
    pg.init()

    display = pg.display.set_mode((800, 800)) # largura / altura
    pg.display.set_caption("T-Rex Running")

    image_dino, dimensions_dino = load_image("/assets/dino.png")
    image_dino = pg.transform.scale(image_dino, [64, 64])
    t_rex = dino.Dinosaur(200, 350, image_dino)

    image_cactus, dimensions_cactus = load_image("/assets/cactus.jpg")
    image_cactus = pg.transform.scale(image_cactus, [32, 32])
    cactus = cac.Cactus(750, 370, 5, image_cactus)

    close = False
    is_jump = False
    jump_count = 10


    while close is not True:
        pg.time.delay(20)
        render(display, t_rex, cactus)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                close = True

        keys = pg.key.get_pressed()

        if keys[pg.K_UP]:
            # Pular
            is_jump = True

        if keys[pg.K_DOWN]:
            # Abaixar
            # Substituir imagem pela do dino abaixado
            print('Abaixar')
        if is_jump:
            if jump_count >= -10:
                t_rex.jump(jump_count)
                jump_count -= 1
            else:
                jump_count = 10
                is_jump = False

        cactus.change_position()

    pg.quit()


screen()
