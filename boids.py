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
	xs,ys,xvs,yvs=boids
	# Fly towards the middle
	for i in range(len(xs)):
		for j in range(len(xs)):
			xvs[i]=xvs[i]+(xs[j]-xs[i])*0.01/len(xs)
	for i in range(len(xs)):
		for j in range(len(xs)):
			yvs[i]=yvs[i]+(ys[j]-ys[i])*0.01/len(xs)
	# Fly away from nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 100:
				xvs[i]=xvs[i]+(xs[i]-xs[j])
				yvs[i]=yvs[i]+(ys[i]-ys[j])
	# Try to match speed with nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10000:
				xvs[i]=xvs[i]+(xvs[j]-xvs[i])*0.125/len(xs)
				yvs[i]=yvs[i]+(yvs[j]-yvs[i])*0.125/len(xs)
	# Move according to velocities
	for i in range(len(xs)):
		xs[i]=xs[i]+xvs[i]
		ys[i]=ys[i]+yvs[i]


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames = animation_frame_num, interval = animation_time_interval)

if __name__ == "__main__":
    plt.show()