
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "input.txt")

with open(filename) as file:
    instructions = list(map(str.rstrip, file.readlines()))


top = set(range(1, 4))
bottom = set(range(7, 10))
left = set(range(1, 8, 3))
right = set(range(3, 10, 3))


def fun(current, direction):

    if direction == "L":
        if current in left:
            return current
        return current-1

    if direction == "R":
        if current in right:
            return current
        return current+1

    if direction == "U":
        if current in top:
            return current
        return current-3

    if direction == "D":
        if current in bottom:
            return current
        return current+3


current = 5

for word in instructions:
    for direction in word:
        current = fun(current, direction)
    print(current)
