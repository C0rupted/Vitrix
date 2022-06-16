from vitrix_engine import *
from lib.paths import GamePaths
from vitrix_engine.prefabs.first_person_controller import FirstPersonController


class HealthBar(Entity):
    def __init__(self, max_value):
        cube = os.path.join(GamePaths.models_dir, "cube.obj")
        super().__init__(
            parent = camera.ui,
            position = Vec2(-.20, -.43),
            scale = Vec2(.4175, .125),
            rotation=Vec3(0, 0, 180),
            model = cube,
        )

        self.set_ranged()

        self.texture = os.path.join(GamePaths.textures_dir, "Inventory",
                                    str)(i) +".png"

# self.icon = Entity(parent=camera.ui, model=cube, position=Vec2(-.20, -.0),
#                    texture=os.path.join(GamePaths.textures_dir, ""),
#                    scale=0.1, shader=None)

# self.shader = None
# self.max_value = max_value
# self.value = self.max_value
# self.segments = 15
# self.value_per_segment = self.max_value / self.segments

# x = 0
# i = 0
# while x < self.value:
#     x += self.value_per_segment
#     i += 1
# self.texture = os.path.join(GamePaths.textures_dir, "Inventory",
#                             str(i) +".png")

# code not ready

# def inventory_close():
#     Inventory().inventory_ui.enable = False

# def inventory_enable():

#     inventory = Inventory()
#     Inventory().enable = False
#     def add_item():
#         Inventory().append(random.choice(('hammer', 'axe', 'gem', 'pistol', 'sword')))

#     for i in range(7):
#         add_item()

#     add_item_button = Button(
#         scale = (.1,.1),
#         x = -.5,
#         color = color.lime.tint(-.25),
#         text = '+',
#         tooltip = Tooltip('Add random item'),
#         on_click = add_item
#     )

# # Drag and drop functions, not ready yet
# def find_free_spot(self):
#     taken_spots = [(int(e.x), int(e.y)) for e in self.item_parent.children]
#     for y in range(8):
#         for x in range(5):
#             if not (x,-y) in taken_spots:
#                 return (x,-y)


# def append(self, item):
#     icon = Draggable(
#         parent = Inventory().item_parent,
#         model = 'quad',
#         texture = item,
#         color = color.white,
#         origin = (-.5,.5),
#         position = self.find_free_spot(),
#         z = -.1,
#         )
#     name = item.replace('_', ' ').title()
#     icon.tooltip = Tooltip(name)
#     icon.tooltip.background.color = color.color(0,0,0,.8)


#     def drag():
#         icon.org_pos = (icon.x, icon.y)

#     def drop():
#         icon.x = int(icon.x)
#         icon.y = int(icon.y)



#         '''if the spot is taken, swap positions'''
#         for c in self.children:
#             if c == icon:
#                 continue

#             if c.x == icon.x and c.y == icon.y:
#                 print('swap positions')
#                 c.position = icon.org_pos


#     icon.drag = drag
#     icon.drop = drop


