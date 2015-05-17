__author__ = 'Kevin'
import pygame, player, enemy

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# set up screen sizing
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

right = pygame.Rect((1250,0),(100,720))
bottom = pygame.Rect((0,630),(1280,75))
left = pygame.Rect((0,0),(100,720))
top = pygame.Rect((0,0),(1280,75))

gameWon = False
difficulty = 1

#def makeWalls(screen) :
    # right? down? width height
    #pygame.draw.rect(screen, BLACK, right,0)
    #pygame.draw.rect(screen, BLACK, bottom,0)
    #pygame.draw.rect(screen, BLACK, left,0)
    #pygame.draw.rect(screen, BLACK, top,0)
    #pygame.display.update()

# image loading
bckgrnd = pygame.image.load('resources/zelda720.png')
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