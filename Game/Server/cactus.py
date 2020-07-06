import random as rad

class Cactus(object):
    def __init__(self, position_y, images):
        self.position_x = 750
        self.position_y = position_y
        self.images = images
        self.speed = 0
        self.matrix_images = images
        self.current_image = self.images[0]

    def create_matrix_position(self):
        print(self.matrix_images)
        # gerar uma matriz com 4 posições, quando um 
        # cacto chega x=0 limpa e gera outro no mesmo indice
        # então utiliza o próximo indiece 

    def change_position(self):

        self.position_x = self.position_x - self.speed

        if self.position_x == 0:
            self.position_x = 750

    def speed_up(self, value):
        self.speed = value
