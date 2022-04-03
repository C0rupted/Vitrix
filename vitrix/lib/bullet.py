import random
from numpy import singlecomplex
import ursina
import os

from lib.enemy import Enemy


class Bullet(ursina.Entity):
    def __init__(self, position: ursina.Vec3, direction: float, x_direction: float, network=False, damage: int = random.randint(5, 20), slave=False):
        if network == False:
            self.singleplayer = True
        
        speed = 35
        dir_rad = ursina.math.radians(direction)
        x_dir_rad = ursina.math.radians(x_direction)


        self.velocity = ursina.Vec3(
            ursina.math.sin(dir_rad) * ursina.math.cos(x_dir_rad),
            ursina.math.sin(x_dir_rad),
            ursina.math.cos(dir_rad) * ursina.math.cos(x_dir_rad)
        ) * speed


        super().__init__(
            position=position + self.velocity / speed,
            model="cube",
            texture=os.path.join("assets", "bullet.png"),
            collider="box",
            scale=0.2
        )


        self.damage = damage
        self.direction = direction
        self.x_direction = x_direction
        self.slave = slave
        if self.singleplayer == False:
            self.network = network


    def update(self):
        self.position += self.velocity * ursina.time.dt
        hit_info = self.intersects()

        if hit_info.hit:
            if not self.slave:
                for entity in hit_info.entities:
                    if isinstance(entity, Enemy):
                        entity.health -= self.damage
                        if self.singleplayer == False:
                            self.network.send_health(entity)

            ursina.destroy(self)
