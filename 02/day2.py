# Part 1

def estimate_wrapping():
    """Estimate amount of wrapping paper given dimensions of a bunch of boxes.

    Dimensions comes as a list of LxWxH in a txt file
    Each box needs 2*l*w + 2*w*h + 2*h*l + squarefeet of SMALLEST side in paper

    Returns:
        Total square feet needed of wrapping paper (int)
    """

    with open('day2_dimensions.txt') as dimensions_file:
        total_paper = 0
        for line in dimensions_file:
            dimensions = line.split('x')
            dimensions = [int(x) for x in dimensions]
            l = dimensions[0]
            w = dimensions[1]
            h = dimensions[2]
            dimensions.sort()

            surface_area = (2*l*w) + (2*w*h) + (2*h*l)
            surface_area += (dimensions[0] * dimensions[1])
            total_paper += surface_area
    return total_paper

# Part 2
def estimate_ribbon():
    """Estimate amount of ribbon needed to wrap all these presents.

    Ribbon length per box is equal to the smallest perimeter of any one face
    PLUS cubic feet of volume of the box (for the bow).

    Returns:
        Total feet of ribbon (int)
    """
    with open('day2_dimensions.txt') as dimensions_file:
        total_ribbon = 0
        for line in dimensions_file:
            dimensions = line.split('x')
            dimensions = [int(x) for x in dimensions]
            dimensions.sort()

            face = (2 * dimensions[0]) + (2 * dimensions[1])
            bow = (dimensions[0] * dimensions[1] * dimensions[2])
            total_ribbon += (face + bow)

        return total_ribbon

