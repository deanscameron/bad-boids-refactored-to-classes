from boids import update_boids
from boids_functions import distance, update_velocity, distance_check
from boids_functions import fly_towards_middle, avoid_nearby_boids, move_boids, match_velocities
from nose.tools import assert_almost_equal, assert_equal
import os
import yaml

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boid_data=regression_data["before"]
    update_boids(boid_data)
    for after,before in zip(regression_data["after"],boid_data):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)

def test_fly_towards_middle():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fly_towards_middle.yml')))
    boid_data=regression_data["before"]
    fly_towards_middle(boid_data)
    for after,before in zip(regression_data["after"],boid_data):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)

def test_avoid_nearby_birds():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'avoid_nearby_boids.yml')))
    boid_data=regression_data["before"]
    avoid_nearby_boids(boid_data)
    for after,before in zip(regression_data["after"],boid_data):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)
			
def test_match_velocities():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'match_velocities.yml')))
    boid_data=regression_data["before"]
    match_velocities(boid_data)
    for after,before in zip(regression_data["after"],boid_data):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)
			
def test_move_boids():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'move_boids.yml')))
    boid_data=regression_data["before"]
    move_boids(boid_data)
    for after,before in zip(regression_data["after"],boid_data):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)
			
def test_distance():
    assert_equal(distance(3,4),5)
    assert_almost_equal(distance(-1,1), 1.41, delta=0.01)
	
def test_update_velocity():
    assert_equal(update_velocity(5, 10, 1), 5)
    assert_equal(update_velocity(5, -5, 0.1), -1)
	
def test_distance_check():
    assert distance_check(1, 4, 6, 10, 5.001)

