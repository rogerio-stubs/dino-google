class Background(object):
    def __init__(self, position_x, position_y, current_image):
        self.position_x = position_x
        self.final_position_x = 10
        self.position_y = position_y
        self.current_image = current_image[0]
        self.speed = 0

    def move(self):
        self.position_x -= self.speed

        if self.position_x == -2400:
            self.position_x = 2400

    def speed_up(self, value):
        self.speed = value
        