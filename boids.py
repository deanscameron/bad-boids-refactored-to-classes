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
from boids_functions import fly_towards_middle, avoid_nearby_boids, move_boids, match_velocities

config=yaml.load(open("config.yml"))

start_x_pos_range = config['start_x_pos_range']
start_y_pos_range = config['start_y_pos_range']
start_x_vel_range = config['start_x_vel_range']
start_y_vel_range = config['start_y_vel_range']
start_number_boids = config['start_number_boids']


boids_start_x_pos=[random.uniform(*start_x_pos_range) for x in range(start_number_boids)]
boids_start_y_pos=[random.uniform(*start_y_pos_range) for x in range(start_number_boids)]
boid_start_x_velocities=[random.uniform(*start_x_vel_range) for x in range(start_number_boids)]
boid_start_y_velocities=[random.uniform(*start_y_vel_range) for x in range(start_number_boids)]
boids=(boids_start_x_pos,boids_start_y_pos,boid_start_x_velocities,boid_start_y_velocities)

			
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