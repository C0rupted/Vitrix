"""
Server script for hosting games
"""

import socket
import json
import time
import random
import threading

from os.path import isfile
if not isfile("server/anticheat.py"):
    import sys
    print("Anticheat not found, can't start")
    sys.exit(1)

from server.anticheat import *

from vitrix.lib.player import Player

ADDR = "0.0.0.0"
PORT = 26822
MAX_PLAYERS = 10
MSG_SIZE = 2048


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ADDR, PORT))
s.listen(MAX_PLAYERS)


players = {}


def generate_id(player_list: dict, max_players: int):
    """
    Generate a unique identifier

    Args:
        player_list (dict): dictionary of existing players
        max_players (int): maximum number of players allowed

    Returns:
        str: the unique identifier
    """

    while True:
        unique_id = str(random.randint(1, max_players))
        if unique_id not in player_list:
            return unique_id


def handle_messages(identifier: str):
    client_info = players[identifier]
    conn: socket.socket = client_info["socket"]
    username = client_info["username"]

    while True:
        try:
            msg = conn.recv(MSG_SIZE)
        except ConnectionResetError:
            break

        if not msg:
            break

        msg_decoded = msg.decode("utf8")

        try:
            left_bracket_index = msg_decoded.index("{")
            right_bracket_index = msg_decoded.index("}") + 1
            msg_decoded = msg_decoded[left_bracket_index:right_bracket_index]
        except ValueError:
            continue

        try:
            msg_json = json.loads(msg_decoded)
        except Exception as e:
            print(e)
            continue

        print(f"Received message from player {username} with ID {identifier}")

        if msg_json["object"] == "player":
            players[identifier]["position"] = msg_json["position"]
            players[identifier]["rotation"] = msg_json["rotation"]
            players[identifier]["health"] = msg_json["health"]

        for player_id in players:
            if player_id != identifier:
                player_info = players[player_id]
                player_conn: socket.socket = player_info["socket"]
                try:
                    player_conn.sendall(msg_decoded.encode("utf8"))
                except OSError:
                    pass


    for player_id in players:
        if player_id != identifier:
            player_info = players[player_id]
            player_conn: socket.socket = player_info["socket"]
            try:
                player_conn.send(json.dumps({"id": identifier, "object": "player", "joined": False, "left": True}).encode("utf8"))
            except OSError:
                pass

    print(f"Player {username} with ID {identifier} has left the game...")
    del players[identifier]
    conn.close()


def main():
    print("Server started, listening for new connections...")

    while True:
        conn, addr = s.accept()
        new_id = generate_id(players, MAX_PLAYERS)
        conn.send(new_id.encode("utf8"))
        username = conn.recv(MSG_SIZE).decode("utf8")
        new_player_info = {"socket": conn, "username": username, "position": (0, 1, 0), "rotation": 0, "health": 100}


        for player_id in players:
            if player_id != new_id:
                player_info = players[player_id]
                player_conn: socket.socket = player_info["socket"]
                try:
                    player_conn.send(json.dumps({
                        "id": new_id,
                        "object": "player",
                        "username": new_player_info["username"],
                        "position": new_player_info["position"],
                        "health": new_player_info["health"],
                        "joined": True,
                        "left": False
                    }).encode("utf8"))
                except OSError:
                    pass

        for player_id in players:
            if player_id != new_id:
                player_info = players[player_id]
                try:
                    conn.send(json.dumps({
                        "id": player_id,
                        "object": "player",
                        "username": player_info["username"],
                        "position": player_info["position"],
                        "health": player_info["health"],
                        "joined": True,
                        "left": False
                    }).encode("utf8"))
                    time.sleep(0.1)
                except OSError:
                    pass

        players[new_id] = new_player_info

        msg_thread = threading.Thread(target=handle_messages, args=(new_id,), daemon=True)
        msg_thread.start()

        print(f"New connection from {addr}, assigned ID: {new_id}...")
        
        check_speed(Player.speed)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        pass

    except SystemExit:
        pass

    finally:
        print("Exiting")
        
        s.close()
