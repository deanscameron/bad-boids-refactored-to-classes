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
from boids_functions import distance, update_velocity, distance_check

config=yaml.load(open("config.yml"))


class Boid(object):
    def __init__(self, x_position, y_position, x_velocity, y_velocity):
        self.x_position = x_position
        self.y_position = y_position
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        
class Boids(object):
    def __init__(self, num_boids=config['number_boids'], 
	                start_x_pos_range = config['start_x_pos_range'], 
	                start_y_pos_range = config['start_y_pos_range'],
					start_x_vel_range = config['start_x_vel_range'],
					start_y_vel_range = config['start_y_vel_range'],
					velocity_scale_factor = config['velocity_scale_factor'],
					velocity_match_scale_factor = config['velocity_match_scale_factor'],
					nearby_distance = config['nearby_distance'],
					match_speed_distance = config['match_speed_distance']):
	    self.num_boids = num_boids
	    self.start_x_pos_range = start_x_pos_range
	    self.start_y_pos_range = start_y_pos_range
	    self.start_x_vel_range = start_x_vel_range
	    self.start_y_vel_range = start_y_vel_range
	    self.velocity_scale_factor = velocity_scale_factor
	    self.velocity_match_scale_factor = velocity_match_scale_factor
	    self.nearby_distance = nearby_distance
	    self.match_speed_distance = match_speed_distance
	    self.random_boids()

    def random_boids(self):
        self.boids = [Boid(random.uniform(*self.start_x_pos_range),
                random.uniform(*self.start_y_pos_range),
                random.uniform(*self.start_x_vel_range),
                random.uniform(*self.start_y_vel_range)) for x in range(self.num_boids)]
		
    def fly_towards_middle(self):
        # Update the velocities of boids such that they fly towards the centre of the flock
        for boid_1 in self.boids:
            for boid_2 in self.boids:
                boid_1.x_velocity += update_velocity(boid_1.x_position, boid_2.x_position, (self.velocity_scale_factor/self.num_boids))
                boid_1.y_velocity += update_velocity(boid_1.y_position, boid_2.y_position, (self.velocity_scale_factor/self.num_boids))

    def avoid_nearby_boids(self):   
        # Update the velocities of boids such that they fly away from nearby birds in the flock
        for boid_1 in self.boids:
            for boid_2 in self.boids:
                if distance_check(boid_1.x_position, boid_2.x_position, boid_1.y_position, boid_2.y_position, self.nearby_distance):
                    boid_1.x_velocity += update_velocity(boid_2.x_position, boid_1.x_position, 1)
                    boid_1.y_velocity += update_velocity(boid_2.y_position, boid_1.y_position, 1)

    def match_velocities(self):
        # Update the velocities of boids such that they fly at the same speed as the rest of the flock
        for boid_1 in self.boids:
            for boid_2 in self.boids:
                if distance_check(boid_1.x_position, boid_2.x_position, boid_1.y_position, boid_2.y_position, self.match_speed_distance):
                    boid_1.x_velocity += update_velocity(boid_1.x_velocity, boid_2.x_velocity, (self.velocity_match_scale_factor/self.num_boids))
                    boid_1.y_velocity += update_velocity(boid_1.y_velocity, boid_2.y_velocity, (self.velocity_match_scale_factor/self.num_boids))  

    def move_boids(self):
        # Boids fly according to their velocities
        for boid_1 in self.boids:
            boid_1.x_position += boid_1.x_velocity
            boid_1.y_position += boid_1.y_velocity

    def update_boids(self):
        self.fly_towards_middle()
        self.avoid_nearby_boids()
        self.match_velocities()
        self.move_boids()
    
    def boids_x_vector(self):
        v = []
        for boid_1 in self.boids:
            v.append(boid_1.x_position)
        return v
            
    def boids_y_vector(self):
        v = []
        for boid_1 in self.boids:
            v.append(boid_1.y_position)
        return v
    
    
boids = Boids()

figure = plt.figure()
axes = plt.axes(xlim = config['plot_x_limits'], ylim = config['plot_y_limits'])
scatter = axes.scatter(boids.boids_x_vector(), boids.boids_y_vector())

def animate(frame):
   boids.update_boids()
   scatter.set_offsets(zip(boids.boids_x_vector(), boids.boids_y_vector()))


anim = animation.FuncAnimation(figure, animate,
                               frames = config['animation_frame_number'], 
                               interval = config['animation_time_interval'])

if __name__ == "__main__":
    plt.show()