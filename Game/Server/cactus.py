import random

class Cactus(object):
    def __init__(self, position_x, position_y, images):
        self.position_x = position_x
        self.position_y = position_y
        self.images = images
        self.speed = 0
        self.current_image = self.images[0]

    def choose_image(self, size_x, floor):
        indice = random.choice(range(0, 5))
        self.current_image = self.images[indice]
        self.position_x = size_x

        dimensions = self.current_image.get_rect()
        dimensions_floor = floor.current_image.get_rect()
        self.position_y = floor.position_y + dimensions_floor[3] - dimensions[3]

    def change_position(self):
        self.position_x = self.position_x - self.speed

    def speed_up(self, value):
        self.speed = value
