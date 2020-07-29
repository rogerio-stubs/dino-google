import os
import pygame as pg

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 30)

DIC_PATH = os.path.abspath(os.path.dirname(__file__))

CACTUS_DIMENSIONS = [[446, 0, 34, 72], [480, 0, 68, 72], [548, 0, 102, 72],
                     [652, 0, 50, 102], [702, 0, 102, 102], [802, 0, 150, 102]]

DINOSAUR_DIMENSIONS = [[1338, 0, 88, 96], [1514, 0, 88, 96], [1602, 0, 88, 96],
                       [1866, 36, 118, 60], [1984, 36, 120, 60]]

BIRD_DIMENSIONS = [[260, 0, 93, 84], [352, 0, 92, 84]]

FLOOR_DIMENSIONS = [[2, 104, 2400, 26]]

def dimensions_game(delta_x, delta_y):
    # Melhorar nomes
    sides = (delta_x * 20) / 100
    bottom = (delta_y * 50) / 100
    width = delta_x - (2 * sides)
    height = delta_y - bottom
    edge_start = sides
    edge_end = width + sides
    middle = (width / 2) + edge_start - 150
    return [sides, 10, width, height], edge_start, edge_end, middle

def position_game(space_game):
    # Gera a posição dinamica
    # dos objetos
    # lembrar que os mesmo são desenhados de cima para baixo
    pass

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
    # display.blit(obj_bird.current_image, [obj_bird.position_x, obj_bird.position_y])
    pg.draw.rect(display, (0, 0, 0), space_game, 1)
    # Melhorar essas duas linhas
    pg.draw.rect(display, (255, 255, 255), [0, 10, space_game[0], space_game[3]])
    pg.draw.rect(display, (255, 255, 255), [space_game[2]+space_game[0], 10, space_game[2], space_game[3]])
    pg.display.update()
        