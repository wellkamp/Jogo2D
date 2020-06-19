import pygame
import random

from Objetos import Obj
from Carro import Carro


pygame.init()

# Sons
pygame.mixer.init()
pygame.mixer.music.load('assets/sounds/backwav.wav')
pygame.mixer.music.play()
curve = pygame.mixer.Sound('assets/sounds/curve.wav')
collisionSound = pygame.mixer.Sound('assets/sounds/Collision.wav')
starSound = pygame.mixer.Sound('assets/sounds/star.wav')

# BackGround
window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption('Jogo de carro Wellington')
bg = pygame.image.load('assets/forest.png')
bg2 = pygame.image.load('assets/forest.png')

# Objetos
estrada = Obj(400, 0, 0, 'assets/estrada_1.png')
carro_pista = Obj(420, 0, 10, 'assets/carro_pista.png')
carro_pista2 = Obj(520, 200, 10, 'assets/carro_pista.png')
carro_pista3 = Obj(640, 550, 10, 'assets/carro_pista.png')
carro_player = Carro(410, 550, 1, 'assets/carro_player.png')
star = Obj(420, 510, 10, 'assets/star1.png')
banana = Obj(760, 400, 10, 'assets/banana.png')

# Variaveis
points = 200
position = [420, 520, 640, 760]
loop = True
clock = pygame.time.Clock()
valor = carro_pista.getY()
valor2 = carro_pista2.getY()
valor4 = carro_pista3.getY()
valor3 = star.getY()
valor5 = banana.getY()
movimentoX = carro_player.getX()
score = 0
jogando = True


def draw():
    if jogando:
        pygame.font.init()
        font_default = pygame.font.get_default_font()
        font_size = pygame.font.SysFont(font_default, 60, True)
        font_text = '{}'.format(str(score))
        font_render = font_size.render(font_text, True, (255, 255, 255))
        window.blit(bg, (0, 0))
        window.blit(bg, (720, 0))
        window.blit(estrada.sprite.image, estrada.sprite.rect)
        window.blit(font_render, (1000, 0))
        window.blit(carro_pista.sprite.image, carro_pista.sprite.rect)
        window.blit(carro_pista2.sprite.image, carro_pista2.sprite.rect)
        window.blit(carro_pista3.sprite.image, carro_pista3.sprite.rect)
        window.blit(carro_player.sprite.image, carro_player.sprite.rect)
        window.blit(star.sprite.image, star.sprite.rect)
        window.blit(banana.sprite.image, banana.sprite.rect)


def fases(valor):
    if valor <= 500:
        clock.tick(10)
    elif valor <= 1000:
        clock.tick(15)
    elif valor <= 2000:
        clock.tick(20)
    elif valor <= 3000:
        clock.tick(25)
    else:
        clock.tick(30)


def crash():
    collisionSound.play()
    font_default = pygame.font.get_default_font()
    font_size = pygame.font.SysFont(font_default, 60, True)
    font_text = 'Game Over! Sua pontuação: {}'.format(str(score))
    font_render = font_size.render(font_text, True, (255, 0, 0))
    window.blit(font_render, (300, 300))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


def collision():
    global score
    global jogando

    carro1 = pygame.sprite.spritecollide(
        carro_player.sprite, carro_pista.group, False)
    carro2 = pygame.sprite.spritecollide(
        carro_player.sprite, carro_pista2.group, False)

    carro1 = pygame.sprite.spritecollide(
        carro_player.sprite, carro_pista.group, False)

    carro3 = pygame.sprite.spritecollide(
        carro_player.sprite, carro_pista3.group, False)

    star_colide = pygame.sprite.spritecollide(
        carro_player.sprite, star.group, False)

    banana_colide = pygame.sprite.spritecollide(
        carro_player.sprite, banana.group, False)

    if carro1 or carro2 or carro3:
        jogando = False
        crash()

    if star_colide:
        score += 100
        starSound.play()
        star.setX(-100)

    if banana_colide:
        temp = carro_player.sprite.image
        carro_player.rotate(temp, 45)


# LOOP principal
while loop:
    fases(score)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and movimentoX <= 640:
                movimentoX = movimentoX + 115
                curve.play()
                carro_player.setX(movimentoX)

            if event.key == pygame.K_LEFT and movimentoX >= 525:
                movimentoX = movimentoX - 115
                curve.play()
                carro_player.setX(movimentoX)
            '''
            if event.key == pygame.K_UP:
                movimentoy = movimentoy - 10
                carro_player.setY(movimentoy)
            '''

    valor = valor + carro_pista.getPos()
    valor2 = valor2 + carro_pista2.getPos()
    valor3 = valor3 + star.getPos()
    valor4 = valor4 + carro_pista3.getPos()
    valor5 = valor5 + banana.getPos()

    carro_pista.setY(valor)
    carro_pista2.setY(valor2)
    carro_pista3.setY(valor4)
    star.setY(valor3)
    banana.setY(valor5)

    if carro_pista.getY() > 750:
        carro_pista.setX(random.choice(position))
        valor = -100

    if carro_pista2.getY() > 750:
        carro_pista2.setX(random.choice(position))
        valor2 = -100

    if carro_pista3.getY() > 750:
        carro_pista3.setX(random.choice(position))
        valor4 = -100

    if star.getY() > 750:
        star.setX(random.choice(position))
        valor3 = -100

    if banana.getY() > 750:
        banana.setX(random.choice(position))
        valor5 = -100

    estrada.updateEstradaAnim()
    star.updateStarAnim()
    draw()
    collision()
    score += 1
    pygame.display.update()


'''
fases(score)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and movimentoX <= 640:
        movimentoX = movimentoX + 115
        carro_player.setX(movimentoX)

    if pressed[pygame.K_LEFT] and movimentoX >= 525:
        movimentoX = movimentoX - 115
        carro_player.setX(movimentoX)

    if pressed[pygame.K_UP]:
        movimentoy = movimentoy - 10
        carro_player.setY(movimentoy)

    if pressed[pygame.K_DOWN]:
        movimentoy = movimentoy + 10
        carro_player.setY(movimentoy)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
'''
