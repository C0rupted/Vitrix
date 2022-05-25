import os
import time
import threading
from vitrix_engine import *
from vitrix_engine.prefabs.first_person_controller import FirstPersonController

from lib.entities.bullet import Bullet
from lib.entities.crate import Crate
from lib.entities.enemy import Zombie, Enemy
from lib.UI.healthbar import HealthBar
from lib.UI.crosshair import Crosshair
from lib.weapons.hammer import Hammer
from lib.weapons.pistol import Pistol
from lib.weapons.sword import Sword
from lib.weapons.battleaxe import BattleAxe
from lib.items.aid_kit import AidKit
from lib.items.ammo import Ammo
# from lib.UI.inventory import inventory


class Player(FirstPersonController):
    def __init__(self, position: Vec3, network = False):
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

        if not network:
            self.singleplayer = True
        else:
            self.singleplayer = False
            self.network = network

        self.pew = Audio("pew", autoplay=False)
        self.pew.volume = 0.2

        self.gun = Pistol()
        self.hammer = Hammer()
        self.sword = Sword()
        self.axe = BattleAxe()

        self.hammer.disable()
        self.sword.disable()
        self.axe.disable()

        self.item_order = ["gun", "hammer", "sword", "axe"]
        self.holding = "gun"

        self.pause_text = Text(
                    ignore_paused=True,
                        text="Paused",
                        enabled=False,
                        position=Vec2(0, .3),
                        scale=3)

        self.reload_warning_text = Text(
                            text="Please reload!",
                            enabled=False,
                            scale=2)

        self.exit_button = Button(
                    ignore_paused=True,
                        text = "Quit Game",
                        scale=0.15,
                        on_click=Sequence(Wait(.01), Func(os._exit, 0))
                    )

        self.rounds_counter = Text(
                        text="Rounds Left: 5",
                        position=Vec2(.5, .47),
                        scale=2.5
                    )

        self.dead_text = Text(
                        text="You are dead!",
                        origin=Vec2(0, 0),
                        position=Vec2(0, .2),
                        scale=3
                    )

        self.respawn_button = Button(
                        text = "Respawn",
                        scale=0.15,
                        on_click=Func(self.respawn)
        )

        self.pause_text.disable()
        self.reload_warning_text.disable()
        self.exit_button.disable()
        self.dead_text.disable()
        self.respawn_button.disable()

        self.health = 150
        self.healthbar = HealthBar(self.health)
        self.crosshair = Crosshair()

        self.rounds_left = 5
        self.paused = False
        self.shots_left = 5
        self.reach = 6
        self.death_message_shown = False

        self.lock = False
        # self._inventory = None
        # self.inventory_opened = False

    def hide_reload_warning(self):
        time.sleep(1)
        self.reload_warning_text.disable()

    def reload(self):
        self.speed = 3
        if self.rounds_left <= 0:
            self.speed = 7
            self.rounds_counter.text = "Rounds Left: 0"
            return

        Audio("reload.wav")
        time.sleep(3)
        self.shots_left = 5
        self.speed = 7

        self.rounds_left -= 1
        self.rounds_counter.text = "Rounds Left: " + str(self.rounds_left)

    def input(self, key):
        if key == "space":
            self.jump()

        if key == "f1": # Third person
            if self.thirdperson: # Check if it's enabled
                self.thirdperson = False
                camera.z = -0
            else:
                self.thirdperson = True
                camera.z = -8

        if key == "f": # Switch item held
            if self.gun.enabled:
                self.gun.disable()
                self.hammer.enable()
                self.crosshair.set_melee()
            elif self.hammer.enabled:
                self.hammer.disable()
                self.sword.enable()
                self.crosshair.set_melee()
            elif self.sword.enabled:
                self.sword.disable()
                self.axe.enable()
                self.crosshair.set_melee()
            else:
                self.axe.disable()
                self.gun.enable()
                self.crosshair.set_ranged()

        if key == "r" and self.gun.enabled:
            threading.Thread(target=self.reload).start()

        # Inventory key access

        #if key == 'i':
        #    if not self.inventory_opened:
        #       _inventory = inventory()
        #       inventory_opened = True
        #    else:
        #       _inventory = None
        #       inventory_opened = False
        #
        #    if self.lock == False:
        #        self.lock = True
        #        self.on_enable()
        #    else:
        #        self.lock = False
        #        self.on_disable()

        if key == "left mouse down" and self.health > 0:
            if not self.gun.on_cooldown and self.gun.enabled:
                if self.shots_left <= 0 and self.speed == 7:
                    self.reload_warning_text.enable()
                    threading.Thread(target=self.hide_reload_warning).start()
                    return
                self.gun.on_cooldown = True
                bullet_pos = self.position + Vec3(0, 2, 0)
                self.pew.play()
                if not self.singleplayer:
                    bullet = Bullet(bullet_pos, self.world_rotation_y,
                                    -self.camera_pivot.world_rotation_x, self.network)
                    self.network.send_bullet(bullet)
                else:
                    bullet = Bullet(bullet_pos, self.world_rotation_y,
                                    -self.camera_pivot.world_rotation_x)
                self.shots_left -= 1
                destroy(bullet, delay=2)
                invoke(setattr, self.gun, 'on_cooldown', False, delay=.25)
            elif self.sword.enabled or self.axe.enabled:
                slash = Audio("swing")
                slash.play()
                hit_info = raycast(self.world_position + Vec3(0, 2, 0), 
                                   self.camera_pivot.forward, self.reach, ignore=(self,))
                try:
                    if isinstance(hit_info.entity, (Zombie, Enemy)):
                        if (hit_info.entity.health - 20) <= 0:
                            slash.stop()
                        hit_info.entity.health -= 20
                except:
                    pass


        if key == "right mouse down":
            hit_info = raycast(self.world_position + Vec3(0, 2, 0), 
                               self.camera_pivot.forward, self.reach, ignore=(self,))
            try:
                for entity in hit_info.entities:
                    if isinstance(hit_info.entity, Crate) and self.hammer.enabled:
                        print(hit_info.entity.contents)
                        destroy(hit_info.entity)
                    if isinstance(hit_info.entity, AidKit):
                        print("Healing...")
                        self.restore_health(hit_info.entity.health_restore)
                        destroy(hit_info.entity)
                    if isinstance(hit_info.entity, Ammo):
                        self.restore_rounds(5)
                        destroy(hit_info.entity)
            except:
                pass

    def death(self):
        self.death_message_shown = True

        self.on_disable()

        Audio("death").play() # Play death sound

        destroy(self.gun)
        destroy(self.healthbar.icon)
        destroy(self.healthbar)
        self.rotation = 0
        self.camera_pivot.world_rotation_x = -45
        self.world_position = Vec3(0, 7, -35)
        self.crosshair.disable()

        self.dead_text.enable()
        self.respawn_button.enable()

        self.exit_button.position = Vec2(0, -.2)
        self.exit_button.enable()

    def respawn(self):
        self.death_message_shown = False
        self.on_enable()
        self.gun = Pistol()
        self.rotation = Vec3(0, 0, 0)
        self.camera_pivot.world_rotation_x = 0
        self.world_position = Vec3(0, 3, 0)
        self.exit_button.position = Vec2(0, 0)
        self.crosshair.enable()
        self.health = 150
        self.rounds_left = 5
        self.healthbar = HealthBar(self.health)
        self.respawn_button.disable()
        self.dead_text.disable()
        self.exit_button.disable()

    def restore_health(self, amount: int):
        if self.health + amount > 150:
            self.health = 150
        else:
            self.health += amount

        self.healthbar.value = self.health    

    def restore_rounds(self, amount: int):
        if self.rounds_left + amount > 15:
            self.rounds_left = 15
        else:
            self.rounds_left += amount

        self.rounds_counter.text = "Rounds Left: " + str(self.rounds_left)

    def update(self):
        if self.y < -10:
            self.position = Vec3(0, 2, 0)

        if self.health <= 0: # Check if player is dead
            if not self.death_message_shown:
                self.death()
        else:
            super().update()

        
    def land(self):
        i, x = 0, -1
        while i <= self.air_time:
            i += 0.18
            x += 1

        if x * 15 > 0:
            self.health -= x * 10
            self.healthbar.value = self.health

        self.air_time = 0
        self.grounded = True