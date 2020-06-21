import pygame as pg
import os

import Server.dinosaur as dino
import Server.cactus as cac

DIC_PATH = os.path.abspath(os.path.dirname(__file__))

def loadImage(imageName):
    image = pg.image.load(DIC_PATH + imageName)
    imageSize = image.get_rect()
    return image, imageSize

def render(display, targetDino, targetCactus):
    display.fill((255, 255, 255))
    display.blit(targetDino.image, [targetDino.positionX, targetDino.positionY])
    # if targetCactus.show == True:
    display.blit(targetCactus.image, [targetCactus.positionX, targetCactus.positionY])
    pg.display.update()

def screen():
    pg.init()

    display = pg.display.set_mode((800, 800)) # largura / altura
    pg.display.set_caption("T-Rex Running")

    imageDino, dimensionsDino = loadImage("/assets/dino.png")
    imageDino = pg.transform.scale(imageDino, [64, 64])
    TRex = dino.Dinosaur(200, 350, imageDino)

    imageCactus, dimensionsCactus = loadImage("/assets/cactus.jpg")
    imageCactus = pg.transform.scale(imageCactus, [32, 32])
    cactus = cac.Cactus(750, 370, imageCactus)

    close = False
    isJump = False
    JumpCount = 10


    while close != True:
        pg.time.delay(20)
        render(display, TRex, cactus)

        for event in pg.event.get():        
            if event.type == pg.QUIT:
                close = True

        keys = pg.key.get_pressed()

        if keys[pg.K_UP]:
            # Pular
            isJump = True

        if keys[pg.K_DOWN]:
            # Abaixar
            # Substituir imagem pela do dino abaixado
            print('Abaixar')

        
        if isJump:
            if JumpCount >= -10:
                TRex.jump(JumpCount)
                JumpCount -= 1
            else:
                JumpCount = 10
                isJump = False

        print(cactus.show)
        if cactus.show:
            cactus.changePosition()
        else:
            cactus.randomCactus()

    pg.quit()


screen()
