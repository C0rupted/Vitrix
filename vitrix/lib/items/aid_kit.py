from ursina import *
from lib.paths import GamePaths
import random

class AidKit(Entity):
    def __init__(self, position: tuple):
        super().__init__(
            model=os.path.join(GamePaths.models_dir, "first_aid_kit.obj"),
            color=color.rgb(255, 0, 0), # red
            position=position,
            collider="sphere",
            scale=0.4,
        )
        self.health_restore = random.randint(27,34) # amount of health to give to player
