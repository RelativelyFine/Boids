import math
import arcade
import random

START_SPEED = 2
MAX_SPEED = 3


class Boid(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)
        self.speed = 5
        self.acceleration = 0.5
        self.boundary_top = 1080
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 1920
        self.max_speed = 10

    def update(self, time):
        self.speed = START_SPEED + self.acceleration * (
            (MAX_SPEED) /
            (1 + math.exp(-time + 5))) - (self.change_angle / MAX_SPEED)

        angle_rad = -math.radians(self.angle)

        self.angle += self.change_angle

        if self.center_x < self.boundary_left or self.center_x > self.boundary_right:
            self.center_x = 1920 if (
                self.center_x + self.speed * math.sin(angle_rad)) < 0 else 0
        else:
            self.center_x += self.speed * math.sin(angle_rad)

        if self.center_y > self.boundary_top or self.center_y < self.boundary_bottom:
            self.center_y = 1080 if (
                self.center_y + self.speed * math.cos(angle_rad)) < 0 else 0
        else:
            self.center_y += self.speed * math.cos(angle_rad)
