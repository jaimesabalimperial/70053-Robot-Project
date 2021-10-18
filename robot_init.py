import random as random
from robot import Robot

class RobotInitialiser():
    with open("robot_names.txt") as names_file:
        robot_names = names_file.read().split()
    
    def __init__(self, names = robot_names, grid_size = 10):
        self.names = names 
        self.grid_size = grid_size
        self.targets = [(self.grid_size-1, self.grid_size-1), (0, self.grid_size-1), (self.grid_size-1, 0), (0, 0)]
        self.robots = []
        

    def generate_name(self): 
        """Generates a random name from a file that has names."""
        #read names from list

        name = random.choice(self.names)

        return name

    def generate_direction(self):
        """Generates a random direction."""
        possible_directions = ["n", "s", "e", "w"]
        random_direction = random.choice(possible_directions)

        return random_direction


    def create_robots(self, n_robots):
        """Initialises a sequence of robots."""

        for i in range(n_robots):
            #define robot traits, create robot object 
            name = self.generate_name()
            position = (random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)) 
            direction = self.generate_direction()

            robot = Robot(name, position, direction, self.targets[i])
            robot.greet() #introduce robot
            self.robots.append(robot) #append new robot to list


        

