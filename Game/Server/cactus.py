import random

class Cactus(object):
    def __init__(self, position_x, position_y, images):
        self.position_x = position_x
        self.position_y = position_y
        self.images = images
        self.speed = 0
        self.current_image = self.images[0]

    def choose_image(self, size_x):
        indice = random.choice(range(0, 5))
        print(indice)
        self.current_image = self.images[indice]
        self.position_x = size_x

    def change_position(self):
        self.position_x = self.position_x - self.speed
        restart = self.speed * (-2)
        if self.position_x <= restart:
            self.position_x = 750

    def speed_up(self, value):
        self.speed = value
