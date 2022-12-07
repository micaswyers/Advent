from string import ascii_lowercase, ascii_uppercase

def _create_priority_dicts(case='lower'):
    if case == 'lower':
        return dict(zip(ascii_lowercase, range(1,27)))
    else:
        return dict(zip(ascii_uppercase, range(27,53)))


# Part 1
def sum_priorities(filename='input.txt'):
    with open(filename, 'r') as f:
        priorities = []
        for line in f:
            one_side = int(len(line)/2)
            c1 = set(line[:one_side])
            c2  = set(line[one_side:])
            overlap = list(c1.intersection(c2))
            priorities.append(overlap[0])
    lower = _create_priority_dicts('lower')
    print(lower)
    upper = _create_priority_dicts('upper')

    total = 0
    for p in priorities:
        if p.islower():
            total += lower[p]
        elif p.isupper():
            total += upper[p]
    return total


print(sum_priorities())