from ursina import *

class AidKit(Entity):
    def __init__(self, position: tuple):
        super().__init__(
            model="sphere", # placeholder model
            color=color.rgb(255),
            position=position,
            collider="sphere"
        )
        self.health_restore = 30 # amount of health to give to player