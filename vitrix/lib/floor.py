import os
import ursina


class FloorCube(ursina.Entity):
    base_dir = os.path.join("assets","textures")
    def __init__(self, position):
        super().__init__(
            position=position,
            scale=2,
            model="cube",
            texture=os.path.join(FloorCube.base_dir, "floor.png"),
            collider="box"
        )

        self.texture.filtering = None


class Floor:
    def __init__(self):
        dark1 = True
        for z in range(-28, 30, 2):
            dark2 = not dark1

            for x in range(-18, 28, 2):
                cube = FloorCube(ursina.Vec3(x, 0, z))

                if dark2:
                    cube.color = ursina.color.color(0, 0.2, 0.8)
                else:
                    cube.color = ursina.color.color(0, 0.2, 1)
                
                dark2 = not dark2
            
            dark1 = not dark1
