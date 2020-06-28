import random as rad

class Cactus(object):
    def __init__(self, position_x, position_y, images):
        self.position_x = position_x
        self.position_y = position_y
        self.images = images
        self.speed = 5
        self.matrix_images = list()
        self.current_image = self.images[0]

    def create_matrix_position(self):
        # matriz nx2 com [tempo, imagem]
        for indice in range(0, 100):
            self.matrix_images.append(indice)

    def change_position(self):
        # O cacto irá aparecer somente quando:
        # depois de uma distância no qual não impossibilite o jogo
        # após essa distância fica livre a criação de um novo cacto
        # Tratando como self.position limita a um unico caacto
        self.position_x = self.position_x - self.speed

        if self.position_x == 0:
            self.position_x = 750

    def speed_up(self):
        # A velocidade aumenta depois de determinado tempo ou qtd pontos
        pass
