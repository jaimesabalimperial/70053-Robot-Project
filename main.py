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


def generate_random_name(file): 
    """Generates a random name from a file that has names."""
    #read names from list
    names_list = open(file).read().split()
    name = random.choice(names_list)

    return name


def generate_random_direction():
    """Generates a random direction."""
    possible_directions = ["n", "s", "e", "w"]
    random_direction = random.choice(possible_directions)

    return random_direction


def run_simulation(n_robots,
                   grid_size=10):
    """ Start robot navigation simulation.

    Args:
        n_robots (int): Number of robots in grid.
        grid_size (int): The size of the grid. Defaults to 10.
    """
    assert n_robots <= 4, "Maximum number of robots is 4 (since there are only four target locations)."

    #generate random name
    robot_names = [generate_random_name("robot_names.txt") for i in range(n_robots)]

    #define target locations
    target_locations=[(grid_size-1, grid_size-1), (0, grid_size-1), (grid_size-1, 0), (0, 0)] 

    robots_list = []
    # record traits in dictionary
    for i in range(n_robots):

        #define robot traits, create robot object
        name = robot_names[i]
        position = make_coordinates_real(random.randint(0, grid_size), random.randint(0, grid_size)) 
        direction = generate_random_direction()
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
