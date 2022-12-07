
# Part 1

def save_directions():
    wire_diagram = set()
    with open('input.txt') as f:
        for line in f:
            wire_diagram.update([line])
    return wire_diagram

def directions_loop(wire_diagram):
    wire_values = {}
    wire_values['b'] = 46065 # Part 2
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
    if assigned in wire_values:
        return

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
    """Determine if string s is in d or if it's a literal

        Args:
            s: string representing item left of ->
            d: dictionary of values
        Returns:
            - value of s in dict, cast of s to an int, or -1 if s is not in the
            dictionary & cannot be cast as an int (=s has not yet been assigned)
    """

    if s in d:
        return d[s]
    try:
        return int(s)
    except Exception:
        # Returning -1 here instead of False because some strings mapped to 0
        return -1
    return -1
