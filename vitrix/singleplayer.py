import os
import ursina

from lib.floor import Floor
from lib.map import Map
from lib.player import Player
from lib.enemy import Zombie
from lib.bullet import Bullet



app = ursina.Ursina()
ursina.window.borderless = False
ursina.window.title = "Vitrix"
ursina.window.exit_button.visible = False


floor = Floor()
map = Map()
sky = ursina.Entity(
    model="sphere",
    texture=os.path.join("assets", "sky.png"),
    scale=9999,
    double_sided=True
)
player = Player(ursina.Vec3(0, 1, 0))

lock = True
quit = False
prev_pos = player.world_position
prev_dir = player.world_rotation_y
enemies = []

pause_text = ursina.Text(
                text="Paused",
                enabled=False,
                origin=ursina.Vec2(0, 0),
                scale=3)



def input(key):
    global lock
    global pause_text

    if key == "tab":
        if lock == False:
            pause_text.enabled = False
            lock = True
            player.on_enable()
            player.is_paused = True
        else:
            pause_text.enabled = True
            lock = False
            player.on_disable()
            player.is_paused = False

    if key == "l":
        enemies.append(Zombie(ursina.Vec3(0, 1.5, 0), player))

    if key == "left mouse down" and player.health > 0:
        if not player.gun.on_cooldown:
            player.gun.on_cooldown = True
            b_pos = player.position + ursina.Vec3(0, 2, 0)
            ursina.Audio("pew").play()
            bullet = Bullet(b_pos, player.world_rotation_y, -player.camera_pivot.world_rotation_x)
            ursina.destroy(bullet, delay=2)
            ursina.invoke(setattr, player.gun, 'on_cooldown', False, delay=.50)


def main():
    app.run()



if __name__ == "__main__":
    main()
