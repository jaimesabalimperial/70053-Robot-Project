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
    with open(file) as names_file:
        names_list = names_file.read().split()
    name = random.choice(names_list)

    return name

def generate_random_direction():
    """Generates a random direction."""
    possible_directions = ["n", "s", "e", "w"]
    random_direction = random.choice(possible_directions)

    return random_direction


def initialise_robot(grid_size, target):
    """Initialises a robot."""
    #define robot traits, create robot object
    name = generate_random_name("robot_names.txt")
    position = make_coordinates_real(random.randint(0, grid_size), random.randint(0, grid_size)) 
    direction = generate_random_direction()

    robot = Robot(name, position, direction, target)
    robot.greet() #introduce robot
    
    return robot

