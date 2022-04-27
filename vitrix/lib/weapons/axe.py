import os
from ursina import *
from lib.paths import GamePaths

class Axe(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            position = Vec2(0.8, -0.3),
            scale=0.1,
            rotation=Vec3(-20, -20, -10),
            model=os.path.join(GamePaths.models_dir, "axe.obj"),
            #texture=os.path.join(GamePaths.textures_dir, "axe.png"),
            color=color.color(0, 0, 0.4),
            on_cooldown=False
        )