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


current = "north"
positions = set()

with open(filename) as instructions:
    directions = instructions.read().split(", ")

found = False
x = 0
y = 0

while not found:

    for di in directions:
        direction = di[0]
        current = turn(current, direction)
        blocks = int(di[1:])

        for i in range(blocks):
            if current == "north":
                y += 1
            elif current == "south":
                y -= 1
            elif current == "east":
                x += 1
            elif current == "west":
                x -= 1

            position = (x, y)

            if position in positions:
                print(position)
                found = True
                break

            positions.add(position)

        if found:
            break

distance = abs(x) + abs(y)
print(distance)
