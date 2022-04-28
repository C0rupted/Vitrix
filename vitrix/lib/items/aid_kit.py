from ursina import *
from lib.paths import GamePaths
import random

class AidKit(Entity):
    def __init__(self, position: tuple):
        super().__init__(
            model=os.path.join(GamePaths.models_dir, "first_aid_kit.obj"),
            color=color.rgb(255),
            position=position,
            collider="sphere"
        )
        self.health_restore = random.randint(25,35) # amount of health to give to player