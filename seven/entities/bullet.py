import arcade
from seven.settings import BULLET_SPEED

class Bullet(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("assets/images/bullet.png", 0.01)
        self.center_x = x
        self.center_y = y
        self.change_y = BULLET_SPEED

    def update(self):
        self.center_y += self.change_y
        if self.center_y > 620:
            self.kill()
