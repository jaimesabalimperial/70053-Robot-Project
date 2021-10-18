import itertools 

class Grid():

    def __init__(self, size):
        self.size = size
        self.cells = {(self.size-1, self.size-1): [], (0, self.size-1): [], (self.size-1, 0): [], (0, 0): []}
    
    def add_drink(self, drink, position): 
        self.cells[position].append(drink)

class DrinkFactory():
    def __init__(self):
        self.drinks = []
    
    def create_drinks(self, robots):
        for i in range(len(robots)):
            self.drinks.append(Drink(robots[i].id))

class Drink():
    def __init__(self, owner_id, name="Rebena", percent_filled = 100.):
        self.name = name
        self.owner_id = owner_id
        self.percent_filled = percent_filled

    def is_full(self):
        if self.percent_filled == 100.0: 
            return True
        else: 
            return False

    def is_empty(self):
        if self.percent_filled <= 0.0: 
            return True
        else: 
            return False

class Robot():
    #generate new id for each Robot instance
    newid = itertools.count()

    def __init__(self, name, position, direction, grid):
        self.name = name 
        self.id = 1000 + next(self.newid)
        self.position = position
        self.direction = direction
        self.grid = grid

    def greet(self):
        """Introduce robot to user. """
        print(f"Hello. My name is {self.name}. My ID is {self.id}.")
    

    def say_location(self):
        """Say position and direction."""

        direction_dict = {"n": "North", "s": "South", "e": "East", "w": "West"} #dictionary including complete strings for the direction abbreviations
        print(f"I am currently at {self.position}, facing {direction_dict[self.direction]}")

    def turn_clockwise(self):
        """Turns 90 degrees clockwise."""

        turning_dict = {"n":"e", "e":"s", "s":"w", "w":"n"}
        self.direction = turning_dict[self.direction]

    def is_stuck(self):
        """Returns True if robot is at the corresponding edge to its direction and prints a message to alert the user."""
        if (self.position[0] == 0 and self.direction == "n"
            or self.position[0] == self.grid.size-1 and self.direction == "s"
            or self.position[1] == self.grid.size-1 and self.direction == "e"
            or self.position[1] == 0 and self.direction == "w"):

            print("I have a wall in front of me!")
            print("Turning 90 degrees clockwise.")
            
            return True   
        else: 
            return False
    
    def move(self):
        """Move one space in current direction."""
        if self.direction == "n":
            self.position = (self.position[0]-1, self.position[1])

        elif self.direction == "s":
            self.position = (self.position[0]+1, self.position[1])

        elif self.direction == "e":
            self.position = (self.position[0], self.position[1]+1)

        elif self.direction == "w":
            self.position = (self.position[0], self.position[1]-1)

    def navigate_to_drink(self, drink):
        """Navigates robot across grid until it reaches its target location."""

        print(f"\n{self.name} is searching for its drink.")

        # initialise motion
        motion_in_place = True

        while motion_in_place:
            self.say_location()

            # pause motion if position is the same as drink
            if (self.position in list(self.grid.cells.keys()) 
               and len(self.grid.cells[self.position]) != 0
               and self.id in [drink.owner_id for drink in self.grid.cells[self.position]]
               ):
                print(f"I am drinking {drink.name} I am happy!")
                motion_in_place = False

            #if robot is not at target, move in current direction until stuck, then turn and so on...
            else:
                if self.is_stuck():
                    self.turn_clockwise()
                else:
                    print("Moving one step forward.")
                    self.move()


