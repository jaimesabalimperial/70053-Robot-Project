import random as random
from robot import Robot, coordinates_func

def run_simulation(n_robots,
                   grid_size=10,
                   direction_dict={"n": "North", "s": "South",
                                   "e": "East", "w": "West"},
                   target_locations=[(9, 9), (0, 9), (9, 0), (0, 0)]):
    """ Start robot navigation simulation.

    Args:
        grid_size (int): The size of the grid. Defaults to 10.
        target_location (tuple): The target coordinate to reach. Defaults to (9,9).
    """
    assert n_robots <= 4, "Maximum number of robots is 4 (since there are only four target locations)."

    #read robot name and introduce robot with identifier
    names_list = open("robot_names.txt").read().split()
    robot_names = [random.choice(names_list) for i in range(n_robots)]

    robots_list = []
    # record traits in dictionary
    for i in range(n_robots):

        #define robot traits, create robot object
        name = robot_names[i]
        position = coordinates_func(random.randint(0, grid_size), random.randint(0, grid_size)) 
        direction = list(direction_dict)[random.randint(0, 3)] 
        target = target_locations[i]

        robot = Robot(name, position, direction, target)
        robots_list.append(robot)

    # navigate robots in another loop so they all introduce themselves before navigating
    for i in range(n_robots):
        robots_list[i].navigate()


if __name__ == "__main__":
    # run simulation
    run_simulation(n_robots=4)
