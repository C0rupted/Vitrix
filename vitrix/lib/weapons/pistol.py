from ursina import *

class Pistol(Entity):
    def __init__(self):
        super().__init__(
            model = "assets/models/pistol.obj"
        )