import random as random
from robot import Robot
from robot_init import initialise_robot

def run_simulation(n_robots,
                   grid_size=10):
    """ Start robot navigation simulation.

    Args:
        n_robots (int): Number of robots in grid.
        grid_size (int): The size of the grid. Defaults to 10.
    """
    assert n_robots <= 4, "Maximum number of robots is 4 (since there are only four target locations)."

    #define possible target locations
    target_locations=[(grid_size-1, grid_size-1), (0, grid_size-1), (grid_size-1, 0), (0, 0)] 

    robots_list = []
    # record traits in dictionary
    for i in range(n_robots):
        robot = initialise_robot(grid_size, target_locations[i])
        robots_list.append(robot)

    #navigate robots in another loop so they all introduce themselves before navigating
    for i in range(n_robots):
        robots_list[i].navigate()


if __name__ == "__main__":
    # run simulation
    run_simulation(n_robots=4)
