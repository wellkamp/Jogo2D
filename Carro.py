import pygame


class Carro:
    def __init__(self, carx, cary, carpos, local):
        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)
        self.sprite.image = pygame.image.load(local).convert_alpha()
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = carx
        self.sprite.rect[1] = cary
        self.sprite.carpos = carpos

    def setX(self, valor):
        self.sprite.rect[0] = valor

    def getX(self):
        return self.sprite.rect[0]

    def getY(self):
        return self.sprite.rect[1]

    def setY(self, valor):
        self.sprite.rect[1] = valor

    def getPos(self):
        return self.sprite.carpos

    def setPos(self, valor):
        self.sprite.carpos = valor + self.carpos

    def setImage(self, local):
        self.sprite.image = local

    def getImage(self):
        return self.sprite.image

    def rotate(self, car, angle):
        self.sprite.image = pygame.transform.rotate(car, angle)
        rect = self.sprite.image.get_rect(center=(0, 0))
        return rect
