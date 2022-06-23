from vitrix_engine import *
from vitrix.lib.data import GamePaths
import random

class AidKit(Entity):
    def __init__(self, position: tuple):
        super().__init__(
            model=os.path.join(GamePaths.models_dir, "first_aid_kit.obj"),
            color=color.rgb(255, 0, 0), # red
            position=position,
            collider="sphere",
            scale=.4,
        )

        self.collider = MeshCollider(self)
        self.health_restore = random.randint(50, 80) # amount of health to give to player
