#Part 1

def count_houses(directions):
    """Counts the number of houses receiving at least one gift from Santa.

    Starts at house 1 & then after moving based on directional arrow,
    Santa delivers another gift, so > delivers to two houses.

    Args:
        directions: string of ><^v directions.
    Returns:
        int representing # of houses receiving 1+ present
    """
    starting_coords = [0,0]
    houses = {}
    houses[str(starting_coords)] = 1
    x = 0
    y = 0
    for char in directions:
        x, y = _parse_char(char, x, y)
        if houses.get(str([x,y])):
            houses[str([x,y])] += 1
        else:
            houses[str([x,y])] = 1
    return len(houses)

def _parse_char(char, x, y):
    """Parse directional character & return updated x & y vals.

    Args:
        char: string (^v<>) representing NSEW
        x: int
        y: int
    Returns:
        x & y
    """

    if char == '^':
        y += 1
    elif char == 'v':
        y -= 1
    elif char == '>':
        x += 1
    elif char == '<':
        x -= 1
    return x, y


# Part 2
def count_houses2(directions):
    """Count number of houses visited by Santa + Robo-Santa

    Santa and Robo-Santa start at the same house then alternate following the
    directions.
    """
    """
    starting_coords = [0,0]
    houses = {}
    houses[str(starting_coords)] = 1
    x = 0
    y = 0
    for char in directions:
        x, y = _parse_char(char, x, y)
        if houses.get(str([x,y])):
            houses[str([x,y])] += 1
        else:
            houses[str([x,y])] = 1
    return len(houses)
    """

    starting_coords = [0,0]
    houses = {}
    houses[str(starting_coords)] = 1
    santa_x = 0
    santa_y = 0
    robo_x = 0
    robo_y = 0
    for idx in range(len(directions)):
        if idx % 2:
            # Odd-indexed directions for Robo-Santa
            robo_x, robo_y = _parse_char(directions[idx], robo_x, robo_y)
            if houses.get(str([robo_x,robo_y])):
                houses[str([robo_x,robo_y])] += 1
            else:
                houses[str([robo_x,robo_y])] = 1
        else:
            # Even-indexed directions for real Santa
            santa_x, santa_y = _parse_char(directions[idx], santa_x, santa_y)
            if houses.get(str([santa_x, santa_y])):
                houses[str([santa_x, santa_y])] += 1
            else:
                houses[str([santa_x, santa_y])] = 1
    return len(houses)











