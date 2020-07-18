import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "input.txt")

overall_fuel = 0

with open(filename) as file:
    for mass in file:
        fuel = int(mass) // 3 - 2
        total_fuel = 0
        while fuel > -1:
            total_fuel += fuel
            fuel = fuel // 3 - 2

        overall_fuel += total_fuel

print(str(overall_fuel) + " is the total fuel you need")
