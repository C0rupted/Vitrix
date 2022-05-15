import os
import sys
import socket

try:    # Check the internet connection before starting.
    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
    
    print("Internet connection detected!")
except:
    from lib.UI.notification import notify

    notify("Vitrix - Internet connection error", """Sorry, Vitrix couldn't connect 
    to the internet. Check your 
    internet connection and try 
    again later.""")

    os._exit(1)

import threading
from vitrix_engine import *
from vitrix_engine.shaders.basic_lighting_shader import basic_lighting_shader

from lib.UI.notification import notify
from lib.classes.network import Network
from lib.entities.floor import Floor
from lib.entities.map import Map
from lib.entities.player import Player
from lib.entities.enemy import Enemy
from lib.entities.bullet import Bullet

from os.path import isfile

if isfile("ib.cfg"):
    if open("ib.cfg", "r").read() == "1":
        print("You can't play multiplayer.")
        print("Reason: Cheats")
        notify("You can't play multiplayer.", "You have been banned\nReason: Cheats")
        sys.exit(1)
else:
    pass

import lib.UI.server_chooser as server_chooser
from lib.classes.anticheat import *

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


app = Ursina()
window.borderless = False
window.title = "Vitrix - Multiplayer"
window.exit_button.visible = False
window.fullscreen = True


floor = Floor()
map = Map()
sky = Entity(
    model=os.path.join("assets", "models", "sphere.obj"),
    texture=os.path.join("assets", "textures", "sky.png"),
    scale=9999,
    double_sided=True
)
Entity.default_shader = basic_lighting_shader

player = Player(Vec3(0, 1, 0), n)

def toggle_fullscreen():
    if window.fullscreen:
        window.fullscreen = False
    else:
        window.fullscreen = True

fullscreen_button = Button(
            text="Toggle Fullscreen",
            position=Vec2(.2, 0),
            scale=0.15,
            enabled=False,
            on_click=Func(toggle_fullscreen)
        )
fullscreen_button.fit_to_text()

prev_pos = player.world_position
prev_dir = player.world_rotation_y
enemies = []


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
                new_enemy = Enemy(Vec3(*info["position"]), enemy_id, info["username"])
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
                destroy(enemy)
                continue

            enemy.world_position = Vec3(*info["position"])
            enemy.rotation_y = info["rotation"]

        elif info["object"] == "bullet":
            b_pos = Vec3(*info["position"])
            b_dir = info["direction"]
            b_x_dir = info["x_direction"]
            b_damage = info["damage"]
            new_bullet = Bullet(b_pos, b_dir, b_x_dir, n, b_damage, slave=True)
            destroy(new_bullet, delay=2)

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
            if isinstance(enemy, Player):
                enemy.healthbar.value = enemy.health


def update():
    if player.health > 0:
        global prev_pos, prev_dir

        if prev_pos != player.world_position or prev_dir != player.world_rotation_y:
            n.send_player(player)

        prev_pos = player.world_position
        prev_dir = player.world_rotation_y

        check_speed(player.speed)
        check_jump_height(player.jump_height, 2.5)
        check_health(player.health)


def input(key):
    if key == ("tab" or "escape"):
        if fullscreen_button.enabled:
            fullscreen_button.disable()
        else:
            fullscreen_button.enable()

def main():
    msg_thread = threading.Thread(target=receive, daemon=True)
    msg_thread.start()
    app.run(info=False)



if __name__ == "__main__":
    main()  
