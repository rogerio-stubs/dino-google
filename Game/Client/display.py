import pygame as pg

def screen():        
    pg.init()
    tela = pg.display.set_mode((1600,800)) # largura / altura
    pg.display.set_caption("T-Rex Running")    
    color = (255,255,255) # cor branca
    close = False

    while close != True:
        for event in pg.event.get():
            print('event', event)
            if event.type == pg.QUIT:
                close = True               

            tela.fill(color) # preenche a tela com a cor branca    

            pg.display.update() 

    pg.quit()


screen()
