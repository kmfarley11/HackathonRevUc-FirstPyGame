__author__ = 'Kevin'
import pygame

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# set up screen sizing
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720



# image loading
bckgrnd = pygame.image.load('resources/nes_zelda_tour_screenshot1.png')
background = pygame.transform.scale(bckgrnd,(1280, 720))

def drawBackground(screen, background):
    screen.blit(background, [0, 0])

'''
def refreshScreen(screen,right,down,one):
    #screen.fill(GREEN)
    #pygame.draw.circle(screen, RED, (right, down), 25, 1)
    drawBackground(screen,background)
    if(one):
        screen.blit(playerLeft1, [right, down])
    elif(not one):
        screen.blit(playerLeft2, [right, down])
    pygame.display.update()
    '''