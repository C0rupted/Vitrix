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


# TODO: Hotbar
class Hotbar(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale = (0.5, 0.1),                                           
            origin = (-0.5, 1),                                         
            position = (-0.3,-0.35),                                        
            texture = 'white_cube',                                     
            texture_scale = (5,1),                                      
            color = color.dark_gray  
        )
        self.item_parent = Entity(parent=self, scale=(1/5,1), position_y=10) # parent for items TODO: fix item position

    def find_free_spot(self):                                                      
        taken_spots = [(int(e.x), int(e.y)) for e in self.item_parent.children]    
        for y in range(8):                                                         
            for x in range(5):                                                     
                if not (x,-y) in taken_spots:                                      
                    return (x,-y)