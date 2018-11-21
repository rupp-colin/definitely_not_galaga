import arcade


ASTEROID_EXPLOSION_TEXTURES = 51

class Explosion(arcade.Sprite):
    """this class is responsible for creating explosion animations"""

    explosion_textures = []

    def __init__(self):
        super().__init__("images/asteroid_explosion/explosion0000.png")
        self.current_texture = 0
        self.texture = self.textures[self.current_texture]

    def update(self):
        self.current_texture += 1
        if self.current_texture < ASTEROID_EXPLOSION_TEXTURES:
            texture_name = f"images/asteroid_explosion/explosion{self.current_texture:0>4}.png"
            self.texture = arcade.load_texture(texture_name)
        else:
            self.kill()
