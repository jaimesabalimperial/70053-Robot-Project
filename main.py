import random as random
#define size of grid in which robot can move in
grid_size = 10

def intro():
    """Itroduction to robot program."""
    name = input("What is the name of the robot? ")
    identifier = 1000

    message = f"Hello. My name is {name}. My ID is {identifier}."
    print(message)

def coordinates_func(row, col):
    """Considers limit cases for when row and column numbers arent within the grid (i.e >grid_size or <0)."""
    #consider limit cases
    if row < 0: 
        row = 0
    elif row >= grid_size: 
        row = grid_size - 1

    if col < 0: 
        col = 0
    elif col >= grid_size: 
        col = grid_size - 1

    return (row,col)

def quadrant(coordinates, grid_len=grid_size):
    """Returns a string with the quadrant the robot is in depending on its coordinates on the grid."""
    quadrant_str = ""
    if coordinates[0] < grid_size/2 and coordinates[1] >= grid_size/2: 
        quadrant_str = "top right"
    elif coordinates[0] >= grid_size/2 and coordinates[1] >= grid_size/2: 
        quadrant_str = "bottom right"
    elif coordinates[0] >= grid_size/2 and coordinates[1] < grid_size/2: 
        quadrant_str = "bottom left"
    elif coordinates[0] < grid_size/2 and coordinates[1] <= grid_size/2: 
        quadrant_str = "top left"
    else:
        quadrant_str = "center"

    return quadrant_str

def coordinate_message(coordinates, quadrant):
    """Prints message containing coordinate and quadrant information."""
    print(f"My current location is {coordinates}. I am in the {quadrant} quadrant.")

def motion(coordinates, direction):
    """Moves robot one space in the direction specified (or automatically assigned) and returns the
    new coordinates."""
    direction_string = ""
    new_coordinates = ()

    if direction == "n": 
        direction_string = "North"
        new_coordinates = coordinates_func(coordinates[0]-1, coordinates[1])
    if direction == "s": 
        direction_string = "South"
        new_coordinates = coordinates_func(coordinates[0]+1, coordinates[1])
    if direction == "e": 
        direction_string = "East"
        new_coordinates = coordinates_func(coordinates[0], coordinates[1]+1)
    if direction == "w": 
        direction_string = "West"
        new_coordinates = coordinates_func(coordinates[0], coordinates[1]-1)
    
    print(f"I am facing {direction_string}")
    print("Moving one step forward.")
        
    return new_coordinates

intro()

#user inputs for initial robot coordinate
row, col = random.randint(0, grid_size), random.randint(0, grid_size)

#initialise robot
coordinates = coordinates_func(row, col)
initial_quadrant = quadrant(coordinates)
coordinate_message(coordinates, initial_quadrant)

#add direction and motion components
possible_directions = ["n", "s", "e", "w"]
direction = possible_directions[random.randint(0,3)]
new_coordinates = motion(coordinates, direction)
new_quadrant = quadrant(new_coordinates)
coordinate_message(new_coordinates, new_quadrant)






