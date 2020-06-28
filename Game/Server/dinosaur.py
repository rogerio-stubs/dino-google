class Dinosaur(object):
    def __init__(self, position_x, position_y, images):
        self.position_x = position_x
        self.position_y = position_y
        self.images = images
        self.index = True
        self.current_image = self.images[0] # alterar para inicial
        self.image_jump = [self.images[0]]
        self.image_walk = [self.images[1], self.images[2]]
        self.image_down = [self.images[3], self.images[4]]

    def jump(self, jump_count):
        self.position_y -= (jump_count * abs(jump_count)) * 0.2
        self.current_image = self.image_jump[0]

    def down(self):
        if self.index:
            self.current_image = self.image_down[0]
            self.index = False
        else:
            self.current_image = self.image_down[1]
            self.index = True

    def walk(self):
        if self.index:
            self.current_image = self.image_walk[0]
            self.index = False
        else:
            self.current_image = self.image_walk[1]
            self.index = True
