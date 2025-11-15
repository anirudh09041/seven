import arcade
from seven.settings import PLAYER_SPEED

class Player(arcade.Sprite):
    def __init__(self, x, y):
        # Use forward slashes and make the path absolute relative to project
        super().__init__("assets/images/player.png", 0.1)
        self.center_x = x
        self.center_y = y
        self.max_hp = 100
        self.hp = 100

    def move(self, dx, dy):
        self.change_x = dx * PLAYER_SPEED
        self.change_y = dy * PLAYER_SPEED

    def update(self):
        super().update()
        self.center_x = max(20, min(self.center_x, 780))
        self.center_y = max(20, min(self.center_y, 580))
