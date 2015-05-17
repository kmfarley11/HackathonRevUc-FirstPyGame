__author__ = 'Kevin'
import pygame, time, random
import player, design, enemy

class Game(object):
    """ This class represents an instance of the game. If we need to
        reset the game we'd just need to create a new instance of this
        class. """

    startTime = time.time()

    def __init__(self):
        """ Constructor. Create all our attributes and initialize
        the game. """
        self.game_over = False

        # Create sprite lists
        self.enemy_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        # Create the player
        self.player = player.Player()
        self.all_sprites_list.add(self.player)

        self.enemyDefeated = False

        # Create the enemy(ies)
        i = design.difficulty
        while i > 0:
            my_enemy = enemy.Enemy()
            my_enemy.rect.x = random.randrange(design.SCREEN_HEIGHT)
            my_enemy.rect.y = random.randrange(-300, design.SCREEN_HEIGHT)
            self.enemy_list.add(my_enemy)
            self.all_sprites_list.add(my_enemy)
            i -= 1

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
                    if design.gameWon : design.difficulty += 1
                    self.__init__()

        return False

    def collisionCheck(self):
        """
        This method is run each time through the frame. It
        updates positions and checks for collisions.
        """
        if not self.game_over:
            # Move all the sprites
            self.all_sprites_list.update(self.player.rect.x,self.player.rect.y)

            i = 0
            for en in self.enemy_list:
                if en.health <= 0:
                    #en.update2(en.rect.x,en.rect.y,True)
                    self.enemy_list.remove(en)
                    i += 1

            self.enemyDefeated = (i == len(self.enemy_list))

            # See if the player block has collided with anything.
            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.enemy_list, self.enemyDefeated)

            self.enemyDefeated = False

            # Check the list of collisions.
            for enem in blocks_hit_list:
                if self.player.state == "attacking" and ((time.time()-self.startTime) * 1000) >= 100:
                    self.startTime = time.time()
                    enem.health -= 2
                    deltax = enem.rect.x - self.player.rect.x
                    deltay = enem.rect.y - self.player.rect.y
                    enem.update2(deltax,deltay,False)

                    #design.bounce(self.my_enemy)# for later implementation?
                    # sword position must  match up with collision area to do damage

                else :
                    self.player.health -= 1
                    #design.bounce(self.player) # for later implementation?
                print('player health: ',self.player.health)
                i = 0
                for enemy in self.enemy_list :
                    print('enemy ', i,' health: ',enemy.health)
                    i += 1
                print('collision occurred')

            if len(self.enemy_list) == 0 :
                design.gameWon = True
                self.game_over = True
            if self.player.health <= 0 :
                design.gameWon = False
                self.game_over = True


    def frameDisplay(self, screen):
        """ Display everything to the screen for the game. """
        #screen.fill(design.GREEN)
        #dsign.makeWalls(screen)
        screen.blit(design.background, [0, 0])
        #pygame.draw.rect(screen,design.BLUE,pygame.Surface.Rect,50)
        if self.game_over:
            # font = pygame.font.Font("Serif", 25)
            font = pygame.font.SysFont("sans-serif", 50)
            if design.gameWon :
                text = font.render("You won!!! click to restart",True,design.BLACK)
            else :
                text = font.render("Game Over, click to restart", True, design.BLACK)
            center_x = (design.SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (design.SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        if not self.game_over:
            self.all_sprites_list.draw(screen)

        pygame.display.flip()

