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
enemies = []

pause_text = ursina.Text(
                text="Paused",
                enabled=False,
                position=ursina.Vec2(0, .3),
                scale=3)

exit_button = ursina.Button(
                text = "Quit Game",
                scale=0.15,
                on_click=ursina.Sequence(ursina.Wait(.01), ursina.Func(os._exit, 0))
            )

pause_text.enabled = False
exit_button.disable()


def input(key):
    global lock
    global pause_text

    if key == "tab" and player.health > 0:
        if lock == False:
            pause_text.enabled = False
            exit_button.disable()
            lock = True
            player.on_enable()
        else:
            pause_text.enabled = True
            exit_button.enable()
            lock = False
            player.on_disable()

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



if __name__ == "__main__":
    app.run()
