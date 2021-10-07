import random as random

def compute_quadrant(coordinates, grid_size=10):
    #Returns a string with the quadrant the robot is in depending on its coordinates on the grid.
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


def location_message(coordinates, direction, direction_dict={"n": "North", "s": "South", "e": "East", "w": "West"}):
    print(f"I am currently at {coordinates}, facing {direction_dict[direction]}")

def wall_message():
    print("I have a wall in front of me!")
    print("Turning 90 degreed clockwise.")


def read_robot_name():
    """Itroduction to robot program."""
    name = input("What is the name of the robot? ")
    identifier = 1000

    message = f"Hello. My name is {name}. My ID is {identifier}."
    print(message)


def coordinates_func(row, col, grid_size = 10):
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


def navigate(coordinates, direction, target_location=(9,9)):
    """Moves robot one space in the direction specified (or automatically assigned) and returns the
    new coordinates."""

    new_coordinates = coordinates #set new coordinates equal to initia coordinates

    #initialise motion
    motion_in_place = True
    while motion_in_place:
        location_message(new_coordinates, direction)
        #pause motion if location is the same as drink
        if new_coordinates == target_location:
            print("I am drinking Ribena! I am happy!")
            break

        if direction == "n": 
            if new_coordinates[0] == 0:
                direction = "e"
                wall_message()
            else: 
                print("Moving one step forward.")
           
            new_coordinates = coordinates_func(new_coordinates[0]-1, new_coordinates[1])

        elif direction == "s": 

            if new_coordinates[0] == 9:
                direction = "w"
                wall_message()
            else: 
                print("Moving one step forward.")
           
            new_coordinates = coordinates_func(new_coordinates[0]+1, new_coordinates[1])

        elif direction == "e": 

            if new_coordinates[1] == 9:
                direction = "s"
                wall_message()
            else: 
                print("Moving one step forward.")
           
            new_coordinates = coordinates_func(new_coordinates[0], new_coordinates[1]+1)

        elif direction == "w": 

            if new_coordinates[1] == 0:
                direction = "n"
                wall_message()
            else: 
                print("Moving one step forward.")
           

            new_coordinates = coordinates_func(new_coordinates[0], new_coordinates[1]-1)
    

def run_simulation(grid_size=10, target_location=(9,9), direction_dict={"n": "North", "s": "South", "e": "East", "w": "West"}):
    """ Start robot navigation simulation.

    Args:
        grid_size (int): The size of the grid. Defaults to 10.
        target_location (tuple): The target coordinate to reach. Defaults to (9,9).
    """
    read_robot_name() #reas robot name and introduce robot with identifier

    #automated random initial robot coordinates
    row, col = random.randint(0, grid_size), random.randint(0, grid_size)

    #initialise robot coordinates (automated)
    coordinates = coordinates_func(row, col)

    #add random direction and consequent motion
    possible_directions = list(direction_dict.keys())
    direction = possible_directions[random.randint(0,3)]

    #navigate robot to drink
    navigate(coordinates, direction)


if __name__ == "__main__":
    #run simulation
    run_simulation()






