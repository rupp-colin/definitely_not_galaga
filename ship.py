import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600


class StarShip(arcade.Sprite):
    """ This class manages the protagonist Star Ship"""
    # def __init__(self):
    #     # attributes of the class
    #     # Ship Stats
    #     self.armor = 0
    #     self.attack = 1
    #     self.max_hp = 5
    #     self.current_hp = 5
    #     self.movement_speed = 3
    #     self.move_left = False
    #     self.move_right = False
    #     self.move_up = False
    #     self.move_down = False

        # positional attributes
        #     self.position_x = position_x
        #     self.position_y = position_y
        # self.change_x = 0
        # self.change_y = 0

    # class methods
    # def draw_ship(self):
    #     """ Draw the protagonist ship"""
    #     arcade.draw_triangle_filled(self.position_x, self.position_y,
    #                                 self.position_x, self.position_y + 32,
    #                                 self.position_x + 20, self.position_y + 18,
    #                                 arcade.color.BLUE_GREEN)
    #     arcade.draw_point(self.position_x, self.position_y,
    #                       arcade.color.RED, 5)
    #     arcade.draw_point(self.position_x, self.position_y + 16,
    #                       arcade.color.RED, 5)
    #     arcade.draw_point(self.position_x, self.position_y + 32,
    #                       arcade.color.RED, 5)
    #     arcade.draw_line(self.position_x + 2, self.position_y + 8,
    #                      self.position_x + 14, self.position_y + 8,
    #                      arcade.color.WHITE, 1)
    #     arcade.draw_line(self.position_x + 6, self.position_y + 17,
    #                      self.position_x + 19, self.position_y + 17,
    #                      arcade.color.WHITE, 3)
    #     arcade.draw_line(self.position_x + 2, self.position_y + 26,
    #                      self.position_x + 14, self.position_y + 26,
    #                      arcade.color.WHITE, 1)

    arcade.draw_rectangle_outline()


    def update(self):
        """animate the ship"""
        self.center_y += self.change_y
        self.center_x += self.change_x

        if self.center_y > SCREEN_HEIGHT - 50:
            self.center_y = SCREEN_HEIGHT - 50

        if self.center_y < 97:
            self.center_y = 97

        if self.center_x < 25:
            self.center_x = 25

        if self.center_x > SCREEN_WIDTH - 50:
            self.center_x = SCREEN_WIDTH - 50


