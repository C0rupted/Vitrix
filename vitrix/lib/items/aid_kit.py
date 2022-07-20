from vitrix_engine import *
from lib.data import GamePaths

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
