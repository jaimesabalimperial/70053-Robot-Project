name = input("What is the name of the robot? ")
identifier = 1000

message = f"Hello. My name is {name}. My ID is {identifier}."
print(message)

#define size of grid in which robot can move in
grid_size = 10

row = int(input("What is its current row coordinate? "))

if row < 0: 
    row = 0
elif row > grid_size: 
    row = grid_size - 1

col = int(input("What is its current column coordinate? "))

if col < 0: 
    col = 0
elif col > grid_size: 
    col = grid_size - 1

quadrant = str

if row < grid_size/2 and col > grid_size/2: 
    quadrant = "top right"
elif row > grid_size/2 and col > grid_size/2: 
    quadrant = "bottom right"
elif row > grid_size/2 and col < grid_size/2: 
    quadrant = "bottom left"
elif row < grid_size/2 and col < grid_size/2: 
    quadrant = "top left"

coordinate = f"({row}, {col})"
coordinate_message = f"My current location is {coordinate}. I am in the {quadrant} quadrant."

print(coordinate_message)
