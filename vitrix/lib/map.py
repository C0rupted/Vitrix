import os
import ursina

from lib.paths import GamePaths
from lib.crate import Crate


class Wall(ursina.Entity):
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
        self.collider = ursina.BoxCollider(self, size=ursina.Vec3(1, 2, 1))


class Map(ursina.Entity):
    def __init__(self):
        super().__init__(
            model=os.path.join(GamePaths.models_dir, "map1.obj"),
            scale=0.2
        )
        self.collider = ursina.MeshCollider(self)
        self.crate_one = Crate(position=ursina.Vec3(10, 1, -5))