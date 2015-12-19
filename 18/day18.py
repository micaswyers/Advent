# Part 1
def define_grid(n=100, f="input.txt"):
    """Given an input file, recreates it as a nxn matrix"""

    grid = []
    with open(f) as input_file:
        for line in input_file:
            row = []
            for char in line.strip():
                row.append(char)
            grid.append(row)
    return grid

def should_turn_on(point, grid):
    # point is a tuple (i, j)

    row = point[0]
    col = point[1]
    lights_on_count = 0
    last_row = row - 1
    next_row = row + 1
    last_col = col - 1
    next_col = col + 1

    if last_row < 0:
        last_row = row
    if next_row > len(grid) - 1:
        next_row = row
    if last_col < 0:
        last_col = col
    if next_col > len(grid) - 1:
        next_col = col
    for i in range(last_row, next_row+1):
        for j in range(last_col, next_col+1):
            if grid[i][j] == "#":
                lights_on_count += 1
    if grid[row][col] == "#":
        lights_on_count -= 1
        if lights_on_count == 2 or lights_on_count == 3:
            return True
        return False
    elif grid[row][col] == ".":
        if lights_on_count == 3:
            return True
        return False

def animate_grid_once(grid):

    next_grid = [["." for x in range(len(grid))] for x in range(len(grid))]
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            on = should_turn_on((i,j), grid)
            if on:
                next_grid[i][j] = "#"
    return next_grid

def animate_grid_multiple(grid, num_iterations=100):

    for iteration in range(num_iterations):
        grid = animate_grid_once(grid)
    return grid

def count_on_lights(grid):

    on_count = 0
    for i, row in enumerate(grid):
        for light in row:
            if light == "#":
                on_count += 1
    return on_count


