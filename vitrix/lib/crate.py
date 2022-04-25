import os
import ursina
import random


class Crate(ursina.Entity):
    base_dir = os.path.join("assets","textures")

    def __init__(self, position):
        super().__init__(
            position=position,
            scale=1.5,
            origin_y=-0.5,
            model="cube",
            texture=os.path.join(Crate.base_dir, "crate.png"),
        )
        
        items_list = ["gun", "bandages", "first_aid_kit", "bandages", "bandages"]

        self.contents = []
        self.is_crate = True
        self.texture.filtering = None
        self.collider = ursina.BoxCollider(self, size=ursina.Vec3(1, 2, 1))
        for i in range (1, random.randint(2, 4)):
            self.contents.append(random.choice(items_list))

        

