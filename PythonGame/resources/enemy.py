__author__ = 'Kevin'
import pygame
import design
import random
'''
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.image = self.enemySide[0][0]
        self.image.fill(design.RED)
        self.rect = self.image.get_rect()
        self.side = 0
        self.speed = 10
        self.it = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.x != 1250:
            self.rect.x += self.speed
            self.it += 1
            self.side = 0
            self.sword = 1
        if keys[pygame.K_DOWN] and self.rect.y != 680:
            self.rect.y += self.speed
            self.it += 1
            self.side = 1
            self.sword = 3
        if keys[pygame.K_LEFT] and self.rect.x != 0:
            self.rect.x -= self.speed
            self.it += 1
            self.side = 0
            self.sword = 2
        if keys[pygame.K_UP] and self.rect.y != 0:
            self.rect.y -= self.speed
            self.it += 1
            self.side = 1
            self.sword = 0

        if self.it > 1000 : self.it = 0

        if keys[pygame.K_SPACE]:
            self.image = self.playerSword[self.sword]
            return


        if self.it % 3 == 0 : self.image = self.playerSide[self.side][0]
        else : self.image = self.playerSide[self.side][1]

    playerSide1 = [pygame.image.load('resources/sprite_1.png'),pygame.image.load('resources/sprite_2.png')]
    playerSide2 = [pygame.image.load('resources/sprite_3.png'),pygame.image.load('resources/sprite_4.png')]
    playerSide = [playerSide1, playerSide2]

    playerSword = [pygame.image.load('resources/sprite_5.png'),pygame.image.load('resources/sprite_6.png'),pygame.image.load('resources/sprite_7.png'),pygame.image.load('resources/sprite_8.png')]
'''