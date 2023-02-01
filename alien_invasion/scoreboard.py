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

    def prep_score(self):
        """Transform scores to image on the screen"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display scoring in the upper right corner of the screen
        self.score_rect = self.score_image

