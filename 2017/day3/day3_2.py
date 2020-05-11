def get_value(positions, coords):
    x, y = coords
    value_1 = positions.get((x+1, y), 0)
    value_2 = positions.get((x-1, y), 0)
    value_3 = positions.get((x, y+1), 0)
    value_4 = positions.get((x, y-1), 0)
    value_5 = positions.get((x+1, y+1), 0)
    value_6 = positions.get((x+1, y-1), 0)
    value_7 = positions.get((x-1, y+1), 0)
    value_8 = positions.get((x-1, y-1), 0)

    value = value_1 + value_2 + value_3 + value_4 + \
        value_5 + value_6 + value_7 + value_8
    return value


def location(coords, current, positions):
    x, y = coords
    # directions
    # a = + x
    # b = + y
    # c = - x
    # d = - y
    # function location gets the current coords and returns the next ones, considering the rest of the coords completed up to moment.
    if current == "a":
        current = "b"
        x += 1
        coords = (x, y)
        if coords in positions:
            current = "a"
            x -= 1
            y -= 1
            coords = (x, y)
    elif current == "b":
        current = "c"
        y += 1
        coords = (x, y)
        if coords in positions:
            current = "b"
            y -= 1
            x += 1
            coords = (x, y)
    elif current == "c":
        current = "d"
        x -= 1
        coords = (x, y)
        if coords in positions:
            current = "c"
            x += 1
            y += 1
            coords = (x, y)
    elif current == "d":
        current = "a"
        y -= 1
        coords = (x, y)
        if coords in positions:
            current = "d"
            y += 1
            x -= 1
            coords = (x, y)

    value = get_value(positions, coords)
    positions.update({coords:  value})
    return (coords, current)


current = "a"
coords = (0, 0)
positions = {coords: 1}

while True:
    coords, current = location(coords, current, positions)
    if positions[coords] > 325489:
        print(positions[coords])
        break
