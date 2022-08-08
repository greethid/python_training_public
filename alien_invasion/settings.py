class Settings:
    """Class dedicated to keep all game settings"""

    def __init__(self):
        """Initializing game settings"""
        #Display settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200, 180, 220)

        #Ship settings
        self.ship_speed = 0.5