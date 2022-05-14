from vitrix_engine import *
from lib.paths import GamePaths
import random

class Ammo(Entity):
    def __init__(self, position: tuple):
        super().__init__(
            model=os.path.join(GamePaths.models_dir, "ammo.obj"),
            texture=os.path.join(GamePaths.textures_dir, "ammo.png"),
            position=position,
            scale=0.4,
        )

        self.is_crate = False
        self.is_aid_kit = False
        self.is_ammo = True
        self.collider = MeshCollider(self)
