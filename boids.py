"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib import animation
import random


# Deliberately terrible code for teaching purposes

start_x_pos_range = [-450, 50.0]
start_y_pos_range = [300.0, 600.0]
start_x_vel_range = [0, 10.0]
start_y_vel_range = [-20.0, 20.0]
number_boids = 50 

animation_frame_num = 50
animation_time_interval = 50

boids_start_x_pos=[random.uniform(*start_x_pos_range) for x in range(number_boids)]
boids_start_y_pos=[random.uniform(*start_y_pos_range) for x in range(number_boids)]
boid_start_x_velocities=[random.uniform(*start_x_vel_range) for x in range(number_boids)]
boid_start_y_velocities=[random.uniform(*start_y_vel_range) for x in range(number_boids)]
boids=(boids_start_x_pos,boids_start_y_pos,boid_start_x_velocities,boid_start_y_velocities)

def update_boids(boids):
	boids_x_positions,boids_y_positions,boids_x_velocities,boids_y_velocities=boids
	# Fly towards the middle
	for i in range(len(boids_x_positions)):
		for j in range(len(boids_x_positions)):
			boids_x_velocities[i]=boids_x_velocities[i]+(boids_x_positions[j]-boids_x_positions[i])*0.01/len(boids_x_positions)
	for i in range(len(boids_x_positions)):
		for j in range(len(boids_x_positions)):
			boids_y_velocities[i]=boids_y_velocities[i]+(boids_y_positions[j]-boids_y_positions[i])*0.01/len(boids_x_positions)
	# Fly away from nearby boids
	for i in range(len(boids_x_positions)):
		for j in range(len(boids_x_positions)):
			if (boids_x_positions[j]-boids_x_positions[i])**2 + (boids_y_positions[j]-boids_y_positions[i])**2 < 100:
				boids_x_velocities[i]=boids_x_velocities[i]+(boids_x_positions[i]-boids_x_positions[j])
				boids_y_velocities[i]=boids_y_velocities[i]+(boids_y_positions[i]-boids_y_positions[j])
	# Try to match speed with nearby boids
	for i in range(len(boids_x_positions)):
		for j in range(len(boids_x_positions)):
			if (boids_x_positions[j]-boids_x_positions[i])**2 + (boids_y_positions[j]-boids_y_positions[i])**2 < 10000:
				boids_x_velocities[i]=boids_x_velocities[i]+(boids_x_velocities[j]-boids_x_velocities[i])*0.125/len(boids_x_positions)
				boids_y_velocities[i]=boids_y_velocities[i]+(boids_y_velocities[j]-boids_y_velocities[i])*0.125/len(boids_x_positions)
	# Move according to velocities
	for i in range(len(boids_x_positions)):
		boids_x_positions[i]=boids_x_positions[i]+boids_x_velocities[i]
		boids_y_positions[i]=boids_y_positions[i]+boids_y_velocities[i]


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames = animation_frame_num, 
							   interval = animation_time_interval)

if __name__ == "__main__":
    plt.show()