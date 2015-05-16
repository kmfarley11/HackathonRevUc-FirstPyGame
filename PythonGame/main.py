__author__ = 'Kevin'
__author__ = 'Sandro'
print('this is the main python file (base of the project)')
import pygame, sys, design, player
from pygame.locals import *
pygame.init()

# TODO: eventually draw/ load images, not circles and rects
# set up the window

screen = pygame.display.set_mode((1280, 720), 0, 32)
pygame.display.set_caption('PyGame')
speed = player.speed
one = 1
it = 0

# draw on the surface object
right = 50
down = 50
screen.fill(design.GREEN)
screen.blit(design.playerLeft1, [right, down])
#pygame.draw.circle(screen, design.RED, (right, down), 25, 1)

# This is the game loop, all events will occur here
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    # TODO: later feature to not allow for two buttons held at same time

    # player
    # key press recognition (up down left right)
    if keys[pygame.K_RIGHT] and right != 1150:
        if (it % 5) == 0 : one = not one
        right += speed
    if keys[pygame.K_DOWN] and down != 680:
        player.move(right, down)
        if (it % 5) == 0 : one = not one
        down += speed
    if keys[pygame.K_LEFT] and right != 0:
        if (it % 5) == 0 : one = not one
        right -= speed
    if keys[pygame.K_UP] and down != 0:
        if (it % 5) == 0 : one = not one
        down -= speed

    if it > 1000 : it = 0
    it += 1
    # update display for each iteration of game running instance
    design.refreshScreen(screen,right,down,one)