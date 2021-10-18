import random as random
from robot import Robot
from robot_init import RobotInitialiser

def run_simulation(n_robots,
                   grid_size=10):
    """ Start robot navigation simulation.

    Args:
        n_robots (int): Number of robots in grid.
        grid_size (int): The size of the grid. Defaults to 10.
    """
    assert n_robots <= 4, "Maximum number of robots is 4 (since there are only four target locations)."

    #create robots
    initialiser = RobotInitialiser()
    initialiser.create_robots(n_robots)

    #navigate robots in another loop so they all introduce themselves before navigating
    for i in range(n_robots):
        initialiser.robots[i].navigate()


if __name__ == "__main__":
    # run simulation
    run_simulation(n_robots=4)
