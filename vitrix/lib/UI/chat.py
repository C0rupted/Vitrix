from vitrix_engine import *
from lib.classes.network import Network

class Chat(Entity):
    def __init__(self, network: Network, username: str, **kwargs):
        super().__init__(
            parent = camera.ui,
            model = Quad(radius=0),
            texture = 'white_cube',
            scale = Vec2(.5, .6),
            position = Vec2(-.636, .2),
            color = color.white33,
            )

        self.list = []
        self.network = network
        self.prefix = f"[{username}]  "

        self.chat_text = Text()
        self.text_field = InputField(position=Vec2(-.636, -.13))

        self.disable()

        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def update(self):
        if len(self.list) >= 24:
            self.list.pop(0)
        
        destroy(self.chat_text)
        self.chat_text = Text(
            text= "".join(f"{item}\n" for item in self.list),
            position = (-.87, .485),
            z=camera.clip_plane_near,
            scale=1
        )

    
    def input(self, key):
        if key == "enter":
            #temp = self.prefix + self.text_field.text
            self.network.send_message(self.prefix + self.text_field.text)
            self.list.append(self.prefix + self.text_field.text)
            self.text_field.text = ""

    def enable(self):
        self.enabled = True
        self.chat_text.enabled = True
        self.text_field.enabled = True
    
    def disable(self):
        self.enabled = False
        self.chat_text.enabled = False
        self.text_field.enabled = False
