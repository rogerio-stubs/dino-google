import random as rad

class Cactus(object):
    def __init__(self, position_x, position_y, speed, image):
        self.position_x = position_x
        self.position_y = position_y
        self.speed = speed
        self.image = image
        self.show = True

    def change_position(self):
        # O cacto irá aparecer somente quando:
        # depois de uma distância no qual não impossibilite o jogo
        # após essa distância fica livre a criação de um novo cacto
        # Tratando como self.position limita a um unico caacto
        self.position_x = self.position_x - self.speed

        if self.position_x:
            self.show = False

    def random_cactus(self):
        self.show = rad.choice([True, False])
        
    def speed_up(self):
        # A velocidade aumenta depois de determinado tempo ou qtd pontos
        pass
