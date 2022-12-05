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

        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (160, 60, 60)
        self.bullet_allowed = 3

        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        # Fleet direction equals 1 means right, -1 means left
        self.fleet_direction = 1

        # Star settings
        self.star_speed = 1

