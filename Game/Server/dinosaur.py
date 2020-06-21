class Dinosaur(object):
    def __init__(self, positionX, positionY, image):
        self.positionX = positionX
        self.positionY = positionY
        self.image = image

    def jump(self, jumpCount):
        self.positionY -= (jumpCount * abs(jumpCount)) * 0.2

    def down(self):
        print('abaixar')