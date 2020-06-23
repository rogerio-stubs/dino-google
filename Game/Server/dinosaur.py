class Dinosaur(object):
    def __init__(self, position_x, position_y, image):
        self.position_x = position_x
        self.position_y = position_y
        self.image = image

    def jump(self, jump_count):
        self.position_y -= (jump_count * abs(jump_count)) * 0.2

    def down(self):
        print('abaixar')
        