import arcade
import random

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1200

class Asteroid(arcade.Sprite):

    def update(self):
        self.center_y += 0
        self.center_x += -3

        if self.center_x < 0:
            self.center_x = random.randrange (SCREEN_WIDTH + 20,
                                              SCREEN_WIDTH + 100)
            self.center_y = random.randrange(100, SCREEN_HEIGHT - 20)
