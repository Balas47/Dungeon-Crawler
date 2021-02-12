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

if __name__ == "__main__":

    pygame.init()

    # Setting up the game window
    width = 500
    height = 500
    screen = pygame.display.set_mode([width, height])

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

        screen.fill(COLORS[ORANGE])
        pygame.display.flip()

    pygame.quit()
