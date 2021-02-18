import pygame
from random import randint, choice

# Import constants for color stuffs
from player import(COLORS, RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO,
                 VIOLET, BLACK, WHITE)

# Indication for open and closed cells in the maze
OPEN = "_"
CLOSED = "&"

# Params for the maze
TURNS = 5
LENGTH = .45

# Directions the generator can move
DIRECTIONS = [[0, -1], [0, 1], [-1, 0], [1, 0]]
XMOVE = 0
YMOVE = 1


class Maze:

    def __init__(self, screen):

        # Color of the individual cells
        self.cell_color = COLORS[WHITE]
        self.screen = screen
        self.wallRects = []
        self.wallSurfs = []
        self.exitRect = None
        self.exitSurf = None


    def generate(self, xdim, ydim):
        """
        This function will generate a maze using the random walk algorithm.
        :param xdim: Number of cells in the x direction.
        :param ydim: Number of cells in the y direction.
        :return: A list of rectangles representing the cells in the maze. And a rect
                 representing the exit cell for the maze.
        """

        # Clear the information being stored if necessary
        self.wallRects.clear()
        self.wallSurfs.clear()

        # Create a list for the maze generation
        maze = [[CLOSED for i in range(xdim)] for i in range(ydim)]

        # Figure out the parameters for number of turns and max walk length
        numTurns = TURNS * xdim
        maxLen = int(xdim * LENGTH)

        xloc, yloc = 0, 0

        # While the generator can still turn
        while numTurns > 0:

            walk = randint(0, maxLen)
            dir = choice(DIRECTIONS)

            # "Carve" out the path in the maze
            for i in range(walk):

                # Update the cell in the maze, and the location
                maze[xloc][yloc] = OPEN
                xloc = xloc + dir[XMOVE]
                yloc = yloc + dir[YMOVE]

                # Bounds checking
                if xloc < 0:
                    xloc = 0
                elif xloc >= xdim:
                    xloc = xdim - 1

                if yloc < 0:
                    yloc = 0
                elif yloc >= ydim:
                    yloc = ydim - 1

            numTurns -= 1

        # Calculate the dimensions of each cell
        cellWidth = self.screen.get_width() / xdim
        cellHeight = self.screen.get_height() / ydim
        rectangles = []

        # Go through the cells of the maze, generating the rectangles
        # in their proper positions on the map
        for row in range(len(maze)):
            for cell in range(len(maze[row])):

                # We are only generating closed rectangles
                if maze[row][cell] == CLOSED:

                    # Create a surface of the right dimensions and color
                    curr = pygame.Surface((int(cellWidth), int(cellHeight)))
                    curr.fill(self.cell_color)
                    self.wallSurfs.append(curr)

                    # Create the rectangle at the proper location
                    cellRect = curr.get_rect()
                    cellRect.left = cellWidth * cell
                    cellRect.top = cellHeight * row
                    self.wallRects.append(cellRect)
                    rectangles.append(cellRect)

        exit = pygame.Surface((int(cellWidth), int(cellHeight)))
        exit.fill(COLORS[GREEN])
        exitRect = exit.get_rect()
        found = False

        # Find a cell to choose to be the end. Preference for the cell at the bottom right
        for row in range(len(maze) - 1, 0, -1):
            for cell in range(len(maze[row]) - 1, 0, -1):

                # Find the first cell thats open, and set it as the exit cell
                if maze[row][cell] == OPEN:
                    exitRect.left = cellWidth * cell
                    exitRect.top = cellHeight * row
                    found = True
                    break

            # Stop searching once an exit is found
            if found:
                break

        self.exitSurf = exit
        self.exitRect = exitRect

        return rectangles, exitRect


    def draw(self):
        """
        This function will draw the rectangles of the maze on the screen.
        :return: None
        """

        # Print out the exit cell
        self.screen.blit(self.exitSurf, self.exitRect)

        # Go through the cells
        for i in range(len(self.wallRects)):
            self.screen.blit(self.wallSurfs[i], self.wallRects[i])
