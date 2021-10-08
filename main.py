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


def read_robot_names(n_robots):
    """Introduction to robot program."""
    #read random robot names from .txt files
    names_list = open("robot_names.txt").read().split()
    robot_names = [random.choice(names_list) for i in range(n_robots)]
    identifiers_list = [1000+i for i in range(1,n_robots+1)]

    messages_list = [f"Hello. My name is {name}. My ID is {identifier}." for name,identifier in zip(robot_names,identifiers_list)]
    
    #print out introductory messages for each robot
    for message in messages_list:
        print(message)

    return robot_names


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

    return [row,col]


def navigate(robot_names, initial_coordinates_list, directions_list, target_locations=[(9,9), (0,9), (9,0), (0,0)]):
    """Moves robot one space in the direction specified (or automatically assigned) and returns the
    new coordinates."""
    for i, robot in enumerate(robot_names):
        print(f"\n{robot} is searching for its drink.")
        new_coordinates = initial_coordinates_list[i] #set new coordinates equal to initia coordinates

        #initialise motion
        motion_in_place = True
        while motion_in_place:
            location_message(new_coordinates, directions_list[i])
            #pause motion if location is the same as drink
            if tuple(new_coordinates) == target_locations[i]:
                print("I am drinking Ribena! I am happy!")
                break

            if directions_list[i] == "n": 
                if new_coordinates[0] == 0:
                    directions_list[i] = "e"
                    wall_message()
                else: 
                    print("Moving one step forward.")
            
                new_coordinates = coordinates_func(new_coordinates[0]-1, new_coordinates[1])

            elif directions_list[i] == "s": 

                if new_coordinates[0] == 9:
                    directions_list[i] = "w"
                    wall_message()
                else: 
                    print("Moving one step forward.")
            
                new_coordinates = coordinates_func(new_coordinates[0]+1, new_coordinates[1])

            elif directions_list[i] == "e": 

                if new_coordinates[1] == 9:
                    directions_list[i] = "s"
                    wall_message()
                else: 
                    print("Moving one step forward.")
            
                new_coordinates = coordinates_func(new_coordinates[0], new_coordinates[1]+1)

            elif directions_list[i] == "w": 

                if new_coordinates[1] == 0:
                    directions_list[i] = "n"
                    wall_message()
                else: 
                    print("Moving one step forward.")
            

                new_coordinates = coordinates_func(new_coordinates[0], new_coordinates[1]-1)
        

def run_simulation(n_robots, grid_size=10, target_location=(9,9), direction_dict={"n": "North", "s": "South", "e": "East", "w": "West"}):
    """ Start robot navigation simulation.

    Args:
        grid_size (int): The size of the grid. Defaults to 10.
        target_location (tuple): The target coordinate to reach. Defaults to (9,9).
    """
    assert n_robots <=4, "Maximum number of robots is 4."

    robot_names = read_robot_names(n_robots) #reas robot name and introduce robot with identifier

    #automated random initial robot coordinates
    initial_coordinates = [coordinates_func(random.randint(0, grid_size), random.randint(0, grid_size))]*n_robots

    #add random direction and consequent motion
    possible_directions = list(direction_dict.keys())
    directions_list = [possible_directions[random.randint(0,3)]]*n_robots

    #navigate robot to drink
    navigate(robot_names, initial_coordinates, directions_list)


if __name__ == "__main__":
    #run simulation
    run_simulation(n_robots=4)






