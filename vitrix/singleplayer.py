import os
from turtle import window_height, window_width

import ursina

from lib.floor import Floor
from lib.map import Map
from lib.player import Player
from lib.enemy import Zombie
from lib.bullet import Bullet

camera_height = 1366
camera_width = 768

app = ursina.Ursina()
ursina.window.borderless = False
ursina.window.title = "Vitrix"
ursina.window.exit_button.visible = False


floor = Floor()
map = Map()
sky = ursina.Entity(
    model="sphere",
    texture=os.path.join("assets/textures", "sky.png"),
    scale=9999,
    double_sided=True
)
player = Player(ursina.Vec3(0, 1, 0))

lock = True
quit = False
bullet_tag = 1 
enemies = []

pause_text = ursina.Text(
                text="Paused",
                enabled=False,
                origin=ursina.Vec2(0, 0),
                scale=3)
controls_dict={
    "tab":"Pause the Game",
    "L":"Release a zombie",
    "left-click":"Fire",
    "space": "Jump",
    "alt-f4":"Exit game",
    "1":"Switch ammo"
}
controls_text = ursina.Text(
                text= "".join(f"{key} = {value}\n" for key,value in controls_dict.items() ),
                origin=ursina.Vec2(2.8, -3),
                scale=1
                )
def cycleAmmo(bullet_tag):  # default bullet tag is int 1

    if bullet_tag == 1:
        return 2
    else:
        return 1


def input(key):
    global lock
    global pause_text
    global bullet_tag

    if key == "tab" and player.health > 0:
        if lock == False:
            pause_text.enabled = False
            lock = True
            player.on_enable()
        else:
            pause_text.enabled = True
            lock = False
            player.on_disable()

    if key == "l":
        enemies.append(Zombie(ursina.Vec3(0, 1.5, 0), player))

    if key == "1":
        bullet_tag = cycleAmmo(bullet_tag)

    if key == "left mouse down" and player.health > 0:
        if not player.gun.on_cooldown:
            player.gun.on_cooldown = True
            b_pos = player.position + ursina.Vec3(0, 2, 0)
            ursina.Audio("pew").play()
            bullet = Bullet(b_pos, player.world_rotation_y, -player.camera_pivot.world_rotation_x, tag = bullet_tag)
            ursina.destroy(bullet, delay=4)
            ursina.invoke(setattr, player.gun, 'on_cooldown', False, delay=.25)



if __name__ == "__main__":
    app.run()
