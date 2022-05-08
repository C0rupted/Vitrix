import os
from vitrix_engine import *

from lib.paths import GamePaths
from lib.entities.crate import Crate


class Wall(Entity):
    base_dir = os.path.join("assets","textures")
    def __init__(self, position):
        super().__init__(
            position=position,
            scale=2,
            model="cube",
            texture=os.path.join(Wall.base_dir, "wall.png"),
            origin_y=-0.5
        )
        
        self.texture.filtering = None
        self.collider = BoxCollider(self, size=Vec3(1, 2, 1))


class Map(Entity):
    def __init__(self):
        super().__init__(
            model=os.path.join(GamePaths.models_dir, "map1.obj"),
            scale=0.3
        )
        self.collider = MeshCollider(self)
        self.crate_one = Crate(position=Vec3(10, 1, -5))