
# Part 1

def save_directions():
    wire_diagram = set()
    with open('input.txt') as f:
        for line in f:
            wire_diagram.update([line])
    return wire_diagram

def directions_loop(wire_diagram):
    wire_values = {}
    while 'a' not in wire_values:
        for line in wire_diagram:
            process_direction(line, wire_values)
    print '*****'
    print wire_values
    return wire_values['a']

def process_direction(direction, wire_values):
    operation = direction.split(' -> ')

    directions = operation[0].split()
    assigned = operation[1].strip()

    if len(directions) == 1:
        op1 = get_value(directions[0], wire_values)
        if op1 != -1:
            print "assigning %s to dict: %s" % (op1, assigned)
            wire_values[assigned] = op1 & 0xffff
    elif len(directions) == 2:
        op1 = get_value(directions[1], wire_values)
        if op1 != -1:
            print "assigning %s to dict: %s" % (~op1, assigned)
            wire_values[assigned] = ~op1 & 0xffff
    elif len(directions) == 3:
        if directions[1] == 'AND':
            op1 = get_value(directions[0], wire_values)
            op2 = get_value(directions[2], wire_values)
            if op1 != -1 and op2 != -1:
                print "assigning %s to dict: %s" % (op1 & op2, assigned)
                wire_values[assigned] = (op1 & op2) & 0xffff
        elif directions[1] == 'OR':
            op1 = get_value(directions[0], wire_values)
            op2 = get_value(directions[2], wire_values)
            if op1 != -1 and op2 != -1:
                print "assigning %s to dict: %s" % (op1 | op2, assigned)
                wire_values[assigned] = (op1 | op2) & 0xffff
        elif directions[1] == 'LSHIFT':
            op1 = get_value(directions[0], wire_values)
            op2 = get_value(directions[2], wire_values)
            if op1 != -1 and op2 != -1:
                print "assigning %s to dict: %s" % (op1 << op2, assigned)
                wire_values[assigned] = (op1 << op2) & 0xffff
        elif directions[1] == 'RSHIFT':
            op1 = get_value(directions[0], wire_values)
            op2 = get_value(directions[2], wire_values)
            if op1 != -1 and op2 != -1:
                print "assigning %s to dict: %s" % (op1 >> op2, assigned)
                wire_values[assigned] = (op1 >> op2) & 0xffff
    return

def get_value(s, d):
    """Determine if string s is in d or if it's a literal"""

    if s in d:
        return d[s]
    try:
        return int(s)
    except Exception:
        return -1
    return -1
