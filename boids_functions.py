"""File containing the boids functions"""

from math import hypot

def distance(position_1, position_2):
    return hypot(position_1, position_2)

def update_vel(position_1, position_2, scale_factor):
    velocity_step = (position_2 - position_1)*scale_factor
    return velocity_step

def dist_check(x_position_1, x_position_2, y_position_1, y_position_2, range):
    if distance((x_position_2 - x_position_1), (y_position_2 - y_position_1)) < range:
	    return True