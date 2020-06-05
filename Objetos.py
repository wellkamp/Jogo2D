import pygame


class Obj:
    def __init__(self, x, y, pos, local):
        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)
        self.sprite.image = pygame.image.load(local).convert_alpha()
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y
        self.sprite.pos = pos

        self.list = ['assets/star1.png', 'assets/star2.png',
                     'assets/star3.png', 'assets/star4.png']
        self.list1 = ['assets/estrada_1.png', 'assets/estrada_2.png']
        self.frame = 0

    def updateStarAnim(self):
        self.frame += 1
        if self.frame > 3:
            self.frame = 0

        self.sprite.image = pygame.image.load(self.list[self.frame])

    def updateEstradaAnim(self):
        self.frame += 1
        if self.frame > 1:
            self.frame = 0

        self.sprite.image = pygame.image.load(self.list1[self.frame])

    def setX(self, valor):
        self.sprite.rect[0] = valor

    def getX(self):
        return self.sprite.rect[0]

    def getY(self):
        return self.sprite.rect[1]

    def setY(self, valor):
        self.sprite.rect[1] = valor

    def getPos(self):
        return self.sprite.pos

    def setPos(self, valor):
        self.sprite.pos = valor + self.pos

    def setImage(self, local):
        self.sprite.image = local

    def getImage(self):
        return self.sprite.image
