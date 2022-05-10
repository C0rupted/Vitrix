import os
from vitrix_engine import *
from lib.paths import GamePaths


class FloorCube(Entity):
    def __init__(self, position):
        super().__init__(
            position=position,
            scale=2,
            model=os.path.join(GamePaths.models_dir, "cube.obj"),
            texture=os.path.join(GamePaths.textures_dir, "floor.png"),
            collider="box"
        )



class Floor:
    def __init__(self):
        dark1 = True
        for z in range(-28, 30, 2):
            dark2 = not dark1

            for x in range(-18, 28, 2):
                cube = FloorCube(Vec3(x, 0, z))

                if dark2:
                    cube.color = color.color(0, 0.2, 0.8)
                else:
                    cube.color = color.color(0, 0.2, 1)
                
                dark2 = not dark2
            
            dark1 = not dark1
