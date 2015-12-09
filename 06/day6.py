def parse_directions():
    grid = define_matrix(1000)
    with open('input.txt') as f:
        for line in f:
            follow_direction(line, grid)
    return count_lights(grid)

def define_matrix(n):
    """Create an nxn matrix of 0s"""

    return [[0 for x in range(n)] for x in range(n)]

def follow_direction(s, grid):
    """Parse directions"""

    s = s.split()
    top_left = [int(x) for x in s[-3].split(',')]
    bottom_right = [int(x) for x in s[-1].split(',')]

    for yval, row in enumerate(grid[top_left[1]:(bottom_right[1]+1)], start=top_left[1]):
        for xval, light in enumerate(row[top_left[0]:bottom_right[0]+1], start=top_left[0]):
            if s[0] == "toggle":
                if light == 0:
                    row[xval] = 1
                else:
                    row[xval] = 0
            else:
                if s[1] == "on":
                    if light == 0:
                        row[xval] = 1
                elif s[1] == "off":
                    if light == 1:
                        row[xval] = 0

def count_lights(grid):
    """Returns number of lights that are turned on."""

    on_lights = 0
    for row in grid:
        for light in row:
            if light == 1:
                on_lights += 1

    return on_lights
