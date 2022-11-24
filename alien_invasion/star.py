import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """Class representing a single star in the background"""

    def __init__(self, ai_game):
        """Star initialization and defining its location"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the star image and define its attribute rect
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        # Placing a new star near the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storing the exact horizontal foreign position
        self.x = float(self.rect.x)

        # Storing the exact vertical foreign position
        self.y = float(self.rect.y)

    def update(self):
        """Moving a star to the down"""
        self.y += self.settings.star_speed
        self.rect.y = self.y