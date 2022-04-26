from ursina import *

class Axe(Entity):
    def __init__(self):
        super().__init__(
            model = "assets/models/axe.obj"
        )