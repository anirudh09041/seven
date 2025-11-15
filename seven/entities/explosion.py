import arcade
import random


class Explosion(arcade.Emitter):
    def __init__(self, x, y):

        # Create a pixel-circle texture
        particle_texture = arcade.make_circle_texture(8, arcade.color.YELLOW)

        super().__init__(
            center_xy=(x, y),

            # Emit 20 particles instantly
            emit_controller=arcade.EmitBurst(20),

            # New Arcade 3.x particle API
            particle_factory=lambda emitter: arcade.FadeParticle(
                filename_or_texture=particle_texture,
                change_xy=(random.uniform(-3, 3), random.uniform(-3, 3)),
                lifetime=random.uniform(0.3, 0.6),
                scale=random.uniform(0.5, 1.2),
            )
        )
