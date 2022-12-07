# Part 1

def parse_floors(directions):
    """Determine ending floor for Santa based on () directions.

    Args:
        directions: Some string composed of ( & )
    Returns:
        start_floor: Int representing Santa's final floor
    """

    start_floor = 0
    for letter in directions:
        if letter == "(":
            start_floor += 1
        elif letter == ")":
            start_floor -= 1
    return start_floor

# Part 2
def parse_floors2(directions):
    """Return position of first basement character (-1)"""

    start_floor = 0
    for pos, char in enumerate(s):
        if char == "(":
            start_floor += 1
        elif char == ")":
            start_floor -= 1

        if start_floor < 0:
            pos = pos + 1
            return "Santa's in the basement after direction #: %s" % (pos,)


