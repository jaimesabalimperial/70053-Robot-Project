import random
from robot_init import RobotInitialiser
from robot import Grid, DrinkFactory

def run_simulation(n_robots, grid_size):
    """ Start robot navigation simulation.

    Args:
        n_robots (int): Number of robots in grid.
        grid_size (int): The size of the grid. Defaults to 10.
    """
    #create grid, robots and drinks
    grid = Grid(grid_size)

    initialiser = RobotInitialiser(grid)
    initialiser.create_robots(n_robots)

    drinks_factory = DrinkFactory()
    drinks_factory.create_drinks(initialiser.robots)

    #navigate robots to their respective drinks
    for i in range(n_robots):   
        grid.add_drink(drinks_factory.drinks[i], initialiser.targets[random.randint(0,3)])
        initialiser.robots[i].navigate_to_drink(drinks_factory.drinks[i])

if __name__ == "__main__":
    # run simulation
    run_simulation(n_robots=6, grid_size=10)
