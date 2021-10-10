import random as random
from robot import Robot

def make_coordinates_real(row, col, grid_size=10):
    """Considers limit cases for when row and column numbers arent within the grid (i.e >grid_size or <0)."""
    # consider limit cases
    if row < 0:
        row = 0
    elif row >= grid_size:
        row = grid_size - 1

    if col < 0:
        col = 0
    elif col >= grid_size:
        col = grid_size - 1

    return [row, col]

def run_simulation(n_robots,
                   grid_size=10,
                   direction_dict={"n": "North", "s": "South",
                                   "e": "East", "w": "West"}):
    """ Start robot navigation simulation.

    Args:
        grid_size (int): The size of the grid. Defaults to 10.
        target_location (tuple): The target coordinate to reach. Defaults to (9,9).
    """
    assert n_robots <= 4, "Maximum number of robots is 4 (since there are only four target locations)."

    #read robot name and introduce robot with identifier
    names_list = open("robot_names.txt").read().split()
    robot_names = [random.choice(names_list) for i in range(n_robots)]

    target_locations=[(grid_size-1, grid_size-1), (0, grid_size-1), (grid_size-1, 0), (0, 0)]

    robots_list = []
    # record traits in dictionary
    for i in range(n_robots):

        #define robot traits, create robot object
        name = robot_names[i]
        position = make_coordinates_real(random.randint(0, grid_size), random.randint(0, grid_size)) 
        direction = list(direction_dict)[random.randint(0, 3)] 
        target = target_locations[i]

        robot = Robot(name, position, direction, target)
        robot.greet() #introduce robot

        robots_list.append(robot)

    # navigate robots in another loop so they all introduce themselves before navigating
    for i in range(n_robots):
        robots_list[i].navigate()


if __name__ == "__main__":
    # run simulation
    run_simulation(n_robots=4)
