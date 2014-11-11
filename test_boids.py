from boids import update_boids
from boids_functions import distance
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

			
def test_distance():
    assert_equal(distance(3,4),5)
    assert_almost_equal(distance(-1,1), 1.41, delta=0.01)