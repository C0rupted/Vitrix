import os
import sys
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


import lib.server_chooser as server_chooser

from server.anticheat import *

from os.path import isfile
if not isfile("../server/anticheat.py"):
    print("Anticheat not found, can't start")

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


app = ursina.Ursina()
ursina.window.borderless = False
ursina.window.title = "Vitrix - Multiplayer"
ursina.window.exit_button.visible = False


floor = Floor()
map = Map()
sky = ursina.Entity(
    model="sphere",
    texture=os.path.join("assets", "t_sky.png"),
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
                origin=ursina.Vec2(0, 0),
                scale=3
            )


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
    
    check_speed(player.speed, [5,7])
        


def input(key):
    global lock
    global pause_text

    if key == "tab":
        if lock == False:
            pause_text.enabled = False
            lock = True
            player.on_enable()
        else:
            pause_text.enabled = True
            lock = False
            player.on_disable()

    if key == "left mouse down" and player.health > 0:
        if not player.gun.on_cooldown:
            player.gun.on_cooldown = True
            b_pos = player.position + ursina.Vec3(0, 2, 0)
            ursina.Audio("pew").play()
            bullet = Bullet(b_pos, player.world_rotation_y, -player.camera_pivot.world_rotation_x, n)
            n.send_bullet(bullet)
            ursina.destroy(bullet, delay=2)
            ursina.invoke(setattr, player.gun, 'on_cooldown', False, delay=.50)


def main():
    msg_thread = threading.Thread(target=receive, daemon=True)
    msg_thread.start()
    app.run()



if __name__ == "__main__":
    main()  
