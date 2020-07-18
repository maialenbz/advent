import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "input.txt")

with open(filename) as file:
    patches = list(map(str.rstrip, file.readlines()))

inches = {}
analyzed_refs = set()
overlapping_refs = set()

for patch in patches:
    ref = patch[:patch.index("@")]
    analyzed_refs.add(ref)

    cut_patch = patch[(patch.index("@")+1):]
    detail_patch = cut_patch.partition(":")
    distances = str.lstrip(detail_patch[0])
    dist_left = int(distances[:distances.index(",")])
    dist_up = int(distances[distances.index(",")+1:])
    dimensions = str.lstrip(detail_patch[2])
    width = int(dimensions[:dimensions.index("x")])
    height = int(dimensions[dimensions.index("x")+1:])

    width_limit = dist_left + width
    height_limit = dist_up + height

    for width_coords in range(dist_left, width_limit):
        for height_coords in range(dist_up, height_limit):
            coords = (width_coords, height_coords)
            try:
                refs = inches[coords]
                refs.append(ref)
                overlapping_refs |= set(refs)
            except KeyError:
                inches[coords] = [ref]

answer = analyzed_refs.difference(overlapping_refs)
print(answer)
