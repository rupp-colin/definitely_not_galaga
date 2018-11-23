import arcade

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1200

class EnemyFighter(arcade.Sprite):

    def update(self):
        self.center_y += self.change_y

        if self.top >= SCREEN_HEIGHT - 10:
            self.change_y *= -1

        if self.bottom <= 80:
            self.change_y *= -1

