__author__ = 'Kevin'
import pygame
import player, design

class Game(object):
    """ This class represents an instance of the game. If we need to
        reset the game we'd just need to create a new instance of this
        class. """

    def __init__(self):
        """ Constructor. Create all our attributes and initialize
        the game. """

        self.health = 100
        self.game_over = False

        # Create sprite lists
        self.block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        # Create the player
        self.player = player.Player()
        self.all_sprites_list.add(self.player)
        '''
        # Create the block sprites
        for i in range(50):
            #block = Block()

            block.rect.x = random.randrange(SCREEN_WIDTH)
            block.rect.y = random.randrange(-300, SCREEN_HEIGHT)

            self.block_list.add(block)
            self.all_sprites_list.add(block)'''

    def processEvents(self):
        """ Process all of the events. Return a "True" if we need
            to close the window. """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()

        return False

    def collisionCheck(self):
        """
        This method is run each time through the frame. It
        updates positions and checks for collisions.
        """
        if not self.game_over:
            # Move all the sprites
            self.all_sprites_list.update()

            # See if the player block has collided with anything.
            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, True)

            # Check the list of collisions.
            for block in blocks_hit_list:
                self.health -= 1
                print(self.health)

            #if len(self.block_list) == 0:
            #    self.game_over = True

    def frameDisplay(self, screen):
        """ Display everything to the screen for the game. """
       #screen.fill(design.GREEN)
        screen.blit(design.background, [0, 0])
        #pygame.draw.rect(screen,design.BLUE,pygame.Surface.Rect,50)
        if self.game_over:
            # font = pygame.font.Font("Serif", 25)
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, click to restart", True, design.BLACK)
            center_x = (design.SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (design.SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        if not self.game_over:
            self.all_sprites_list.draw(screen)

        pygame.display.flip()

