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


def motion(coordinates, direction):
    """Moves robot one space in the direction specified (or automatically assigned) and returns the
    new coordinates."""
    direction_string = ""
    new_coordinates = coordinates
    direction_dict = {"n": "North", "s": "South", "e": "East", "w": "West"}

    motion_in_place = True
    while motion_in_place:
        print(f"I am currently at {new_coordinates}, facing {direction_dict[direction]}")

        if direction == "n": 
            if new_coordinates[0] == 0:
                print("I have a wall in front of me!")
                print("Turning 90 degreed clockwise.")
                direction = "e"
                print(f"I am currently at {new_coordinates}, facing {direction_dict[direction]}")
                break
            else: 
                print("Moving one step forward.")
           
            new_coordinates = coordinates_func(new_coordinates[0]-1, new_coordinates[1])

        elif direction == "s": 

            if new_coordinates[0] == 9:
                print("I have a wall in front of me!")
                print("Turning 90 degreed clockwise.")
                direction = "w"
                print(f"I am currently at {new_coordinates}, facing {direction_dict[direction]}")
                break
            else: 
                print("Moving one step forward.")
           
            new_coordinates = coordinates_func(new_coordinates[0]+1, new_coordinates[1])

        elif direction == "e": 

            if new_coordinates[1] == 9:
                print("I have a wall in front of me!")
                print("Turning 90 degreed clockwise.")
                direction = "s"
                print(f"I am currently at {new_coordinates}, facing {direction_dict[direction]}")
                break
            else: 
                print("Moving one step forward.")
           
            new_coordinates = coordinates_func(new_coordinates[0], new_coordinates[1]+1)

        elif direction == "w": 

            if new_coordinates[1] == 0:
                print("I have a wall in front of me!")
                print("Turning 90 degreed clockwise.")
                direction = "n"
                print(f"I am currently at {new_coordinates}, facing {direction_dict[direction]}")
                break
            else: 
                print("Moving one step forward.")
           

            new_coordinates = coordinates_func(new_coordinates[0], new_coordinates[1]-1)
    
    return new_coordinates

if __name__ == "__main__":
    intro()

    #user inputs for initial robot coordinate
    row, col = random.randint(0, grid_size), random.randint(0, grid_size)

    #initialise robot
    coordinates = coordinates_func(row, col)

    #add direction and motion components
    possible_directions = ["n", "s", "e", "w"]
    direction = possible_directions[random.randint(0,3)]
    new_coordinates = motion(coordinates, direction)






