import os
from ursina import *
from lib.paths import GamePaths

class Hammer(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            position = Vec2(0.19, -0.39),
            scale=0.1,
            rotation=Vec3(-20, -20, -5),
            model=os.path.join(GamePaths.models_dir, "hammer.obj"),
            texture=os.path.join(GamePaths.textures_dir, "hammer.png"),
            color=color.color(0, 0, 0.4),
            on_cooldown=False
        )