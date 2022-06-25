import socket
import json

from lib.entities.player import Player
from lib.entities.enemy import Enemy
from lib.entities.bullet import Bullet


class Network:
    def __init__(self, server_addr: str, server_port: int, username: str):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = server_addr
        self.port = server_port
        self.username = username
        self.recv_size = 2048
        self.id = 0


    def settimeout(self, value):
        self.client.settimeout(value)


    def connect(self):
        """
        Connect to the server and get a unique identifier
        """

        self.client.connect((self.addr, self.port))
        self.id = self.client.recv(self.recv_size).decode("utf8")
        self.client.send(self.username.encode("utf8"))
        if self.client.recv(self.recv_size).decode("utf8") == "False":
            return False
        else:
            return True


    def receive_info(self):
        try:
            msg = self.client.recv(self.recv_size)
        except socket.error as e:
            print(e)

        if not msg:
            return None

        msg_decoded = msg.decode("utf8")

        if msg_decoded == "kicked":
            return "kicked"
        if msg_decoded == "banned":
            return "banned"

        left_bracket_index = msg_decoded.index("{")
        right_bracket_index = msg_decoded.index("}") + 1
        msg_decoded = msg_decoded[left_bracket_index:right_bracket_index]

        msg_json = json.loads(msg_decoded)

        return msg_json


    def send_player(self, player: Player):
        player_info = {
            "object": "player",
            "id": self.id,
            "position": (player.world_x, player.world_y, player.world_z),
            "rotation": player.rotation_y,
            "health": player.health,
            "joined": False,
            "left": False
        }
        player_info_encoded = json.dumps(player_info).encode("utf8")

        try:
            self.client.send(player_info_encoded)
        except socket.error as e:
            print(e)


    def send_bullet(self, bullet: Bullet):
        bullet_info = {
            "object": "bullet",
            "position": (bullet.world_x, bullet.world_y, bullet.world_z),
            "damage": bullet.damage,
            "direction": bullet.direction,
            "x_direction": bullet.x_direction
        }

        bullet_info_encoded = json.dumps(bullet_info).encode("utf8")

        try:
            self.client.send(bullet_info_encoded)
        except socket.error as e:
            print(e)


    def send_health(self, player: Enemy):
        health_info = {
            "object": "health_update",
            "id": player.id,
            "health": player.health
        }

        health_info_encoded = json.dumps(health_info).encode("utf8")

        try:
            self.client.send(health_info_encoded)
        except socket.error as e:
            print(e)


    def send_message(self, message: str):
        message_info = {
            "object": "chat_message",
            "message": message
        }

        message_info_encoded = json.dumps(message_info).encode("utf8")

        try:
            self.client.send(message_info_encoded)
        except socket.error as e:
            print(e)


    def send_command(self, type: str, target: str):
        command_info = {
            "object": "command",
            "type": type,
            "author": self.username,
            "target": target
        }

        command_info_encoded = json.dumps(command_info).encode("utf8")

        try:
            self.client.send(command_info_encoded)
        except socket.error as e:
            print(e)
