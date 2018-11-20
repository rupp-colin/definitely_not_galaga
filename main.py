# imports go here
import arcade
import ship

# define screen size
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


class ShittyGalaga(arcade.Window):
    def __init__(self, width, height, title):

        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

        self.player = ship.StarShip(25, 300, 0, 0)

    def on_draw(self):
        """Called whenever the window needs to be re-drawn"""
        arcade.start_render()
        # draw player1
        self.player.draw_ship()
        # draw menu line
        arcade.draw_line(0, 70, 1200, 70, arcade.color.WHITE_SMOKE, 5)
        # Display level in menu
        arcade.draw_text("Level 1", 500, 24, arcade.color.WHITE_SMOKE, 24)
        # Extra Lives TODO write a function to display
        # correct number of lives and at the appropriate place
        # ship.StarShip.draw_ship(self, 25, 20)
        # ship.StarShip.draw_ship(self, 65, 20)
        # ship.StarShip.draw_ship(self, 105, 20)

    def update(self, delta_time):
        self.player.update()

    def on_key_press(self, key, modifiers):
        """Called whenever the user presses a key"""
        if key == arcade.key.RIGHT:
            self.player.change_x = self.player.movement_speed

        if key == arcade.key.LEFT:
            self.player.change_x = -self.player.movement_speed

        if key == arcade.key.UP:
            self.player.change_y = self.player.movement_speed

        if key == arcade.key.DOWN:
            self.player.change_y = -self.player.movement_speed

    def on_key_release(self, key, modifiers):
        """called when a user releases a key"""
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0


def main():
    window = ShittyGalaga(SCREEN_WIDTH, SCREEN_HEIGHT, "Shitty Galaga")
    arcade.run()


main()
