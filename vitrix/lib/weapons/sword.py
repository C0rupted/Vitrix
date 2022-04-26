import os
from ursina import *
from lib.paths import GamePaths

class Sword(Entity):
    def __init__(self):
        super().__init__(
            model = os.path.join(GamePaths.models_dir, "sword.obj")
        )