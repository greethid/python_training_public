class Settings:
    """Class dedicated to keep all game settings"""

    def __init__(self):
        """Initializing game settings"""
        # Display settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200, 180, 220)

        # Ship settings
        # self.ship_speed = 2.0  -> moved to initialize_dynamic_settings()
        self.ship_limit = 3

        # Bullet settings
        # self.bullet_speed = 3  -> moved to initialize_dynamic_settings()
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (160, 60, 60)
        self.bullet_allowed = 5

        # Alien settings
        # self.alien_speed = 0.5 -> moved to initialize_dynamic_settings()
        self.fleet_drop_speed = 20
        # Fleet direction equals 1 means right, -1 means left
        self.fleet_direction = 1

        # Star settings
        self.star_speed = 1

        # Easy change of the game speed
        self.speedup_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialization the settings which will be changed during a game"""
        self.ship_speed = 2.0
        self.bullet_speed = 3
        self.alien_speed = 0.5

    def increase_speed(self):
        """Change game speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale