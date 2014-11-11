"""File containing the boids functions"""

import config
import yaml
from math import hypot

config=yaml.load(open("config.yml"))

velocity_scale_factor = config['velocity_scale_factor']
velocity_match_scale_factor = config['velocity_match_scale_factor']
nearby_distance = config['nearby_distance']
match_speed_distance = config['match_speed_distance']

def distance(position_1, position_2):
    return hypot(position_1, position_2)

def update_velocity(position_1, position_2, scale_factor):
    velocity_step = (position_2 - position_1)*scale_factor
    return velocity_step

def distance_check(x_position_1, x_position_2, y_position_1, y_position_2, range):
    if distance((x_position_2 - x_position_1), (y_position_2 - y_position_1)) < range:
	    return True

def fly_towards_middle(boids):
	boids_x_positions,boids_y_positions,boids_x_velocities,boids_y_velocities = boids
	number_boids = len(boids_x_positions)
	# Update the velocities of boids such that they fly towards the centre of the flock
	for i in range(number_boids):
		for j in range(number_boids):
			boids_x_velocities[i] += update_velocity(boids_x_positions[i], boids_x_positions[j], (velocity_scale_factor/number_boids))
			boids_y_velocities[i] += update_velocity(boids_y_positions[i], boids_y_positions[j], (velocity_scale_factor/number_boids))

def avoid_nearby_boids(boids):
	boids_x_positions,boids_y_positions,boids_x_velocities,boids_y_velocities = boids
	number_boids = len(boids_x_positions)	
    # Update the velocities of boids such that they fly away from nearby birds in the flock
	for i in range(number_boids):
		for j in range(number_boids):
			if distance_check(boids_x_positions[i], boids_x_positions[j], boids_y_positions[i], boids_y_positions[j], nearby_distance):
				boids_x_velocities[i] += update_velocity(boids_x_positions[j], boids_x_positions[i], 1)
				boids_y_velocities[i] += update_velocity(boids_y_positions[j], boids_y_positions[i], 1)

def match_velocities(boids):
	boids_x_positions,boids_y_positions,boids_x_velocities,boids_y_velocities = boids
	number_boids = len(boids_x_positions)		
    # Update the velocities of boids such that they fly at the same speed as the rest of the flock
	for i in range(number_boids):
		for j in range(number_boids):
			if distance_check(boids_x_positions[i], boids_x_positions[j], boids_y_positions[i], boids_y_positions[j], match_speed_distance):
				boids_x_velocities[i] += update_velocity(boids_x_velocities[i], boids_x_velocities[j], (velocity_match_scale_factor/number_boids))
				boids_y_velocities[i] += update_velocity(boids_y_velocities[i], boids_y_velocities[j], (velocity_match_scale_factor/number_boids))	

def move_boids(boids):
	boids_x_positions,boids_y_positions,boids_x_velocities,boids_y_velocities = boids
	number_boids = len(boids_x_positions)
	# Boids fly according to their velocities
	for i in range(number_boids):
		boids_x_positions[i] += boids_x_velocities[i]
		boids_y_positions[i] += boids_y_velocities[i]