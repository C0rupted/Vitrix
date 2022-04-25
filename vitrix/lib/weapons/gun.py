from ursina import *

class Gun(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            position=Vec2(0.6, -0.45),
            scale=Vec3(0.1, 0.2, 0.65),
            rotation=Vec3(-20, -20, -5),
            model="cube",
            texture="white_cube",
            color=color.color(0, 0, 0.4),
            on_cooldown=False
        )