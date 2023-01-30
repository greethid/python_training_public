import pygame.font


class Scoreboard:
    """Class dedicated to creating scoreboards"""

    def __init__(self, ai_game):
        """Initialization of scoring attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Setting font for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare init scoring images
        self.prep_score()

