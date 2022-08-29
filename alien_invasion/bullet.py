import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class dedicated to managing the bullets shot by the ship"""

    def __init__(self, ai_game):
        """Create a bullet object in actual ship's position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create rectangular bullet at point (0, 0) and then define for it current position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Bullet's position is defined by floating point value
        self.y = float(self.rect.y)

    def update(self):
        """Moving the bullet on the screen"""
        # Updating bullet's position
        self.y -= self.settings.bullet_speed
        # Updating rectangle's position of the bullet
        self.rect.y = self.y

    def draw_bullet(self):
        """Displaying the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

