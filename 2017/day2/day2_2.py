import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "input.txt")

total = 0

with open(filename) as file:
    for line in file:
        strings = line.rstrip().split("\t")
        numbers = [int(s) for s in strings]
        numbers.sort(reverse=True)
        y = x = 0
        while x < len(numbers):
            y += 1
            if numbers[x] % numbers[y] == 0:
                total += numbers[x] // numbers[y]
                break
            if y == len(numbers)-1:
                x += 1
                y = x

print(total)
