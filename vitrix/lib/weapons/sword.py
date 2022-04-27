import os
from ursina import *
from lib.paths import GamePaths

class Sword(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            position = Vec2(0.6, -0.39),
            scale=0.1,
            rotation=Vec3(120, 60, 50),
            model=os.path.join(GamePaths.models_dir, "sword.obj"),
            #texture=os.path.join(GamePaths.textures_dir, "sword.png"),
            color=color.color(0, 0, 0.4),
            on_cooldown=False
        )