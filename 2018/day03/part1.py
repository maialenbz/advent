import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "input.txt")

with open(filename) as file:
    patches = list(map(str.rstrip, file.readlines()))

inches = {}

for patch in patches:

    cut_patch = patch[(patch.index("@")+1):]
    detail_patch = cut_patch.partition(":")
    distances = str.lstrip(detail_patch[0])
    dist_left = int(distances[:distances.index(",")])
    dist_up = int(distances[distances.index(",")+1:])
    dimensions = str.lstrip(detail_patch[2])
    width = int(dimensions[:dimensions.index("x")])
    heigth = int(dimensions[dimensions.index("x")+1:])

    width_limit = dist_left + width
    heigth_limit = dist_up + heigth

    for width_coords in range(dist_left, width_limit):
        for heigth_coords in range(dist_up, heigth_limit):
            coords = (width_coords, heigth_coords)
            if coords not in inches:
                inches[coords] = 1
            elif coords in inches:
                inches[coords] += 1

repeated = 0

for coords in inches:
    if inches[coords] > 1:
        repeated += 1

print(repeated)
