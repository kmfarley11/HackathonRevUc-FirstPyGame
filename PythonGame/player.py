__author__ = 'Kevin'
import pygame
import design

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = self.playerSide[0][0]
        #self.image.fill(design.RED)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 320
        self.side = 0
        self.speed = 35
        self.facingEnemy = False
        self.it = 0
        self.health = 100
        self.state = "walking"

    def update(self, x, y):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and not self.rect.colliderect(design.right):
            self.rect.x += self.speed
            self.it += 1
            self.side = 0
            if self.rect.x > x : self.facingEnemy = True
        if keys[pygame.K_DOWN] and not self.rect.colliderect(design.bottom):
            self.rect.y += self.speed
            self.it += 1
            self.side = 1
            if self.rect.y < y : self.facingEnemy = True
        if keys[pygame.K_LEFT] and not self.rect.colliderect(design.left):
            self.rect.x -= self.speed
            self.it += 1
            self.side = 2
            if self.rect.x < x : self.facingEnemy = True
        if keys[pygame.K_UP] and not self.rect.colliderect(design.top):
            self.rect.y -= self.speed
            self.it += 1
            self.side = 3
            if self.rect.y > y : self.facingEnemy = True

        if self.it > 1000 : self.it = 0

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            if self.it % 3 == 0 : self.image = self.playerSword[0][self.side]
            else : self.image = self.playerSword[1][self.side]
            self.rect.fit(self.image.get_rect())
            self.state = "attacking"
            return

        if self.it % 3 == 0 : self.image = self.playerSide[0][self.side]
        else : self.image = self.playerSide[1][self.side]
        self.rect.fit(self.image.get_rect())

        self.state = "walking"

    playerSide1 = [pygame.image.load('resources/sprite_1.png'),pygame.image.load('resources/sprite_2.png'),pygame.image.load('resources/sprite_3.png'),pygame.image.load('resources/sprite_4.png')]
    playerSide2 = [pygame.image.load('resources/sprite_5.png'),pygame.image.load('resources/sprite_6.png'),pygame.image.load('resources/sprite_7.png'),pygame.image.load('resources/sprite_8.png')]
    playerSide = [playerSide1, playerSide2]

    playerSword1 = [pygame.image.load('resources/sprite_9.png'),pygame.image.load('resources/sprite_10.png'),pygame.image.load('resources/sprite_11.png'),pygame.image.load('resources/sprite_12.png')]
    playerSword2 = [pygame.image.load('resources/sprite_13.png'),pygame.image.load('resources/sprite_14.png'),pygame.image.load('resources/sprite_15.png'),pygame.image.load('resources/sprite_16.png')]
    playerSword = [playerSword1, playerSword2]