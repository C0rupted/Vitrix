import os
import ursina

from lib.entities.floor import Floor
from lib.entities.map import Map
from lib.entities.player import Player
from lib.entities.enemy import Zombie

from lib.items.aid_kit import AidKit
from lib.items.ammo import Ammo

from ursina.shaders.basic_lighting_shader import basic_lighting_shader

app = ursina.Ursina()
# The inventory needs to load after ursina app()
from lib.UI.inventory import *

ursina.window.borderless = False
ursina.window.exit_button.visible = False

paused = False
ursina.window.title = "Vitrix - Singleplayer"
ursina.Entity.default_shader = basic_lighting_shader
ursina.window.fullscreen = True

floor = Floor()
map = Map()
sky = ursina.Entity(
    model="sphere",
    texture=os.path.join("assets", "textures", "sky.png"),
    scale=9999,
    double_sided=True
)

def toggle_fullscreen():
    if ursina.window.fullscreen:
        ursina.window.fullscreen = False
    else:
        ursina.window.fullscreen = True

fullscreen_button = ursina.Button(
            text="Toggle Fullscreen",
            position=ursina.Vec2(.2, 0),
            scale=0.15,
            enabled=False,
            on_click=ursina.Func(toggle_fullscreen)
        )
fullscreen_button.fit_to_text()


player = Player(ursina.Vec3(0, 1, 0))
aid_kit = AidKit(ursina.Vec3(10, 1.6, 3))
ammo = Ammo(ursina.Vec3(15, 1, 3))

enemies = []


#controls_dict={
#    "tab":"Pause the Game",
#    "L":"Release a zombie",
#    "left-click":"Fire",
#    "space": "Jump",
#    "alt-f4":"Exit game",
#    "1":"Switch ammo"
#}
#controls_text = ursina.Text(
#                text= "".join(f"{key} = {value}\n" for key,value in controls_dict.items() ),
#                origin=ursina.Vec2(2.8, -3),
#                scale=1
#                )
#def cycleAmmo(bullet_tag):  # default bullet tag is int 1
#    if bullet_tag == 1:
#        return 2
#    else:
#        return 1


def input(key):
    if key == ("tab" or "escape"):
        if fullscreen_button.enabled:
            fullscreen_button.disable()
        else:
            fullscreen_button.enable()
    
    if key == "l":
        enemies.append(Zombie(ursina.Vec3(0, 1.5, 0), player))


sun = ursina.DirectionalLight()
sun.look_at(ursina.Vec3(1,-1,-1))


if __name__ == "__main__":
    app.run(info=False)