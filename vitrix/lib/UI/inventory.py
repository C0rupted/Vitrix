from vitrix_engine import *
from vitrix_engine.prefabs.first_person_controller import FirstPersonController



# inventory hotbar
def inventory():
    hotbar = Entity(
        model='quad',
        parent=camera.ui,
        enable = True,
    )

    # Set size and position
    hotbar.scale_y=0.3
    hotbar.scale_x=0.4
    hotbar.y=-0.1 + (hotbar.scale_y*0.5)
    hotbar.x=-0.57

    # UI design
    hotbar.color=color.dark_gray




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