# wire_1 = ("R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72")
# wire_2 = ("U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83")

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "input.txt")

with open(filename) as file:
    everything = file.readlines()
    # wire_1 = everything[:everything.index("\n")]
    # wire_2 = everything[everything.index("\n"):]
    wire_1 = everything[0].split(",")
    wire_2 = everything[1].split(",")

coords = (0, 0)
positions = []


def directions(coords, direction, positions):
    orientation = direction[0]
    movement = int(direction[1:])
    x, y = coords
    y_1 = y
    x_1 = x

    if orientation == "U":
        for y in range(y_1, y_1 + movement):
            coords = (x, y)
            positions.add(coords)
        y = y_1 + movement

    elif orientation == "D":
        for y in range(y_1 - movement, y_1):
            coords = (x, y)
            positions.add(coords)
        y = y_1 - movement

    elif orientation == "L":
        for x in range(x_1 - movement, x_1):
            coords = (x, y)
            positions.add(coords)
        x = x_1 - movement

    elif orientation == "R":
        for x in range(x_1, x_1 + movement):
            coords = (x, y)
            positions.add(coords)
        x = x_1 + movement

    return (x, y)


positions1 = set()
positions2 = set()

for direction in wire_1:
    coords = directions(coords, direction, positions1)

coords = (0, 0)
for direction in wire_2:
    coords = directions(coords, direction, positions2)


coincidences = positions1.intersection(positions2)
print(len(coincidences))
print(len(positions1))
print(len(positions2))

distances = []

for positions in coincidences:
    x, y = positions
    distance = abs(x) + abs(y)
    distances.append(distance)

distances.sort()
answer = distances[0]

print(answer)
