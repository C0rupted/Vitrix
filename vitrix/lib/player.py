import os
import ursina
from ursina.prefabs.first_person_controller import FirstPersonController

from lib.weapons.hammer import Hammer
from lib.weapons.pistol import Pistol
from lib.weapons.sword import Sword
from lib.weapons.axe import Axe

from lib.items.aid_kit import AidKit

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
        self.hit_info = self.intersects()

        self.thirdperson = False

        self.cursor.color = ursina.color.rgb(255, 0, 0, 255)

        self.gun = Pistol()
        self.hammer = Hammer()
        self.sword = Sword()
        self.axe = Axe()

        self.hammer.disable()
        self.sword.disable()
        self.axe.disable()

        self.item_order = ["gun", "hammer", "sword", "axe"]
        self.holding = "gun"

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
        if key == "space":
            self.jump()

        if key == "f1": # Third person
            if self.thirdperson: # Check if it's enabled
                self.thirdperson = False
                ursina.camera.z = -0
            else:
                self.thirdperson = True
                ursina.camera.z = -8

        if key == "f": # Switch item held
            if self.gun.enabled:
                self.gun.disable()
                self.hammer.enable()
            elif self.hammer.enabled:
                self.hammer.disable()
                self.sword.enable()
            elif self.sword.enabled:
                self.sword.disable()
                self.axe.enable()
            else:
                self.axe.disable()
                self.gun.enable()

    def death(self):
        self.death_message_shown = True

        self.on_disable()

        ursina.Audio("death").play() # Play death sound

        ursina.destroy(self.gun)
        self.rotation = 0
        self.camera_pivot.world_rotation_x = -45
        self.world_position = ursina.Vec3(0, 7, -35)
        self.cursor.color = ursina.color.rgb(0, 0, 0, a=0)

        self.dead_text = ursina.Text(
            text="You are dead!",
            color=ursina.color.rgb(0, 0, 0, 255),
            origin=ursina.Vec2(0, 0),
            position=ursina.Vec2(0, .2),
            scale=3
        )

        self.respawn_button = ursina.Button(
            text = "Respawn",
            scale=0.15,
            on_click=ursina.Sequence(ursina.Wait(.01), ursina.Func(self.respawn))
        )

        self.exit_button = ursina.Button(
            text = "Quit Game",
            position = ursina.Vec2(0, -.2),
            scale=0.15,
            on_click=ursina.Sequence(ursina.Wait(.01), ursina.Func(os._exit, 0))
        )
    
    def respawn(self):
        self.death_message_shown = False
        self.on_enable()
        self.gun = Pistol()
        self.rotation = ursina.Vec3(0,0,0)
        self.camera_pivot.world_rotation_x = 0
        self.world_position = ursina.Vec3(0,1,0)
        self.health = 100
        self.respawn_button.disable()
        self.dead_text.disable()
        self.exit_button.disable()

    def restore_health(self, amount: int):
        if self.health + amount > 100:
            self.health = 100
        else:
            self.health += amount

    def update(self):
        self.healthbar.scale_x = self.health / 100 * self.healthbar_size.x

        if self.y < -10:
            self.position = ursina.Vec3(0, 2, 0)

        if self.health <= 0: # Check if player is dead
            if not self.death_message_shown:
                self.death()
        else:
            super().update()
