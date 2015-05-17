__author__ = 'Kevin'
import pygame, design
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = self.enemy1
        self.rect = self.image.get_rect()
        self.rect.x = 750
        self.rect.y = 320
        self.side = 0
        self.speed = 15
        self.it = 0
        self.health = 100
        self.canBeHit = True

    #TODO: maybe add rand arithmetic to sometimes run away
    def update(self,x,y):
        if(self.rect.right < x + 50) and not self.rect.colliderect(design.right): self.rect.x += self.speed
        if(self.rect.bottom < y + 50) and not self.rect.colliderect(design.bottom): self.rect.y += self.speed
        if(self.rect.left > x + 65) and not self.rect.colliderect(design.left): self.rect.x -= self.speed
        if(self.rect.top > y - 40) and not self.rect.colliderect(design.top): self.rect.y -= self.speed

    enemy1 = pygame.image.load('resources/crazyShiz.png')