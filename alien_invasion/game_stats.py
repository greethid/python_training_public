class GameStats:
    """Monitoring statistics in the game 'Alien Invasion'"""

    def __init__(self, ai_game):
        """Initialization of statistical data"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Run game 'alien invasion' in inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialization of statistical data which can change during play"""
        self.ship_left = self.settings.ship_limit