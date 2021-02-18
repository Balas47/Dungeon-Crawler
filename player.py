import pygame

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

# Colors for indicating the directions that the player is facing
UP = COLORS[VIOLET]
DOWN = COLORS[GREEN]
LEFT = COLORS[BLUE]
RIGHT = COLORS[RED]

HITF = -1

# The player class controls the position of the player on the screen, as
# well as how the different inputs effect what happens for the player.
class Player(pygame.sprite.Sprite):

    def __init__(self, screen):

        # Necessary for making the player a Sprite
        super(Player, self).__init__()

        # The player will keep track of the dimensions of the player "model"
        # and the screen the player is going to be drawn on
        self.screen = screen
        self.width = 10
        self.height = 10

        # Initial position and speed of the player
        self.x, self.y = 0, 0
        self.x_speed, self.y_speed = .5, .5
        self.facing = UP

        # Keep track of the player surface and rectangle
        self.player_surf = pygame.Surface((self.width, self.height))
        self.player_surf.fill(self.facing)
        self.rect = self.player_surf.get_rect()


    def move(self, buttons, obstacles):
        """
        This function will take care of the movement of the player
        :param buttons: The buttons the user pressed to determine direction
                       of the player movement
        """

        # Get the index of a colliding rect
        hit = self.rect.collidelist(obstacles)

        # Check the players collisions in the x and y directions considering precedence of rects in to the left, and to the top of the at hit
        checkx = obstacles[hit].left < self.x + 1 < obstacles[hit].right or obstacles[hit].left < self.x + self.width - 1 < obstacles[hit].right
        checkl = obstacles[(hit + 1) % len(obstacles)].left < self.x + 1 < obstacles[(hit + 1) % len(obstacles)].right or obstacles[(hit + 1) % len(obstacles)].left < self.x + self.width - 1 < obstacles[(hit + 1) % len(obstacles)].right
        checky = obstacles[hit].top < self.y + 1 < obstacles[hit].bottom or obstacles[hit].top < self.y + self.height - 1 < obstacles[hit].bottom
        checkb = False

        # Find the rect directly below the one being collided with
        for i in range(hit + 1, len(obstacles)):
            if obstacles[i].left == obstacles[hit].left:
                checkb = obstacles[i].top < self.y + 1 < obstacles[i].bottom or obstacles[i].top < self.y + self.height - 1 < obstacles[i].bottom
                break

        # Take care of the actual movement of the player
        if buttons[pygame.K_w]:
            self.y -= self.y_speed

            # Undo the movement if necessary (if the player would be within the wall)
            if hit > HITF and obstacles[hit].top <= self.y <= obstacles[hit].bottom:
                if checkx or checkl:
                    self.y += self.y_speed

            self.facing = UP

        if buttons[pygame.K_a]:
            self.x -= self.x_speed

            if hit > HITF and obstacles[hit].left <= self.x <= obstacles[hit].right:
                if checky or checkb:
                    self.x += self.x_speed

            self.facing = LEFT

        if buttons[pygame.K_s]:
            self.y += self.y_speed

            if hit > HITF and obstacles[hit].top <= self.y + self.height <= obstacles[hit].bottom:
                if checkx or checkl:
                    self.y -= self.y_speed

            self.facing = DOWN

        if buttons[pygame.K_d]:
            self.x += self.x_speed

            if hit > HITF and obstacles[hit].left <= self.x + self.width <= obstacles[hit].right:
                if checky or checkb:
                    self.x -= self.x_speed

            self.facing = RIGHT

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


    def reset(self):
        """
        This function will reset the location of the player
        :return: None
        """
        self.x = 0
        self.y = 0
        self.rect.left = self.x
        self.rect.top = self.y


    def draw(self, dim_x, dim_y):
        """
        This function will take care of actually drawing the player onto the
        game screen.
        :param dim_x: The x dimension of the screen.
        :param dim_y: The y dimension of the screen.
        """

        # Update the position, and color of the player on the screen
        #self.screen.blit(self.player_surf, (self.x, self.y)
        self.player_surf.fill(self.facing)
        self.screen.blit(self.player_surf, self.rect)
