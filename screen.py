import arcade
import boid
import math
import random

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Boids!"
VISION_RANGE = 100
BOIDS_NUM = 200
ALIGNMENT = 4
SPRITE_SCALING = 0.02
COHESION = 5
SEPARATION = 1
PERSONAL_SPACE = 10


class Screener(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.timey = 0
        # Separate variable that holds the player sprite
        self.boid_list = None

        self.physics_engine = None

        arcade.set_background_color((51, 54, 64))

    def setup(self):

        self.boid_list = arcade.SpriteList()

        # Set up the player
        for i in range(BOIDS_NUM):
            self.boid_sprite = boid.Boid(r"./sprites/point.png",
                                         SPRITE_SCALING)
            self.boid_sprite.angle = random.randrange(0, 360)
            self.boid_sprite.center_x = random.randint(0, SCREEN_WIDTH)
            self.boid_sprite.center_y = random.randint(0, SCREEN_HEIGHT)
            self.boid_list.append(self.boid_sprite)

    def on_draw(self):
        arcade.start_render()
        self.boid_list.draw()

    def on_update(self, delta_time):
        for b1 in self.boid_list:
            tot_ang = 0
            tot_pos_x = 0
            tot_pos_y = 0
            num = 0
            for b2 in self.boid_list:
                if math.sqrt((b1.center_x - b2.center_x)**2 +
                             (b1.center_y - b2.center_y)**2) < VISION_RANGE:
                    tot_ang += b2.angle
                    tot_pos_x += b2.center_x
                    tot_pos_y += b2.center_y
                    num += 1

            to_be_angle = (tot_ang / num) % 360
            now_delta = (to_be_angle - b1.angle) * delta_time * ALIGNMENT
            b1.angle += now_delta

            tot_pos_x_avg = (tot_pos_x / num)
            tot_pos_y_avg = (tot_pos_y / num)

            to_be_angle_dir = math.degrees(
                math.atan2(tot_pos_x_avg - b1.center_x,
                           tot_pos_y_avg - b1.center_y))
            if to_be_angle_dir < 0:
                to_be_angle_dir += 360

            diff_ang = -(b1.angle - to_be_angle_dir)

            if diff_ang > 90:
                b1.speed -= 0.1 * delta_time
                diff_ang -= (diff_ang - 90) * 2
            else:
                b1.speed += 0.1 * delta_time

            b1.angle += diff_ang * delta_time * COHESION

        self.timey += delta_time
        for i in self.boid_list:
            i.update(self.timey)


def main():
    window = Screener()
    window.setup()
    window.run()


if __name__ == "__main__":
    main()