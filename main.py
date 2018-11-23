# imports go here
import arcade
import random
import ship
import enemy_fighter
import asteroid as space_rock
import explosions as boom

# define screen size
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
ASTEROID_COUNT = 30
ASTEROID_EXPLOSION_TEXTURES = 51

# GAME STATES
TITLE_PAGE = 0
LEVEL_ONE = 1
GAME_OVER = 2


# attributes for ship
movement_speed = 3

class ShittyGalaga(arcade.Window):
    def __init__(self, width, height, title):

        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

        self.current_state = TITLE_PAGE

        self.frame_count = 0

        self.player_list = None
        self.bullet_list = None
        self.enemyBullet_list = None
        self.asteroid_list = None
        self.explosion_list = None
        self.enemy_list = None

        self.player_sprite = None
        self.score = 0

        self.instructions = []
        # load each background image for different screens
        texture = arcade.load_texture("images/game_background.png")
        self.instructions.append(texture)
        # same texture for both instructions and level one, so append
        # the same texture again
        self.instructions.append(texture)


    def setup(self):
        """set up the game"""

        # set up enemies for level
        self.enemy_list = arcade.SpriteList()
        enemy = enemy_fighter.EnemyFighter("images/enemy_ship01.png", )
        enemy.center_x = 1150
        enemy.center_y = 300
        enemy.change_y = 3
        enemy.angle = 90
        self.enemy_list.append(enemy)

        self.enemyBullet_list = arcade.SpriteList()

        # Set up player ship
        self.bullet_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.explosion_list = arcade.SpriteList()

        # preloading animation frames for explosions
        explosion_texture_list = []
        for i in range(ASTEROID_EXPLOSION_TEXTURES):
            texture_name = f"images/asteroid_explosion/explosion{i:0>d}.png"
            explosion_texture_list.append(texture_name)

        #self.explosion_list.preload_textures(explosion_texture_list)

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


    def draw_instructions_page(self, page_number):
        """ draws a game state page"""
        page_texture = self.instructions[page_number]
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      page_texture.width, page_texture.height,
                                      page_texture, 0)
        arcade.draw_text("Definitely Not Galaga", 230, 330, arcade.color.CYBER_YELLOW, 54)
        arcade.draw_text("press any key to restart", 370, 250, arcade.color.WHITE_SMOKE, 24)


    def draw_game_over(self):
        """Draws "GAME OVER" across the screen"""
        arcade.draw_text("GAME OVER", 400, 300, arcade.color.WHITE, 54)
        arcade.draw_text("press any key to restart", 350, 250, arcade.color.WHITE_SMOKE, 24)

    def draw_game(self):
        """draws the necessary things for the game"""
        page_texture = self.instructions[0]
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      page_texture.width, page_texture.height,
                                      page_texture, 0)
        #self.player.draw_ship()
        self.player_list.draw()
        self.asteroid_list.draw()
        self.bullet_list.draw()
        self.explosion_list.draw()
        self.enemy_list.draw()
        self.enemyBullet_list.draw()

        # draw menu line
        # arcade.draw_line(0, 70, 1200, 70, arcade.color.SMOKY_BLACK, 5)
        # Display level in menu
        arcade.draw_text("Level 1", 500, 24, arcade.color.SMOKY_BLACK, 24)
        arcade.draw_text(f"Score: {self.score}", 1050, 30, arcade.color.SMOKY_BLACK, 16)


    def on_draw(self):
        """Called whenever the window needs to be re-drawn"""

        arcade.start_render()
        if self.current_state == TITLE_PAGE:
            self.draw_instructions_page(0)
        elif self.current_state == LEVEL_ONE:
            self.draw_game()
        else:
            self.draw_game()
            self.draw_game_over()

    # USER CONTROLS SECTION
    def on_key_press(self, key, modifiers):
        """Called whenever the user presses a key"""
        if self.current_state == TITLE_PAGE:
            self.setup()
            self.current_state = LEVEL_ONE
        elif self.current_state == GAME_OVER:
            self.current_state = TITLE_PAGE


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

    # events updater
    def update(self, delta_time):
        if self.current_state == LEVEL_ONE:
            self.player_sprite.update()
            self.asteroid_list.update()
            self.bullet_list.update()
            self.explosion_list.update()
            self.enemy_list.update()

            self.frame_count += 1

            for enemy in self.enemy_list:
                if self.frame_count % 120 == 0:
                    bullet = arcade.Sprite("fireBall.png", 0.3)
                    bullet.center_x = enemy.center_x
                    bullet.center_y = enemy.center_y
                    bullet.change_x = -3
                    self.enemyBullet_list.append(bullet)

            for bullet in self.enemyBullet_list:
                if bullet.right < 0:
                    bullet.kill()

            self.enemyBullet_list.update()

            ################# WHEN THE PLAYER DIES ########################
            for player in self.player_list:
                player_got_hit = arcade.check_for_collision_with_list(self.player_sprite, self.asteroid_list)
                if len(player_got_hit) > 0:
                    explosion = boom.Explosion()
                    explosion.center_x = player_got_hit[0].center_x
                    explosion.center_y = player_got_hit[0].center_y
                    self.explosion_list.append(explosion)
                    player.kill()
                    self.current_state = GAME_OVER

            for bullet in self.bullet_list:
                hit_list = arcade.check_for_collision_with_list(bullet, self.asteroid_list)
                if len(hit_list) > 0:
                    explosion = boom.Explosion()
                    explosion.center_x = hit_list[0].center_x
                    explosion.center_y = hit_list[0].center_y
                    self.explosion_list.append(explosion)
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
