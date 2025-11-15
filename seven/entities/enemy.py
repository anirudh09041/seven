import arcade
import random


class Enemy(arcade.Sprite):
    def __init__(self, speed):
        super().__init__("assets/images/enemy.png", 0.1)
        self.center_x = random.randint(20, 780)
        self.center_y = 620
        self.change_y = -speed
    def update(self):
        self.center_y += self.change_y
        if self.center_y < -20:
            self.kill()
