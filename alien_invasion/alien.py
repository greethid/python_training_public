import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class representing a single alien in fleet"""

    def __init__(self, ai_game):
        """Alien initialization and defining its location"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and define its attribute rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Placing a new alien near the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storing the exact horizontal foreign position
        self.x = float(self.rect.x)

    def update(self):
        """Moving an alien to the right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges_right_left(self):
        """Returns True if alien touches the right or the left edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

