__author__ = 'Kevin'

print('this is the main python file (base of the project)')
import pygame, design, game

def main():
    pygame.init()

    # set up the window
    pygame.display.set_caption('MyGame')
    one = 1
    it = 0

    # draw on the surface object
    right = 50
    down = 50
    #screen.blit(pygame.image.load('resources/nes_zelda_tour_screenshot1.png'), [right, down])

    # This is the game loop, all events will occur here
    clock = pygame.time.Clock()
    thisGame = game.Game()
    while True:

        terminate = thisGame.processEvents()

        # TODO: later feature to not allow for two buttons held at same time
        thisGame.collisionCheck()
        thisGame.frameDisplay(design.screen)

        # This call will regulate your FPS (to be 40 or less)
        clock.tick(40)

        if terminate :
            pygame.mixer.sound.stop()
            break
    # stop sound
    pygame.quit()

if __name__ == "__main__": main()
