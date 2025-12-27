import pygame

class Shape:
    def __init__(self, sizeX, sizeY, color):
        self.sizeXSelf = sizeX
        self.sizeYSelf = sizeY
        self.colorSelf = color

class Rectangle(Shape):
    def __init__(self, sizeX, sizeY, color):
        super().__init__(sizeX, sizeY, color)

    def draw(self, screen, posX, posY):
        rectInstance = pygame.Rect(posX, posY, self.sizeXSelf, self.sizeYSelf)
        pygame.draw.rect(screen, self.colorSelf, rectInstance)

class Circle(Shape):
    def __init__(self, sizeX, sizeY, color):
        super().__init__(sizeX, sizeY, color)




    
