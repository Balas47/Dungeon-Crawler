import sys, pygame

#Color values for the rainbow in ROYGBIV, black, and white order
COLORS = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0),
          (0, 0, 255), (46, 43, 95), (139, 0, 255), (0, 0, 0), (255, 255, 255)]

# Constants for accessing the color values
RED = 0
ORANGE = 1
YELLOW = 2
GREEN = 3
BLUE = 4
INDIGO = 5
VIOLET = 6
BLACK = 7
WHITE = 8

# The player class controls the position of the player on the screen, as
# well as how the different inputs effect what happens for the player.
class Player:

    def __init__(self, screen):

        # The player will keep track of the dimensions of the player "model"
        # and the screen the player is going to be drawn on
        self.screen = screen
        self.width = 10
        self.height = 10
        self.color = COLORS[VIOLET]

        # Initial position of the player
        self.x, self.y = 0, 0

    def draw(self, dim_x, dim_y):
        """
        This function will take care of actually drawing the player onto the
        game screen.
        :param dim_x: The x dimension of the screen.
        :param dim_y: The y dimension of the screen.
        """
        
        player_surf = pygame.Surface((self.width, self.height))
        player_surf.fill(self.color)

        # For now, drawing the player onto the center of the screen
        self.screen.blit(player_surf, (self.x, self.y))
    

if __name__ == "__main__":

    pygame.init()

    # Setting up the game window
    width = 500
    height = 500
    screen = pygame.display.set_mode([width, height])

    the_player = Player(screen)

    # Setting up the main loop
    run_game = True
    while run_game:

        # Quit the game when the user wants to
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

            # The escape key quits the game
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run_game = False

        # Print everything on the screen
        screen.fill(COLORS[ORANGE])
        the_player.draw(width, height)
        pygame.display.flip()

    pygame.quit()
