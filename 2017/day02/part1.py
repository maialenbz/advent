import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "input.txt")

total = 0

with open(filename) as file:
    for line in file:
        strings = line.rstrip().split("\t")
        numbers = [int(s) for s in strings]
        total += max(numbers) - min(numbers)

print(total)
