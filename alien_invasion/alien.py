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
        self.x += self.settings.alien_speed
        self.rect.x = self.x
