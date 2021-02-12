import pygame

# Import constants for color stuffs
from main import(COLORS, RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO,
                 VIOLET, BLACK, WHITE)

# The player class controls the position of the player on the screen, as
# well as how the different inputs effect what happens for the player.
class Player():

    def __init__(self, screen):

        # The player will keep track of the dimensions of the player "model"
        # and the screen the player is going to be drawn on
        self.screen = screen
        self.width = 10
        self.height = 10
        self.color = COLORS[VIOLET]

        # Initial position and speed of the player
        self.x, self.y = 0, 0
        self.x_speed, self.y_speed = .5, .5

        # Keep track of the player surface and rectangle
        self.player_surf = pygame.Surface((self.width, self.height))
        self.player_surf.fill(self.color)
        self.rect = self.player_surf.get_rect()


    def move(self, buttons):
        """
        This function will take care of the movement of the player
        :param buttons: The buttons the user pressed to determine direction
                       of the player movement
        """

        # Take care of the actual movement of the player
        if buttons[pygame.K_w]:
            self.y -= self.y_speed
            
        if buttons[pygame.K_a]:
            self.x -= self.x_speed

        if buttons[pygame.K_s]:
            self.y += self.y_speed

        if buttons[pygame.K_d]:
            self.x += self.x_speed

        # Make sure that the player cannot go off of the screen
        if 0 > self.x:
            self.x = 0
        elif self.x > self.screen.get_width() - self.width:
            self.x -= self.x_speed

        if 0 > self.y:
            self.y = 0
        elif self.y > self.screen.get_height() - self.height:
            self.y -= self.y_speed

        # Update the player rectangle
        self.rect.left = self.x
        self.rect.top = self.y


    def draw(self, dim_x, dim_y):
        """
        This function will take care of actually drawing the player onto the
        game screen.
        :param dim_x: The x dimension of the screen.
        :param dim_y: The y dimension of the screen.
        """
        
        # Update the position of the player on the screen
        #self.screen.blit(self.player_surf, (self.x, self.y))
        self.screen.blit(self.player_surf, self.rect)
