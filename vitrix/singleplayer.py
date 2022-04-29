import os
import ursina

from lib.floor import Floor
from lib.map import Map
from lib.player import Player
from lib.enemy import Zombie

from lib.items.aid_kit import AidKit

from ursina.shaders.basic_lighting_shader import basic_lighting_shader

app = ursina.Ursina()
# The inventory needs to load after ursina app()
from lib.inventory import *

ursina.window.borderless = False
ursina.window.title = "Vitrix - Singleplayer"
ursina.window.exit_button.visible = False

paused = False

ursina.Entity.default_shader = basic_lighting_shader


floor = Floor()
map = Map()
sky = ursina.Entity(
    model="sphere",
    texture=os.path.join("assets", "textures", "sky.png"),
    scale=9999,
    double_sided=True
)

player = Player(ursina.Vec3(0, 1, 0))
aid_kit = AidKit(ursina.Vec3(10, 1.6, 3))

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
    if key == "l":
        enemies.append(Zombie(ursina.Vec3(0, 1.5, 0), player))


def update():
    if player.intersects(aid_kit).hit:
        print("aid kit collided")
        player.restore_health(aid_kit.health_restore)
        aid_kit.destroy()

sun = ursina.DirectionalLight()
sun.look_at(ursina.Vec3(1,-1,-1))


if __name__ == "__main__":
    app.run()