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
    print "Light in question is (%s,%s) = %s" % (row, col, grid[row][col])
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
    print "last_row ", last_row
    print "next_row ", next_row
    print "last_col ", last_col
    print "next_col ", next_col
    for i in range(last_row, next_row+1):
        for j in range(last_col, next_col+1):
            print "Looking at light: [%s,%s] = %s" % (i,j, grid[i][j])
            if grid[i][j] == "#":
                lights_on_count += 1
    if grid[row][col] == "#":
        print "Lights_On_count = ", lights_on_count
        lights_on_count -= 1
        if lights_on_count == 2 or lights_on_count == 3:
            print "Need to leave ON light on"
            return True
        return False
    elif grid[row][col] == ".":
        print "Lights_On_count = ", lights_on_count
        if lights_on_count == 3:
            print "need to turn OFF light on"
            return True
        return False

def animate_grid(grid):

    next_grid = [["." for x in range(len(grid))] for x in range(len(grid))]
    for i, row in enumerate(grid):
        print "Row: ", i
        for j, col in enumerate(row):
            on = should_turn_on((i,j), grid)
            if on:
                next_grid[i][j] = "#"
    return next_grid


# For each line in the grid
    # animate each line
        # keep track of previous line, current line, next line to determine if should be on or off
        # will need to append to a new grid
# When all lines have been animated the right number of times, count lights
