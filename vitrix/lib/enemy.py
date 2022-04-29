import ursina
import random

zombie_names=["Peter","Harry","Sayed","Usman","Gopal","Ryan","Gerald","James","Robert","Frank","Leon","Jordan","Russell","Johny","Ankur","Carl","Suresh"]

class Enemy(ursina.Entity):
    def __init__(self, position: ursina.Vec3, identifier: str, username: str):
        super().__init__(
            position=position,
            model="cube",
            origin_y=-0.5,
            collider="box",
            texture="white_cube",
            color=ursina.color.color(0, 0, 1),
            scale=ursina.Vec3(1, 2, 1)
        )
        self.gun = ursina.Entity(
            parent=self,
            position=ursina.Vec3(0.55, 0.5, 0.6),
            scale=ursina.Vec3(0.1, 0.2, 0.65),
            model="cube",
            texture="white_cube",
            color=ursina.color.color(0, 0, 0.4)
        )

        self.name_tag = ursina.Text(
            parent=self,
            text=username,
            position=ursina.Vec3(0, 1.3, 0),
            scale=ursina.Vec2(5, 3),
            billboard=True,
            origin=ursina.Vec2(0, 0)
        )

        self.health = 100
        self.id = identifier
        self.username = username


    def update(self):
        try:
            color_saturation = 1 - self.health / 100
        except AttributeError:
            self.health = 100
            color_saturation = 1 - self.health / 100

        self.color = ursina.color.color(0, color_saturation, 1)

        if self.health <= 0:
            ursina.destroy(self)


class Zombie(ursina.Entity):
    def __init__(self, position: ursina.Vec3, player):
        super().__init__(
            position=position,
            model="cube",
            origin_y=-0.5,
            collider="box",
            texture="white_cube",
            color=ursina.color.color(0, 0, 1),
            scale=ursina.Vec3(1, 2, 1)
        )

        self.growl = ursina.Audio("zombie_growl")
        self.growl.loop = True
        self.growl.volume = 0.5
        self.growl.play()

        self.name_tag = ursina.Text(
            parent=self,
            text=random.choice(zombie_names),  #Random zombie names
            position=ursina.Vec3(0, 1.3, 0),
            scale=ursina.Vec2(5, 3),
            billboard=True,
            origin=ursina.Vec2(0, 0)
        )

        self.health = 30
        self.player = player
        


    def update(self):

        try:
            color_saturation = 1 - self.health / 30
        except AttributeError:
            self.health = 30
            color_saturation = 1 - self.health / 30

        self.color = ursina.color.color(0, color_saturation, 1)

        
        dist = ursina.distance_xz(self.player.position, self.position)
        if dist > 40:
            pass

        self.look_at_2d(self.player.position, 'y')
        hit_info = ursina.raycast(self.world_position + ursina.Vec3(0,1,0), self.forward, 30, ignore=(self,))
        if hit_info.entity == self.player:
            if dist > 1.5:
                self.position += self.forward * ursina.time.dt * 2
            else:
                self.player.health -= 10
                ursina.Audio("hurt").play()
                self.position += self.forward * ursina.time.dt * -150

        
        if self.health <= 0:
            self.growl.stop()
            ursina.Audio("splat").play()
            ursina.destroy(self)

        
