import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set the starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load the alien and set its rect position
        self.original_image = pygame.image.load('images/alien.bmp').convert_alpha()
        self.scale_factor = 2  # Set your desired scaling factor
        self.image = pygame.transform.scale(self.original_image,
                                            (self.original_image.get_width() * self.scale_factor,
                                             self.original_image.get_height() * self.scale_factor))
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)
    def check_edges(self):
        """Return true if the alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <=0:
            return True
    def update(self):
        """Moves the alien to the right"""
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x