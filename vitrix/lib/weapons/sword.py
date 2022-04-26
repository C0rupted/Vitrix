from ursina import *

class Sword(entity):
    def __init__(self):
        super().__init__(
            model = "assets/models/sword.obj"
        )