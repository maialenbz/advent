import os
dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "input.txt")

with open(filename) as f:
    di = list(map(int, f.read().split(",")))


def operation(digits):
    # operation will get a digits list and will return a value of digits[0]
    x = 0
    while x+3 < len(digits):
        position_1 = digits[x+1]
        position_2 = digits[x+2]
        final_position = digits[x+3]
        if digits[x] == 1:
            digits[final_position] = digits[position_1] + digits[position_2]
        elif digits[x] == 2:
            digits[final_position] = digits[position_1] * digits[position_2]
        elif digits[x] == 99:
            break
        x += 4
    return digits[0]


for noun in range(1, 100):
    for verb in range(1, 100):
        digits = di.copy()
        digits[1] = noun
        digits[2] = verb
        first_position = operation(digits)
        if first_position == 19690720:
            print(f"{noun} and {verb}")
            break
