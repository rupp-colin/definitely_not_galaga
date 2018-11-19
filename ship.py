import arcade


def draw_ship(x, y):
    """ Draw the protagonist ship"""

    arcade.draw_triangle_filled(x, y, x, y + 32, x + 20, y + 18,
                                arcade.color.BLUE_GREEN)
    arcade.draw_point(x, y, arcade.color.RED, 5)
    arcade.draw_point(x, y + 32, arcade.color.RED, 5)
    arcade.draw_point(x, y + 16, arcade.color.RED, 5)
