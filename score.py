import pygame

# Import constants for color stuffs
from player import(COLORS, RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO,
                 VIOLET, BLACK, WHITE)

class Score:

    def __init__(self, screen):

        # Get a font object with the proper font we want to use
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.screen = screen

        # Keep track of the score, and the way score adds up
        self.score = 0
        self.perLevel = 50
        self.levels = 0

        # Initial font information for displaying
        self.update()

    def update(self):
        """
        This function will update the score that is displayed onto the screen.
        :return: None
        """

        # Update the score
        self.score += (self.perLevel * self.levels)
        self.levels += 1

        # Updaet the surface and the rect that will be displayed
        self.fontSurf = self.font.render(str(self.score), True, BLACK)
        self.fontRect = self.fontSurf.get_rect()
        self.fontRect.left = self.screen.get_width() - self.fontRect.width
        self.fontRect.top = self.fontRect.height // 2

    def draw(self):
        """
        This function will draw the text onto the screen
        :return: None
        """

        self.screen.blit(self.fontSurf, self.fontRect)
