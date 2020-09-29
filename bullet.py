import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class to manage bullets fired from ship """
    def __init__(self, ai_game):
        """ create bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a bullect rect at (0,0) and set correct position.
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect1 = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)

        self.rect.midtop = ai_game.ship.rect.midleft
        self.rect1.midtop = ai_game.ship.rect.midright

        # store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        self.y1 = float(self.rect1.y)

    def update(self):
        """ move the bullet up the screen """
        # update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        self.y1 -= self.settings.bullet_speed
        # update the rect position
        self.rect.y = self.y 
        self.rect1.y = self.y1 

    def draw_bullet(self):
        """ draw the bullet to the screen """
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect1)