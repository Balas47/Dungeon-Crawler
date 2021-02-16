import sys, pygame
import player
import maze

# Import constants for color stuffs
from player import(COLORS, RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO,
                 VIOLET, BLACK, WHITE)


if __name__ == "__main__":

    pygame.init()

    # Setting up the game window
    width = 800
    height = 800
    screen = pygame.display.set_mode([width, height])

    the_player = player.Player(screen)

    # Set up the maze, and get the list of rects representing the walls
    the_maze = maze.Maze(screen)
    obstacles = the_maze.generate(20, 20)

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
        the_player.move(keys, obstacles)

        # Print everything on the screen
        screen.fill(COLORS[ORANGE])
        the_player.draw(width, height)
        the_maze.draw()
        pygame.display.flip()

    pygame.quit()
