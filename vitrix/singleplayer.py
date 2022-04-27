import os
import time
import ursina
import threading

from lib.floor import Floor
from lib.map import Map
from lib.player import Player
from lib.enemy import Zombie
from lib.bullet import Bullet


app = ursina.Ursina()
ursina.window.borderless = False
ursina.window.title = "Vitrix - Singleplayer"
ursina.window.exit_button.visible = False

paused = False

pew = ursina.Audio("pew", autoplay=False)
pew.volume = 0.2

floor = Floor()
map = Map()
sky = ursina.Entity(
    model="sphere",
    texture=os.path.join("assets", "textures", "sky.png"),
    scale=9999,
    double_sided=True
)
player = Player(ursina.Vec3(0, 1, 0))

lock = True
quit = False
shots_left = 5
enemies = []

pause_text = ursina.Text(
            ignore_paused=True,
                text="Paused",
                enabled=False,
                position=ursina.Vec2(0, .3),
                scale=3)

reload_warning_text = ursina.Text(
                       text="Please reload!",
                       enabled=False,
                       scale=2)

exit_button = ursina.Button(
            ignore_paused=True,
                text = "Quit Game",
                scale=0.15,
                on_click=ursina.Sequence(ursina.Wait(.01), ursina.Func(os._exit, 0))
            )

pause_text.enabled = False
reload_warning_text.disable()
exit_button.disable()

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

def hide_reload_warning():
    time.sleep(1)
    reload_warning_text.disable()

def reload():
    global shots_left
    global player

    ursina.Audio("reload.wav")
    time.sleep(3)
    shots_left = 5
    player.speed = 7
    


def input(key):
    global lock
    global shots_left
    global pause_text

    if key == "tab" or key == "escape":
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
    
    if key == "r":
        player.speed = 3
        threading.Thread(target=reload).start()
        

    if key == "l":
        enemies.append(Zombie(ursina.Vec3(0, 1.5, 0), player))

    #if key == "1":
    #    bullet_tag = cycleAmmo(bullet_tag)

    if key == "left mouse down" and player.health > 0 and player.gun.enabled:
        if not player.gun.on_cooldown:
            if shots_left <= 0 and player.speed == 7:
                reload_warning_text.enable()
                threading.Thread(target=hide_reload_warning).start()
                return
            player.gun.on_cooldown = True
            b_pos = player.position + ursina.Vec3(0, 2, 0)
            pew.play()
            bullet = Bullet(b_pos, player.world_rotation_y, -player.camera_pivot.world_rotation_x)
            shots_left -= 1
            ursina.destroy(bullet, delay=4)
            ursina.invoke(setattr, player.gun, 'on_cooldown', False, delay=.25)
    
    if key == "right mouse down" and player.hammer.enabled:
        hit_info = ursina.raycast(player.world_position + ursina.Vec3(0,1,0), player.forward, 30, ignore=(player,))
        try:
            if hit_info.entity.is_crate:
                print(hit_info.entity.contents)
                ursina.destroy(hit_info.entity)
        except:
            pass

# def input(key):
#     global lock, pause_text

#     if key == "tab" or key == "escape":
#         if lock == False:
#             pause_text.enabled = False
#             exit_button.disable()
#             lock = True
#             player.on_enable()
#         else:
#             pause_text.enabled = True
#             exit_button.enable()
#             lock = False
#             player.on_disable()

#def update():
#    check_speed(player.speed)
#    check_jump_height(player.jump_height, 2.5)
#    check_health(player.health)

if __name__ == "__main__":
    app.run()
