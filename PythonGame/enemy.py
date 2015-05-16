__author__ = 'Kevin'
import pygame
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = self.enemy1
        #self.image.fill(design.RED)
        self.rect = self.image.get_rect()
        self.rect.x = 750
        self.rect.y = 320
        self.side = 0
        self.speed = 10
        self.it = 0
        self.health = 100

    def update(self):
        ai = randint(0,200)

        if ai % 2 == 0 and self.rect.x != 1250:
            self.rect.x += self.speed
            self.it += 1
            self.side = 0
        if ai % 3 == 0 and self.rect.y != 680:
            self.rect.y += self.speed
            self.it += 1
            self.side = 1
        if  ai % 4 == 0 and self.rect.x != 0:
            self.rect.x -= self.speed
            self.it += 1
            self.side = 0
        if  ai % 5 == 0 and self.rect.y != 0:
            self.rect.y -= self.speed
            self.it += 1
            self.side = 1
        else :
            return

        if self.it > 1000 : self.it = 0


        #if self.it % 3 == 0 : self.image = self.playerSide[self.side][0]
        #else : self.image = self.playerSide[self.side][1]

    enemy1 = pygame.image.load('resources/crazyShiz.png')
    #playerSide1 = [pygame.image.load('resources/sprite_1.png'),pygame.image.load('resources/sprite_2.png')]
    #playerSide2 = [pygame.image.load('resources/sprite_3.png'),pygame.image.load('resources/sprite_4.png')]
    #playerSide = [playerSide1, playerSide2]

    #playerSword = [pygame.image.load('resources/sprite_5.png'),pygame.image.load('resources/sprite_6.png'),pygame.image.load('resources/sprite_7.png'),pygame.image.load('resources/sprite_8.png')]
