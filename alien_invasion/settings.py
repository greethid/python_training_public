class Settings:
    """Class dedicated to keep all game settings"""

    def __init__(self):
        """Initializing game settings"""
        # Display settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200, 180, 220)

        # Ship settings
        self.ship_speed = 1.0

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)