import arcade
import random

class Explosion(arcade.Emitter):
    def __init__(self, x, y):
        particle_texture = arcade.make_circle_texture(8, arcade.color.YELLOW)

        super().__init__(
            center_xy=(x, y),
            emit_controller=arcade.EmitBurst(20),   # number of particles
            particle_factory=lambda emitter: arcade.LifetimeParticle(
                filename_or_texture=particle_texture,
                change_xy=(random.uniform(-2, 2), random.uniform(-2, 2)),
                lifetime=random.uniform(0.3, 0.6),
                scale=random.uniform(0.5, 1.2),
                alpha=255,
                change_alpha=-5,
            )
        )
