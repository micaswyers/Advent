# Part 1

def save_directions():

    directions_dict = {}
    with open('input.txt') as f:
        for line in f:
            directions = line.split(" = ")
            directions_dict[directions[0]] = int(directions[1].strip())
    return directions_dict
