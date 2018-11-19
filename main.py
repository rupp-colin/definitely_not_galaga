# imports go here
import arcade
import ship

# define screen size
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600


def on_draw(delta_time):
    arcade.start_render()

    # make the ship move
    ship.draw_ship(25, on_draw.ship_y)
    # make ship move upwards
    on_draw.ship_y += on_draw.delta_y * delta_time
    # make ship reverse direction after hitting top boundary
    if on_draw.ship_y > SCREEN_HEIGHT - 50 or on_draw.ship_y < 90:
        on_draw.delta_y *= -1

    # draw menu line
    arcade.draw_line(0, 70, 1200, 70, arcade.color.WHITE_SMOKE, 5)

    # Display level in menu
    arcade.draw_text("Level 1", 500, 24, arcade.color.WHITE_SMOKE, 24)

    # Display score in menu

    # Extra Lives TODO write a function to display
    # correct number of lives and at the appropriate place
    ship.draw_ship(25, 20)
    ship.draw_ship(65, 20)
    ship.draw_ship(105, 20)


on_draw.ship_y = 100
on_draw.delta_y = 130


def main():
    # initialize window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "shitty galaga")
    arcade.set_background_color(arcade.color.BLACK)

    # Call on_draw every 80th of a second
    arcade.schedule(on_draw, 1/80)
    arcade.run()


main()
