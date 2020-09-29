class Settings:
    """ A class to store  all settings for alien invasion"""

    def __init__(self):
        """ initializes the game's static settings"""
        #screen settings 
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (230,230,230)

        # ship settings
        
        self.ship_limit = 2

        # bullet settings
        
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230,0,230)
        self.bullets_allowed = 30

        # Alien settings
        
        self.fleet_drop_speed = 10

        #how quickly the game speeds up
        self.speedup_scale = 1.1

        # how quickly the alien point values increase
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ initialize settings that change throughout the game """
        self.ship_speed = 1.5
        self.bullet_speed = 5.0
        self.alien_speed = 1.0
        
        #fleet_direction of 1 represents right and -1 represents left 
        self.fleet_direction = 1

        # scoring
        self.alien_points = 10000

    def increase_speed(self):
        """ increases speed settings and alien point values """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)