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
        # corrigir em relação a imagem.
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
