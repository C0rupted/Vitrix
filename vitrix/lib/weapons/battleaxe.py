import os
from ursina import *
from lib.paths import GamePaths

class BattleAxe(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            position = Vec2(0.7, -0.3),
            scale=0.05,
            rotation=Vec3(-20, -20, -10),
            model=os.path.join(GamePaths.models_dir, "battleaxe.obj"),
            #texture=os.path.join(GamePaths.textures_dir, "axe.png"),
            color=color.color(0, 0, 0.4),
            on_cooldown=False
        )