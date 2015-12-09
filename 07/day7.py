# Part 1

def follow_directions():
    with open('input.txt') as f:
        for line in f:
            print line
            process_direction(line)

def process_direction(direction):
    directions = direction.split()

    if len(directions) == 3:
        # simple assignment
        print 'assign'
    elif len(directions) == 4:
        print 'NOT'
    elif len(directions) == 5:
        if directions[1] == 'AND':
            print 'AND' # and code
        elif directions[1] == 'OR':
            print 'OR' # or code
        elif directions[1] == 'LSHIFT':
            print 'LSHIFT' # left-shift code
        elif directions[1] == 'RSHIFT':
            print 'RSHIFT' # right-shift code




