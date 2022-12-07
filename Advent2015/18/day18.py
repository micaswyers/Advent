# Part 1
def define_grid(n=100, f="input.txt", stuck_corners=False):
    """Given an input file, recreates it as a nxn matrix

        Args:
            n: int, dimension for a square matrix
            f: string, name of input file
            stuck_corners: bool, indicates whether four corner lights should always be on
        Returns:
            grid: nxn matrix recreating input characters in f-file
    """

    grid = []
    with open(f) as input_file:
        for line in input_file:
            row = []
            for char in line.strip():
                row.append(char)
            grid.append(row)
    if stuck_corners:
       return turn_on_corners(grid)
    return grid

def should_turn_on(point, grid):
    """Returns True if a light should be turned on based on surrounding points
        - Each light's next state depends on the surrounding 8 lights' states.
        - Edge & corner lights have fewer than 8 neighbors; those are considered OFF.
        - An on-light with 2 or 3 surrounding on lights stays on.
        - An off-light with exactly 3 surrounding on lights turns on.
        - Everything else is turned off.
        Args:
            point: tuple, containing the row & col for a given light (both ints)
            grid: an nxn matrix
        Returns:
            - True if the light should turn on; False otherwise
    """

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
    """Given a grid, animate it once"""

    next_grid = [["." for x in range(len(grid))] for x in range(len(grid))]
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            on = should_turn_on((i,j), grid)
            if on:
                next_grid[i][j] = "#"
    return next_grid

def animate_grid_multiple(grid, num_iterations=100):
    """Animate the grid n-number of times

        Args:
            grid: some nxn matrix
            num_iterations: the number of times to run the animation step
        Returns:
            grid: The updated grid based on n iterations of animation
    """

    for iteration in range(num_iterations):
        grid = animate_grid_once(grid)
    return grid

def count_on_lights(grid):
    """Given some grid, return the number of illuminated lights."""

    on_count = 0
    for i, row in enumerate(grid):
        for light in row:
            if light == "#":
                on_count += 1
    return on_count

# Part 2

def turn_on_corners(grid):
    """Turns all four corners of grid to "#" (On)"""

    x = len(grid) - 1
    grid[0][0] = "#"
    grid[0][x] = "#"
    grid[x][0] = "#"
    grid[x][x] = "#"
    return grid

def animate_grid_with_on_corners(grid, num_iterations=100):
    """Given a grid, animate it once but corner four lights are stuck on"""

    for iteration in range(num_iterations):
    # Make sure lights are stuck on in the corners
        grid = turn_on_corners(animate_grid_once(grid))
    return grid
