import random as random
import itertools 

def coordinates_func(row, col, grid_size=10):
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


def location_message(position, direction, direction_dict={"n": "North", "s": "South", "e": "East", "w": "West"}):
    print(f"I am currently at {position}, facing {direction_dict[direction]}")


def wall_message():
    print("I have a wall in front of me!")
    print("Turning 90 degreed clockwise.")

class Robot():
    #generate new id for each Robot instance
    newid = itertools.count()

    def __init__(self, name, position, direction, target):
        self.name = name 
        self.id = 1000 + next(self.newid)
        self.position = position
        self.direction = direction
        self.target = target

        print(f"Hello. My name is {self.name}. My ID is {self.id}.")

    def navigate(self):
        """Navigates robot across grid until it reaches its target location."""

        print(f"\n{self.name} is searching for its drink.")

        # set new coordinates equal to initial coordinates
        new_coordinates = self.position

        # initialise motion
        motion_in_place = True
        while motion_in_place:
            location_message(new_coordinates, self.direction)
            # pause motion if location is the same as drink
            if tuple(new_coordinates) == self.target:
                print("I am drinking Ribena! I am happy!")
                break

            if self.direction == "n":
                if new_coordinates[0] == 0:
                    self.direction = "e"
                    wall_message()
                else:
                    print("Moving one step forward.")

                new_coordinates = coordinates_func(new_coordinates[0]-1,
                                                   new_coordinates[1])

            elif self.direction == "s":

                if new_coordinates[0] == 9:
                    self.direction = "w"
                    wall_message()
                else:
                    print("Moving one step forward.")

                new_coordinates = coordinates_func(new_coordinates[0]+1, 
                                                   new_coordinates[1])

            elif self.direction == "e":

                if new_coordinates[1] == 9:
                    self.direction = "s"
                    wall_message()
                else:
                    print("Moving one step forward.")

                new_coordinates = coordinates_func(new_coordinates[0], 
                                                   new_coordinates[1]+1)

            elif self.direction == "w":

                if new_coordinates[1] == 0:
                    self.direction = "n"
                    wall_message()
                else:
                    print("Moving one step forward.")

                new_coordinates = coordinates_func(new_coordinates[0], 
                                                   new_coordinates[1]-1)
