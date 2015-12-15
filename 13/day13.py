from collections import defaultdict

def parse_input():
    """Returns a dict mapping each person to other people & how happy this makes her.

    Sample output:
        ex) {'Mica': {'Harrison': 100, 'Bodger': -100}}
    """

    seating_dict = defaultdict(lambda: {})
    with open('input.txt') as f:
        for line in f:
            happiness = line.split()
            name1 = happiness[0]
            name2 = happiness[-1].strip(".")
            if happiness[2] == "lose":
                units = int(happiness[3]) * -1
            else:
                units = int(happiness[3])
            seating_dict[name1][name2] = units
    return seating_dict

def symmetrical_dict(seating_dict):

    updated_dict = defaultdict(lambda: {})
    for person, units_dict in seating_dict.iteritems():
        for schmoe in units_dict:
            if person != schmoe:
                total_units = seating_dict[person][schmoe] + seating_dict[schmoe][person]
                updated_dict[person][schmoe] = total_units
            else:
                continue
    return updated_dict

