__author__ = 'Kevin'
import pygame, design
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = self.enemy1
        self.rect = self.image.get_rect()
        '''
        self.rect.x = 750
        self.rect.y = 320
        '''
        self.side = 0
        self.speed = 15
        self.it = 0
        #self.hidden = False
        self.health = 100

    #TODO: maybe add rand arithmetic to sometimes run away
    def update(self,x,y):
        if(self.rect.right < x + 50) and not self.rect.colliderect(design.right): self.rect.x += self.speed
        if(self.rect.bottom < y + 175) and not self.rect.colliderect(design.bottom): self.rect.y += self.speed
        if(self.rect.left > x + 65) and not self.rect.colliderect(design.left): self.rect.x -= self.speed
        if(self.rect.top > y - 40) and not self.rect.colliderect(design.top): self.rect.y -= self.speed

    def update2(self,x,y,hidden):
        # use delta values to set signs for proper bounce direction
        if (x < 0) : x = -1
        else : x = 1
        if (y < 0) : y = -1
        else : y = 1

        if not self.rect.colliderect(design.right): self.rect.x += self.speed + x * 15
        if not self.rect.colliderect(design.bottom): self.rect.y += self.speed + y * 15
        if not self.rect.colliderect(design.left): self.rect.x -= self.speed - x * 15
        if not self.rect.colliderect(design.top): self.rect.y -= self.speed - y * 15

        if hidden : del self.enemy1

    enemy1 = pygame.image.load('resources/crazyShiz.png')