from ursina import *

class Inventory(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale = (.5, .8),                                           
            origin = (-.5, .5),                                         
            position = (-.3,.4),                                        
            texture = 'white_cube',                                     
            texture_scale = (5,8),                                      
            color = color.dark_gray  
        )
        self.item_parent = Entity(parent=self, scale=(1/5,1/8)) # parent for items

    def append(self, item):                                             
        Button(                                                         
            parent = self.item_parent,                             
            model = 'quad',                                             
            origin = (-.5,.5),                                          
            color = color.random_color(),                               
            z = -.1                                                     
            )
        item.parent = self.item_parent