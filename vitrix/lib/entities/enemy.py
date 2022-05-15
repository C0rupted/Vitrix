from vitrix_engine import *
import random

zombie_names=["Peter","Harry","Sayed","Usman","Gopal","Ryan","Gerald","James","Robert","Frank","Leon","Jordan","Russell","Johny","Ankur","Carl","Suresh"]

class Enemy(Entity):
    def __init__(self, position: Vec3, identifier: str, username: str):
        super().__init__(
            position=position,
            model="cube",
            origin_y=-0.5,
            collider="box",
            texture="white_cube",
            color=color.color(0, 0, 1),
            scale=Vec3(1, 2, 1),
            add_to_scene_entities=False
        )
        self.gun = Entity(
            parent=self,
            position=Vec3(0.55, 0.5, 0.6),
            scale=Vec3(0.1, 0.2, 0.65),
            model="cube",
            texture="white_cube",
            color=color.color(0, 0, 0.4)
        )

        self.name_tag = Text(
            parent=self,
            text=username,
            position=Vec3(0, 1.3, 0),
            scale=Vec2(5, 3),
            billboard=True,
            origin=Vec2(0, 0)
        )

        self.is_enemy = True
        self.health = 150
        self.id = identifier
        self.username = username

        scene.entities.append(self)


    def update(self):
        if self.health <= 0:
            destroy(self)


class Zombie(Entity):
    def __init__(self, position: Vec3, player):
        super().__init__(
            position=position,
            model="cube",
            origin_y=-0.5,
            collider="box",
            texture="white_cube",
            color=color.color(0, 0, 1),
            scale=Vec3(1, 2, 1)
        )

        self.growl = Audio("zombie_growl")
        self.growl.loop = True
        self.growl.volume = 0.5
        self.growl.play()

        self.name_tag = Text(
            parent=self,
            text=random.choice(zombie_names),  #Random zombie names
            position=Vec3(0, 1.3, 0),
            scale=Vec2(5, 3),
            billboard=True,
            origin=Vec2(0, 0)
        )

        self.is_enemy = True
        self.health = 45
        self.player = player
        


    def update(self):

        try:
            color_saturation = 1 - self.health / 30
        except AttributeError:
            self.health = 30
            color_saturation = 1 - self.health / 30

        self.color = color.color(0, color_saturation, 1)

        
        dist = distance_xz(self.player.position, self.position)
        if dist > 40:
            pass

        self.look_at_2d(self.player.position, 'y')
        hit_info = raycast(self.world_position + Vec3(0,1,0), self.forward, 30, ignore=(self,))
        if hit_info.entity == self.player:
            if dist > 1.5:
                self.position += self.forward * time.dt * 2
            else:
                self.player.health -= 10
                self.player.healthbar.value = self.player.health
                Audio("hurt").play()
                self.position += self.forward * time.dt * -150

        
        if self.health <= 0:
            self.growl.stop()
            Audio("splat").play()
            destroy(self)

        
