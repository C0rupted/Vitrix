import os
import sys
import time
import socket
import threading
import ursina

from lib.notification import notify
from lib.network import Network
from lib.floor import Floor
from lib.map import Map
from lib.player import Player
from lib.enemy import Enemy
from lib.bullet import Bullet

cheats = False

from os.path import isfile

if isfile("ib.cfg"):
    if open("ib.cfg", "r").read() == "1":
        print("You can't play multiplayer.")
        print("Reason: Cheats")
        notify("You can't play multiplayer.", "You have been banned\nReason: Cheats")
        sys.exit(1)
else:
    pass

import lib.server_chooser as server_chooser
from lib.anticheat import *

try:
    with open("data.txt", "r") as file:
        lines =  file.readlines()
        username = lines[0].strip()
        server_addr = lines[1].strip()
        server_port = lines[2].strip()
except FileNotFoundError:
    sys.exit(1)


while True:
    print(username, " ", server_addr, " ", server_port)
    try:
        server_port = int(server_port)
    except ValueError:
        print("\nThe port you entered was not a number, try again with a valid port...")
        continue

    n = Network(server_addr, server_port, username)
    n.settimeout(5)

    error_occurred = False

    try:
        n.connect()
    except ConnectionRefusedError:
        notify("Vitrix Error", 
                 "Connection refused! This can be because server hasn't started or has reached it's player limit.")
        error_occurred = True
    except socket.timeout:
        notify("Vitrix Error", 
                 "Server took too long to respond, please try again later...")
        error_occurred = True
    except socket.gaierror:
        notify("Vitrix Error", 
                 "The IP address you entered is invalid, please try again with a valid address...")
        error_occurred = True
    finally:
        n.settimeout(None)

    if error_occurred:
        sys.exit(1)
    
    if not error_occurred:
        break


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


app = ursina.Ursina()
ursina.window.borderless = False
ursina.window.title = "Vitrix - Multiplayer"
ursina.window.exit_button.visible = False

pew = ursina.Audio("pew", autoplay=False)
pew.volume = 0.2

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
prev_pos = player.world_position
prev_dir = player.world_rotation_y
enemies = []

pause_text = ursina.Text(
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

reload_warning_text.disable()
pause_text.enabled = False
exit_button.disable()


def receive():
    while True:
        try:
            info = n.receive_info()
        except Exception as e:
            print(e)
            continue

        if not info:
            print("Server has stopped! Exiting...")
            sys.exit()

        if info["object"] == "player":
            enemy_id = info["id"]

            if info["joined"]:
                new_enemy = Enemy(ursina.Vec3(*info["position"]), enemy_id, info["username"])
                new_enemy.health = info["health"]
                enemies.append(new_enemy)
                continue

            enemy = None

            for e in enemies:
                if e.id == enemy_id:
                    enemy = e
                    break

            if not enemy:
                continue

            if info["left"]:
                enemies.remove(enemy)
                ursina.destroy(enemy)
                continue

            enemy.world_position = ursina.Vec3(*info["position"])
            enemy.rotation_y = info["rotation"]

        elif info["object"] == "bullet":
            b_pos = ursina.Vec3(*info["position"])
            b_dir = info["direction"]
            b_x_dir = info["x_direction"]
            b_damage = info["damage"]
            new_bullet = Bullet(b_pos, b_dir, b_x_dir, n, b_damage, slave=True)
            ursina.destroy(new_bullet, delay=2)

        elif info["object"] == "health_update":
            enemy_id = info["id"]

            enemy = None

            if enemy_id == n.id:
                enemy = player
            else:
                for e in enemies:
                    if e.id == enemy_id:
                        enemy = e
                        break

            if not enemy:
                continue

            enemy.health = info["health"]


def update():
    if player.health > 0:
        global prev_pos, prev_dir

        if prev_pos != player.world_position or prev_dir != player.world_rotation_y:
            n.send_player(player)

        prev_pos = player.world_position
        prev_dir = player.world_rotation_y


def input(key):
    global lock, pause_text

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

    if key == "left mouse down" and player.health > 0:
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

    if key == "right mouse down":
        hit_info = ursina.raycast(player.world_position + ursina.Vec3(0,0,0), player.forward, 30, ignore=(player,))
        try:
            if hit_info.entity.is_crate:
                print(hit_info.entity.contents)
                ursina.destroy(hit_info.entity)
        except:
            pass
    

    check_speed(player.speed)
    check_jump_height(player.jump_height, 2.5)
    check_health(player.health)


def main():
    msg_thread = threading.Thread(target=receive, daemon=True)
    msg_thread.start()
    app.run()



if __name__ == "__main__":
    main()  
