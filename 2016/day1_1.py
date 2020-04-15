import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "input.txt")


# current: the current orientation
# direction: the direction to turn
def turn(current, direction):
    """turn will return a new orientation 'north', 'south', 'east' or 'west'"""
    orientations = ["north", "east", "south", "west"]
    index = orientations.index(current)

    if direction == "L":
        return orientations[(index-1) % len(orientations)]

    if direction == "R":
        return orientations[(index+1) % len(orientations)]

    return current


count = {
    "north": 0,
    "east": 0,
    "south": 0,
    "west": 0
}

current = "north"

with open(filename) as instructions:
    directions = instructions.read().split(", ")


for di in directions:
    direction = di[0]
    current = turn(current, direction)
    blocks = int(di[1:])
    count[current] += blocks

vertical = count["north"] - count["south"]
horizontal = count["east"] - count["west"]

total_distance = abs(vertical) + abs(horizontal)
print(total_distance)
