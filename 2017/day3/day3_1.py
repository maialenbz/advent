import math

number = 325489
reference = math.sqrt(number)
spiral = int(reference)

if spiral % 2 != 0:
    spiral += 2
if spiral % 2 == 0:
    spiral += 1

side = spiral - 1
counting_distance = side // 2
max_dis = spiral - 1

first_corner = spiral ** 2

count = first_corner
jumps = 0
x = 0

while count > number:
    count -= 1
    jumps += 1
    if jumps <= counting_distance:
        x += 1
    else:
        x -= 1

    if jumps == side:
        jumps = 0

distance = max_dis - x
print(distance)
