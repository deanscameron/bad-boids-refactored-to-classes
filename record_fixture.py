import yaml
import boids
from copy import deepcopy
from boids_functions import fly_towards_middle, avoid_nearby_boids, move_boids, match_velocities

#before=deepcopy(boids.boids)
#boids.update_boids(boids.boids)
#after=boids.boids
#fixture={"before":before,"after":after}
#fixture_file=open("fixture.yml",'w')
#fixture_file.write(yaml.dump(fixture))
#fixture_file.close()

#before=deepcopy(boids.boids)
#fly_towards_middle(boids.boids)
#after=boids.boids
#fixture={"before":before,"after":after}
#fixture_file=open("fly_towards_middle.yml",'w')
#fixture_file.write(yaml.dump(fixture))
#fixture_file.close()

#before=deepcopy(boids.boids)
#avoid_nearby_boids(boids.boids)
#after=boids.boids
#fixture={"before":before,"after":after}
#fixture_file=open("avoid_nearby_boids.yml",'w')
#fixture_file.write(yaml.dump(fixture))
#fixture_file.close()

before=deepcopy(boids.boids)
match_velocities(boids.boids)
after=boids.boids
fixture={"before":before,"after":after}
fixture_file=open("match_velocities.yml",'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()
