"""
Implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib import animation
import random
from math import hypot
import config

start_x_pos_range = [-450, 50.0]
start_y_pos_range = [300.0, 600.0]
start_x_vel_range = [0, 10.0]
start_y_vel_range = [-20.0, 20.0]
start_number_boids = 50 

animation_frame_number = 50
animation_time_interval = 50

nearby_distance = 10
match_speed_distance = 100

velocity_scale_factor = 0.01
velocity_match_scale_factor = 0.125

plot_x_limits = [-500, 1500]
plot_y_limits = [-500, 1500]


boids_start_x_pos=[random.uniform(*start_x_pos_range) for x in range(start_number_boids)]
boids_start_y_pos=[random.uniform(*start_y_pos_range) for x in range(start_number_boids)]
boid_start_x_velocities=[random.uniform(*start_x_vel_range) for x in range(start_number_boids)]
boid_start_y_velocities=[random.uniform(*start_y_vel_range) for x in range(start_number_boids)]
boids=(boids_start_x_pos,boids_start_y_pos,boid_start_x_velocities,boid_start_y_velocities)


def distance(position_1, position_2):
    return hypot(position_1, position_2)

def update_velocity(position_1, position_2, scale_factor):
    velocity_step = (position_2 - position_1)*scale_factor
    return velocity_step

def distance_check(x_position_1, x_position_2, y_position_1, y_position_2, range)
    if distance((x_position_2 - x_position_1), (y_position_2 - y_position_1)) < range
	    return True
	
def update_boids(boids):
	boids_x_positions,boids_y_positions,boids_x_velocities,boids_y_velocities = boids
	number_boids = len(boids_x_positions)
	
	# Fly towards the middle
	for i in range(number_boids):
		for j in range(number_boids):
			boids_x_velocities[i] += update_velocity(boids_x_positions[i], boids_x_positions[j], (velocity_scale_factor/number_boids))
	for i in range(number_boids):
		for j in range(number_boids):
			boids_y_velocities[i] += update_velocity(boids_y_positions[i], boids_y_positions[j], (velocity_scale_factor/number_boids)
	
	# Fly away from nearby boids
	for i in range(number_boids):
		for j in range(number_boids):
			if distance_check(boids_x_positions[i], boids_x_positions[j], boids_y_positions[i], boids_y_positions[j], nearby_distance):
				boids_x_velocities[i] += update_velocity(boids_x_positions[j], boids_x_positions[i], 1)
				boids_y_velocities[i] += update_velocity(boids_y_positions[j], boids_y_positions[i], 1) 
	
	# Try to match speed with nearby boids
	for i in range(number_boids):
		for j in range(number_boids):
			if distance_check(boids_x_positions[i], boids_x_positions[j], boids_y_positions[i], boids_y_positions[j], match_speed_distance):
				boids_x_velocities[i] += update_velocity(boids_x_velocities[i], boids_x_velocities[j], (velocity_match_scale_factor/number_boids))
				boids_y_velocities[i] += update_velocity(boids_y_velocities[i], boids_y_velocities[j], (velocity_match_scale_factor/number_boids))
	
	# Move according to velocities
	for i in range(len(boids_x_positions)):
		boids_x_positions[i] += boids_x_velocities[i]
		boids_y_positions[i] += boids_y_velocities[i]


figure = plt.figure()
axes = plt.axes(xlim = plot_x_limits, ylim = plot_y_limits)
scatter = axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames = animation_frame_number, 
							   interval = animation_time_interval)

if __name__ == "__main__":
    plt.show()