import arcade


class Lazer():
    def __init__(self, x, y, color, width, facing):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.facing = facing
        self.velocity = 7 * facing

    def draw():
        arcade.draw_line(self, self.x, self.y,
                         self.x + 6, self.y,
                         self.color, self.width)
