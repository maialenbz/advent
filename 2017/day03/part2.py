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
    # right = + x
    # up = + y
    # left = - x
    # down = - y
    # function location gets the current coords and returns the next ones, considering the rest of the coords completed up to the moment.
    if current == "right":
        current = "up"
        x += 1
        coords = (x, y)
        if coords in positions:
            current = "right"
            x -= 1
            y -= 1
            coords = (x, y)
    elif current == "up":
        current = "left"
        y += 1
        coords = (x, y)
        if coords in positions:
            current = "up"
            y -= 1
            x += 1
            coords = (x, y)
    elif current == "left":
        current = "down"
        x -= 1
        coords = (x, y)
        if coords in positions:
            current = "left"
            x += 1
            y += 1
            coords = (x, y)
    elif current == "down":
        current = "right"
        y -= 1
        coords = (x, y)
        if coords in positions:
            current = "down"
            y += 1
            x -= 1
            coords = (x, y)

    value = get_value(positions, coords)
    positions.update({coords:  value})
    return (coords, current)


current = "right"
coords = (0, 0)
positions = {coords: 1}

while True:
    coords, current = location(coords, current, positions)
    if positions[coords] > 325489:
        print(positions[coords])
        break
