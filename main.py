import sys, pygame
import player

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


if __name__ == "__main__":

    pygame.init()

    # Setting up the game window
    width = 500
    height = 500
    screen = pygame.display.set_mode([width, height])

    the_player = player.Player(screen)

    # Setting up the main loop
    run_game = True
    while run_game:

        for event in pygame.event.get():

            # Stop the main loop if necessary
            if event.type == pygame.QUIT:
                run_game = False

            # The escape key quits the game
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run_game = False

        # Take care of user inputs
        keys = pygame.key.get_pressed()
        the_player.move(keys)

        # Print everything on the screen
        screen.fill(COLORS[ORANGE])
        the_player.draw(width, height)
        pygame.display.flip()

    pygame.quit()
