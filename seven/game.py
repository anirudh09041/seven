from seven.settings import *
from seven.entities.player import Player
from seven.entities.enemy import Enemy
from seven.entities.bullet import Bullet
import random
import os
import arcade


# Set working directory to project root
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.join(file_path))

class Game(arcade.Window):
    def __init__(self):
        self.score = 0
        self.game_over = False
        self.enemy_speed = 2
        self.backgrounds = []
        self.current_background_index = 0
        self.current_background = None


        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.keys_held = set()

    def setup(self):
        self.player = Player(400, 50)
        self.bullet_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        # Load background textures
        self.backgrounds = [
            arcade.load_texture("assets/images/backgrounds/bg_0.png"),
            arcade.load_texture("assets/images/backgrounds/bg_1.png"),
        ]


        self.current_background = self.backgrounds[0]

        self.sound_shoot = arcade.load_sound("assets/sounds/shoot.wav")
        # self.sound_enemy_die = arcade.load_sound("assets/sounds/enemy_die.wav")
        # self.sound_player_hit = arcade.load_sound("assets/sounds/player_hit.wav")
        self.sound_game_over = arcade.load_sound("assets/sounds/game_over.wav")

        self.background_music = arcade.load_sound("assets/sounds/music.mp3")
        self.music_player = arcade.play_sound(self.background_music, looping=True)



    def on_draw(self):
        arcade.start_render()



        arcade.draw_lrwh_rectangle_textured(
            0, 0,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            self.current_background
        )

        # ---- Improved Health Bar ----
        bar_width = 100
        bar_height = 8
        bar_x = 50
        bar_y = 570

        # Background bar (dark red)
        arcade.draw_rectangle_filled(bar_x, bar_y, bar_width, bar_height, arcade.color.DARK_RED)

        # Foreground (green)
        current_health_width = bar_width * (self.player.hp / self.player.max_hp)
        arcade.draw_rectangle_filled(
            bar_x - (bar_width - current_health_width) / 2,
            bar_y,
            current_health_width,
            bar_height,
            arcade.color.LIGHT_GREEN
        )

        # Health text
        arcade.draw_text(
            f"{self.player.hp}/{self.player.max_hp}",
            bar_x + bar_width + 10,
            bar_y - 7,
            arcade.color.WHITE,
            12
        )

        # ---- Score ----
        arcade.draw_text(
            f"Score: {self.score}",
            5, 540,
            arcade.color.WHITE,
            20,
            bold=True
        )

        # ---- Sprites ----
        self.player.draw()
        self.bullet_list.draw()
        self.enemy_list.draw()


        #------Game Over -----
        if self.game_over:
            arcade.draw_text(
                "GAME OVER",
                300, 320,
                arcade.color.RED,
                40,
                bold=True
            )

            arcade.draw_text(
                f"Final Score: {self.score}",
                320, 260,
                arcade.color.WHITE,
                20
            )

            arcade.draw_text(
                "Press R to Restart",
                320, 220,
                arcade.color.LIGHT_GRAY,
                18
            )

    def on_key_press(self, key, _):
        self.keys_held.add(key)

        if key == arcade.key.SPACE:
            bullet = Bullet(self.player.center_x, self.player.center_y + 20)
            self.bullet_list.append(bullet)
            arcade.play_sound(self.sound_shoot)

        if key == arcade.key.R and self.game_over:
            self.setup()  # Reset everything
            self.game_over = False
            return

    def on_key_release(self, key, _):
        if key in self.keys_held:
            self.keys_held.remove(key)

    def on_update(self, delta_time):

        if self.game_over:
            return

        dx = 0
        dy = 0

        if arcade.key.W in self.keys_held:
            dy = 1
        if arcade.key.S in self.keys_held:
            dy = -1
        if arcade.key.A in self.keys_held:
            dx = -1
        if arcade.key.D in self.keys_held:
            dx = 1

        self.player.move(dx, dy)
        self.player.update()
        self.bullet_list.update()
        self.enemy_list.update()



        # Spawn enemies
        if random.random() < 0.009:
            self.enemy_list.append(Enemy(self.enemy_speed))

        # Collision: bullet hits enemy
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)
            for enemy in hit_list:
                enemy.kill()
                bullet.kill()
                self.score += 10

        # Increase enemy speed every 100 points
        self.enemy_speed = 2 + (self.score // 100)

        # Change background after every 100 score
        new_index = (self.score // 100) % len(self.backgrounds)

        if new_index != self.current_background_index:
            self.current_background_index = new_index
            self.current_background = self.backgrounds[new_index]

        # Enemy hits player
        player_hits = arcade.check_for_collision_with_list(self.player, self.enemy_list)
        for enemy in player_hits:
            enemy.kill()
            self.player.hp -= 20
            if self.player.hp <= 0:
                self.player.hp = 0
                self.game_over = True

                if self.music_player:
                    self.music_player.pause()

                arcade.play_sound(self.sound_game_over)




