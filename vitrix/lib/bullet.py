import ursina
import os

from lib.enemy import Enemy, Zombie
from lib.paths import GamePaths


class Bullet(ursina.Entity):

    def __init__(self, position: ursina.Vec3, direction: float, x_direction: float, network=False, damage: int = 10, slave=False):
        if network == False:
            self.singleplayer = True
        
        speed = 100
        dir_rad = ursina.math.radians(direction)
        x_dir_rad = ursina.math.radians(x_direction)


        self.velocity = ursina.Vec3(
            ursina.math.sin(dir_rad) * ursina.math.cos(x_dir_rad),
            ursina.math.sin(x_dir_rad),
            ursina.math.cos(dir_rad) * ursina.math.cos(x_dir_rad)
        ) * speed

        #bullet_tags ={
        #    1 : {
        #    "model" :"sphere",
        #    "texture" : "bullet1.png",
        #    "collider" : "sphere",
        #    "double_sided" : False,
        #    "scale" : 0.2
        #    },
        #
        #    2 : {
        #    "model" : os.path.join(Bullet.model_dir,"bullet2"),
        #    "texture" : "bullet2.png",
        #    "collider" : "sphere",
        #    "double_sided" : False,
        #    "scale" : 1.0
        #    }
        #}

        super().__init__(
            position=position + self.velocity / speed,
            model="sphere",
            texture=os.path.join(GamePaths.textures_dir, "bullet.png"),
            collider=b"sphere",
            double_sided=True,
            scale=0.2
            
        )


        self.damage = damage
        self.direction = direction
        self.x_direction = x_direction
        self.slave = slave



    def update(self):
        self.position += self.velocity * ursina.time.dt
        # self.rotation_z+=6
        hit_info = self.intersects()

        if hit_info.hit:
            if not self.slave:
                for entity in hit_info.entities:
                    if isinstance(entity, Enemy) or isinstance(entity, Zombie):
                        entity.health -= self.damage
                        if self.singleplayer == False:
                            self.network.send_health(entity)

            ursina.destroy(self)
