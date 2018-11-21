# imports go here
import arcade
import random
import ship
import asteroid as space_rock

# define screen size
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
ASTEROID_COUNT = 30

# attributes for ship
movement_speed = 3

class ShittyGalaga(arcade.Window):
    def __init__(self, width, height, title):

        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

        # self.player = ship.StarShip(25, 300, 0, 0)
        self.player_list = None
        self.bullet_list = None
        self.asteroid_list = None
        self.score = 0

    def setup(self):
        """set up the game"""

        # Set up player ship
        self.bullet_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = ship.StarShip("star_ship.gif", 0.5)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 300
        self.player_sprite.angle = 270
        self.player_list.append(self.player_sprite)
        # make some asteroids for now
        for i in range(ASTEROID_COUNT):
            asteroid = space_rock.Asteroid("asteroid01.png", 0.3)
            asteroid.center_x = random.randrange(200, SCREEN_WIDTH)
            asteroid.center_y = random.randrange(100, SCREEN_HEIGHT - 20)
            self.asteroid_list.append(asteroid)


    def on_draw(self):
        """Called whenever the window needs to be re-drawn"""

        arcade.start_render()

        #self.player.draw_ship()
        self.player_list.draw()
        self.asteroid_list.draw()
        self.bullet_list.draw()
        # draw menu line
        arcade.draw_line(0, 70, 1200, 70, arcade.color.WHITE_SMOKE, 5)
        # Display level in menu
        arcade.draw_text("Level 1", 500, 24, arcade.color.WHITE_SMOKE, 24)
        arcade.draw_text(f"Score: {self.score}", 1050, 30, arcade.color.WHITE_SMOKE, 16)

    def on_key_press(self, key, modifiers):
        """Called whenever the user presses a key"""
        if key == arcade.key.SPACE:
            bullet = arcade.Sprite("laserBlue01.png", 0.7)
            bullet.center_x = self.player_sprite.center_x + 12
            bullet.center_y = self.player_sprite.center_y
            bullet.change_x = 5
            self.bullet_list.append(bullet)

        if key == arcade.key.RIGHT:
            self.player_sprite.change_x += movement_speed

        if key == arcade.key.LEFT:
            self.player_sprite.change_x -= movement_speed

        if key == arcade.key.UP:
            self.player_sprite.change_y += movement_speed

        if key == arcade.key.DOWN:
            self.player_sprite.change_y -= movement_speed

    def on_key_release(self, key, modifiers):
        """called when a user releases a key"""
        if key == arcade.key.LEFT:
            self.player_sprite.change_x += movement_speed

        if key == arcade.key.RIGHT:
            self.player_sprite.change_x -= movement_speed

        if key == arcade.key.UP:
            self.player_sprite.change_y -= movement_speed

        if key == arcade.key.DOWN:
            self.player_sprite.change_y += movement_speed

    def update(self, delta_time):
        self.player_sprite.update()
        self.asteroid_list.update()
        self.bullet_list.update()

        # player_got_hit = arcade.check_for_collision_with_list(self.player_sprite, self.asteroid_list)
        # if len(player_got_hit) > 0:
        #     player_sprite.kill()
        #     asteroid.kill()

        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.asteroid_list)
            if len(hit_list) > 0:
                bullet.kill()

            for asteroid in hit_list:
                asteroid.center_x = random.randrange(SCREEN_WIDTH + 20,
                                                     SCREEN_WIDTH + 100)
                asteroid.center_y = random.randrange(100,
                                                     SCREEN_HEIGHT - 20)
                self.score += 1

            if bullet.left > SCREEN_WIDTH:
                bullet.kill()


def main():
    window = ShittyGalaga(SCREEN_WIDTH, SCREEN_HEIGHT, "Shitty Galaga")
    window.setup()
    arcade.run()


main()
