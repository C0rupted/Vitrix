from vitrix_engine import *
#from lib.paths import GamePaths

class Inventory(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = Quad(radius=.015),
            texture = 'white_cube',
            texture_scale = (5, 3),
            scale = (.5, .3),
            origin = (-.5, .5),
            position = (-.3,.4),
            color = color.color(0, 0, .1, .9),
            )
        
        self.items = [
            [["empty", 0], ["empty", 0], ["empty", 0], ["empty", 0], ["empty", 0]],
            [["empty", 0], ["empty", 0], ["empty", 0], ["empty", 0], ["empty", 0]],
            [["empty", 0], ["empty", 0], ["empty", 0], ["empty", 0], ["empty", 0]]
        ]

        self.entities = [
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None]
        ]

    
    def find_free_spot(self):
        y = 0
        for items in self.items:
            x = 0
            for item in items:
                if item[0] == "empty":
                    return y, x
                x += 1
            y += 1


    def find_item(self, id: str):
        y = 0
        for items in self.items:
            x = 0
            for item in items:
                if item[0] == id:
                    return y, x
                x += 1
            y += 1
        return False


    def append(self, id: str, amount: int):
        if self.find_item(id) != False:
            column, row = self.find_item(id)
            self.items[column][row][1] += amount
            icon = self.entities[column][row]
            name = id.replace('_', ' ').title()
            icon.tooltip.text = f"{name} x{self.items[column][row][1]}"
        else:
            try:
                column, row = self.find_free_spot()
            except:
                return False
            
            self.items[column][row][0] = id
            self.items[column][row][1] = amount

            icon = Draggable(
                parent = self,
                model = 'quad',
                texture = id,
                color = color.white,
                scale_x = 1/self.texture_scale[0],
                scale_y = 1/self.texture_scale[1],
                origin = (-.5,.5),
                x = row * 1/self.texture_scale[0],
                y = -column * 1/self.texture_scale[1],
                z = -.5,
            )
            name = id.replace('_', ' ').title()

            icon.tooltip = Tooltip(f"{name} x1")
            icon.tooltip.background.color = color.color(0, 0, 0, .8)

            def drag():
                icon.org_pos = (icon.x, icon.y)
                icon.z -= .01

            def drop():
                icon.x = int((icon.x + (icon.scale_x/2)) * 5) / 5
                icon.y = int((icon.y - (icon.scale_y/2)) * 3) / 3
                icon.z += .01

                if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                    icon.position = (icon.org_pos)
                    return

                for columns in self.entities:
                    for entity in columns:
                        if entity == icon:
                            continue
                        try:
                            if entity.x == icon.x and entity.y == icon.y:
                                entity.position = icon.org_pos
                        except:
                            pass


            icon.drag = drag
            icon.drop = drop

            self.entities[column][row] = icon



if __name__ == '__main__':
    app = Ursina()
    inventory = Inventory()

    def add_item():
        inventory.append(random.choice(["gun", "first_aid_kit", "first_aid_kit", "first_aid_kit", 
                                        "first_aid_kit"]), 1)

    add_item_button = Button(
        scale = (.1,.1),
        x = -.5,
        color = color.lime.tint(-.25),
        text = '+',
        tooltip = Tooltip('Add random item'),
        on_click = add_item
        )

    bg = Entity(parent=camera.ui, model='quad', texture='shore', scale_x=camera.aspect_ratio, z=1)

    window.exit_button.visible = False
    window.fps_counter.enabled = False
    app.run()