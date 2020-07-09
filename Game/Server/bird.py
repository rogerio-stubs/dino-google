class Bird(object): # Tb é um dinossauro
    def __init__(self, source, position_y, images):
        self.source = source
        self.position_x = source
        self.position_y = position_y
        self.images = images
        self.index = True
        self.current_image = self.images[0]
        self.speed = 0

    def change_position(self):
        self.position_x = self.position_x - self.speed

        if self.position_x == 0:
            self.position_x = self.source

    def fly(self):
        if self.index:
            self.current_image = self.images[0]
            self.index = False
        else:
            self.current_image = self.images[1]
            self.index = True

    def speed_up(self, value):
        self.speed = value
