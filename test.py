import math

bx = -1
by = 1
ax = 0
ay = 0
ang = 90

to_be_angle_dir = math.degrees(math.atan2(bx - ax, by - ay))
if to_be_angle_dir < 0:
    to_be_angle_dir += 360

diff_ang = -(ang - to_be_angle_dir)

print(diff_ang)

if diff_ang > 90:
    diff_ang -= (diff_ang - 90) * 2

print(to_be_angle_dir)

print(diff_ang)