import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "input.txt")

with open(filename) as f:
    digits = list(map(int, f.read().split(",")))
    print(digits)

digits[1] = 12
digits[2] = 2

x = 0
while x < len(digits):
    if digits[x] == 1:
        position_1 = digits[x+1]
        position_2 = digits[x+2]
        final_position = digits[x+3]
        digits[final_position] = digits[position_1] + digits[position_2]
    if digits[x] == 2:
        position_1 = digits[x+1]
        position_2 = digits[x+2]
        final_position = digits[x+3]
        digits[final_position] = digits[position_1] * digits[position_2]
    if digits[x] == 99:
        break
    x += 4

print(digits)
print(digits[0])
