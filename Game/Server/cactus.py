import random as rad

class Cactus(object):
    def __init__(self, positionX, positionY, image):
        self.positionX = positionX
        self.positionY = positionY
        self.image = image
        self.show = True

    def changePosition(self):
        
        self.positionX = self.positionX - 20

        if self.positionX:
            self.show = False

        return self.positionX

    def randomCactus(self):
        
        sequence = [True, False]
        self.show = rad.choice(sequence)
        