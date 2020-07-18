import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "input.txt")

with open(filename) as file:
    instructions = list(map(str.rstrip, file.readlines()))


cu = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D"]

top = {"1", "2", "4", "5", "9"}
bottom = {"5", "9", "A", "C", "D"}
left = {"1", "2", "5", "A", "D"}
right = {"1", "4", "9", "C", "D"}
top_center = {"3"}
bottom_center = {"B"}


def fun(current, direction):
    # fun takes current and gives back the final position
    index = cu.index(current)
    if direction == "L":
        if current in left:
            return current
        current = cu[index-1]
        return current

    if direction == "R":
        if current in right:
            return current
        current = cu[index+1]
        return current

    if direction == "U":
        if current in top:
            return current
        if current in top_center:
            current = "1"
            return current
        if current == "D":
            current = "B"
            return current
        current = cu[index-4]
        return current

    if direction == "D":
        if current in bottom:
            return current
        if current in bottom_center:
            current = "D"
            return current
        if current == "1":
            current = "3"
            return current
        current = cu[index+4]
        return current


current = "5"

for word in instructions:

    for direction in word:
        current = fun(current, direction)
    print(current)
