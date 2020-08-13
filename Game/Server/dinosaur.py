import pygame as pg

class Dinosaur(object):
    def __init__(self, position_x, position_y, images):
        self.floor = position_x
        self.position_x = position_x
        self.position_y = position_y
        self.images = images
        self.index = True
        self.current_image = self.images[0] 
        self.image_jump = [self.images[0]]
        self.image_walk = [self.images[1], self.images[2]]
        self.image_down = [self.images[3], self.images[4]]

    def coordinates(self, floor):
        dimensions_dino = self.current_image.get_rect()
        dimensions_floor = floor.current_image.get_rect()
        self.position_y = floor.position_y + dimensions_floor[3] - dimensions_dino[3]

    def jump(self, jump_count):
        self.position_y -= (jump_count * abs(jump_count)) * 0.2
        self.current_image = self.image_jump[0]

    def down(self):
        self.current_image = self.image_down[self.index]
        if self.index:
            self.index = False
        else:
            self.index = True

    def walk(self):
        self.current_image = self.image_walk[self.index]

        if self.index:
            self.index = False
        else:
            self.index = True

    def collided(self, objs):
        list_objs = list()
        for obj in objs:
            list_objs.append([obj.position_x, obj.position_y, obj.dimensions[2]-10, obj.dimensions[3]])
        
        coordinates_dino = pg.Rect(self.position_x, self.position_y, self.current_image.get_rect()[2], self.current_image.get_rect()[3])
        if coordinates_dino.collidelist(list_objs) >= 0:
            return True
        return False
