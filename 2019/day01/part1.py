import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "input.txt")

total = 0
with open(filename) as file:
    for mass in file:
        fuel = int(mass)//3 - 2
        total += fuel

print(int(total))
