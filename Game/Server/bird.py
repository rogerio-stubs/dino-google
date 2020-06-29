class Bird(object): # Tb é um dinossauro
    def __init__(self, position_x, position_y, images):
        self.position_x = position_x
        self.position_y = position_y
        self.images = images
        self.index = True
        self.current_image = self.images[0]
        self.speed = 5

    def change_position(self):
        self.position_x = self.position_x - self.speed

        if self.position_x == 0:
            self.position_x = 750

    def speed_up(self):
        # A velocidade aumenta depois de determinado tempo ou qtd pontos
        pass

    def fly(self):
        if self.index:
            self.current_image = self.images[0]
            self.index = False
        else:
            self.current_image = self.images[1]
            self.index = True
            