import ursina
from ursina.prefabs.first_person_controller import FirstPersonController
import os.path
from lib.inventory import Inventory, Hotbar


class Player(FirstPersonController):
    def __init__(self, position: ursina.Vec3):
        super().__init__(
            position=position,
            model="cube",
            jump_height=2.5,
            jump_duration=0.4,
            origin_y=-2,
            collider="box",
            speed=7
        )

        self.hotbar = Hotbar()

        self.items = []
        self.inventory = None

        gun_item = None
        # hotbar_gun_item = ursina.Button(parent=self.hotbar.item_parent, model='quad', texture="assets/icon_gun.png", origin=(-.5,.5), position=self.hotbar.find_free_spot(), z=-.1)

        self.thirdperson = False
        self.inventory_opened = False

        self.cursor.color = ursina.color.rgb(255, 0, 0, 122)

        self.gun = ursina.Entity(
            parent=ursina.camera.ui,
            position=ursina.Vec2(0.6, -0.45),
            scale=ursina.Vec3(0.1, 0.2, 0.65),
            rotation=ursina.Vec3(-20, -20, -5),
            model="cube",
            texture=os.path.join("assets", "t_gun.png"),
            color=ursina.color.color(0, 0, 0.4),
            on_cooldown=False
        )

        self.healthbar_pos = ursina.Vec2(0, 0.45)
        self.healthbar_size = ursina.Vec2(0.8, 0.04)
        self.healthbar_bg = ursina.Entity(
            parent=ursina.camera.ui,
            model="quad",
            color=ursina.color.rgb(255, 0, 0),
            position=self.healthbar_pos,
            scale=self.healthbar_size
        )
        self.healthbar = ursina.Entity(
            parent=ursina.camera.ui,
            model="quad",
            color=ursina.color.rgb(0, 255, 0),
            position=self.healthbar_pos,
            scale=self.healthbar_size
        )

        self.health = 100
        self.death_message_shown = False

    def input(self, key):
        global gun_item, inventory
        if key == "f1": # Third person
            if self.thirdperson: # Check if it's enabled
                self.thirdperson = False
                ursina.camera.z = -0

            else:
                self.thirdperson = True
                ursina.camera.z = -10
        
        # Inventory
        if key == "i":
            if self.inventory_opened:
                self.inventory_opened = False
                ursina.destroy(inventory, delay=0.1)
                ursina.destroy(gun_item)

            else:
                self.inventory_opened = True
                inventory = Inventory()
                gun_item = ursina.Button(parent=inventory.item_parent, model='quad', texture="assets/icon_gun.png", origin=(-.5,.5), z=-.1)

    def death(self):
        self.death_message_shown = True

        self.on_disable()

        ursina.Audio("death").play() # Play death sound

        ursina.destroy(self.gun)
        self.rotation = 0
        self.camera_pivot.world_rotation_x = -45
        self.world_position = ursina.Vec3(0, 7, -35)
        self.cursor.color = ursina.color.rgb(0, 0, 0, a=0)

        ursina.Text(
            text="You are dead!",
            origin=ursina.Vec2(0, 0),
            scale=3
        )

    def update(self):
        self.healthbar.scale_x = self.health / 100 * self.healthbar_size.x

        if self.y < -10:
            self.position = ursina.Vec3(0, 2, 0)

        if self.health <= 0: # Check if player is dead
            if not self.death_message_shown:
                self.death()
        else:
            super().update()
