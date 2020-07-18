import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "input.txt")

file = open(filename)
total = 0

for line in file:
    total += int(line)
    print(total)
