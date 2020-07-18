import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "input.txt")

with open(filename) as file:
    lines = file.readlines()

total = 0
totals = set()
finished = False

while not finished:
    for line in lines:
        total += int(line)
        if total in totals:
            print(str(total) + " is the answer")
            finished = True
            break
        totals.add(total)
