import pygame

class Ship:
    """Class dedicated to managing the spacecraft"""

    def __init__(self, ai_game):
        """Spacecraft initialization and its initial position"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Loading image of the spacecraft and downloading its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Every new spacecraft appears on the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Displaying the spacecraft at its current position"""
        self.screen.blit(self.image, self.rect)