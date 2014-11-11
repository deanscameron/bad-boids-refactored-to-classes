"""
Implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib import animation
import random
import config
import yaml

config=yaml.load(open("config.yml"))

start_x_pos_range = config['start_x_pos_range']
start_y_pos_range = config['start_y_pos_range']
start_x_vel_range = config['start_x_vel_range']
start_y_vel_range = config['start_y_vel_range']
start_number_boids = config['start_number_boids']

velocity_scale_factor = config['velocity_scale_factor']
velocity_match_scale_factor = config['velocity_match_scale_factor']
nearby_distance = config['nearby_distance']
match_speed_distance = config['match_speed_distance']

#boids_start_x_pos=[random.uniform(*start_x_pos_range) for x in range(start_number_boids)]
#boids_start_y_pos=[random.uniform(*start_y_pos_range) for x in range(start_number_boids)]
#boid_start_x_velocities=[random.uniform(*start_x_vel_range) for x in range(start_number_boids)]
#boid_start_y_velocities=[random.uniform(*start_y_vel_range) for x in range(start_number_boids)]
#boids=(boids_start_x_pos,boids_start_y_pos,boid_start_x_velocities,boid_start_y_velocities)

class boids(object):
    def __init__(self, x_position, y_position, x_velocity, y_velocity):
        self.x_position = x_position
        self.y_position = y_position
		self.x_velocity = x_velocity
		self.y_velocity = y_velocity
	
	def random_boids(self, start_number_boids):
        self.boids = [Boid(random.uniform(*start_x_pos_range),
                random.uniform(*start_y_pos_range),
                random.uniform(*start_x_vel_range),
                random.uniform(*start_y_vel_range),self) for x in range(start_number_boids)]
  
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

    def update_boids(boids):
        boids_x_positions,boids_y_positions,boids_x_velocities,boids_y_velocities = boids
        number_boids = len(boids_x_positions)
	
        fly_towards_middle(boids)
        avoid_nearby_boids(boids)
        match_velocities(boids)
        move_boids(boids)
	

figure = plt.figure()
axes = plt.axes(xlim = config['plot_x_limits'], ylim = config['plot_y_limits'])
scatter = axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames = config['animation_frame_number'], 
							   interval = config['animation_time_interval'])

if __name__ == "__main__":
    plt.show()