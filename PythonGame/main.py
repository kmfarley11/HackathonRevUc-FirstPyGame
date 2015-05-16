__author__ = 'Kevin'
__author__ = 'Sandro'
print('this is the main python file (base of the project)')
import pygame, sys, design
from pygame.locals import *
pygame.init()

# TODO: eventually draw/ load images, not circles and rects
# set up the window
display_surface = pygame.display.set_mode((1000, 1000), 0, 32)
pygame.display.set_caption('PyGame')

# draw on the surface object
right = 50
down = 50
display_surface.fill(design.BLACK)
pygame.draw.circle(display_surface, design.RED, (right, down), 25, 1)

# This is the game loop, all events will occur here
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    # TODO: later feature to not allow for two buttons held at same time

    # key press recognition (up down left right)
    if keys[pygame.K_RIGHT]:
        display_surface.fill(design.BLACK)
        pygame.draw.circle(display_surface, design.RED, (right, down), 25, 1)
        right = right + 1
    if keys[pygame.K_DOWN]:
        display_surface.fill(design.BLACK)
        pygame.draw.circle(display_surface, design.RED, (right, down), 25, 1)
        down = down + 1
    if keys[pygame.K_LEFT]:
        display_surface.fill(design.BLACK)
        pygame.draw.circle(display_surface, design.RED, (right, down), 25, 1)
        right = right - 1
    if keys[pygame.K_UP]:
        display_surface.fill(design.BLACK)
        pygame.draw.circle(display_surface, design.RED, (right, down), 25, 1)
        down = down - 1

    # update display for each iteration of game running instance
    pygame.display.update()