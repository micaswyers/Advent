from collections import defaultdict

def parse_input(input_file):
    """Returns a dict mapping each person to other people & how happy this makes her.

    Sample output:
        ex) {'Mica': {'Harrison': 100, 'Bodger': -100}}
    """

    seating_dict = defaultdict(lambda: {})
    with open(input_file) as f:
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
    """Returns updated dictionary adding together Person A & Person B's changes in happiness"""

    updated_dict = defaultdict(lambda: {})
    for person, units_dict in seating_dict.iteritems():
        for schmoe in units_dict:
            if person != schmoe:
                total_units = seating_dict[person][schmoe] + seating_dict[schmoe][person]
                updated_dict[person][schmoe] = total_units
            else:
                continue
    return updated_dict

def calculate_max_happiness(seating_dict, remaining_nodes, start_node, current_node):
    """Returns maximum happiness number possible

        Args:
            seating_dict: dict mapping person to other people + change in happiness
            remaining_nodes: list of people not yet seated
            start_node: where you start the seating arrangement
            current_node: whom you just seated
        Returns:
            maximum happiness configuration
     """


    happiness_options = []
    if not remaining_nodes:
        return seating_dict[start_node][current_node]
    for next_node in remaining_nodes:
        happiness = 0
        possible_next_nodes = remaining_nodes[:]
        happiness += seating_dict[current_node][next_node]
        happiness += calculate_max_happiness(
                seating_dict,
                possible_next_nodes,
                start_node,
                possible_next_nodes.pop(remaining_nodes.index(next_node)),
        )
        happiness_options.append(happiness)
    return max(happiness_options)

def solve_physical_idiocy():
    """Find the best seating arrangement & return its happiness total"""

    #seating_dict = symmetrical_dict(parse_input('input.txt')) # Part 1
    seating_dict = symmetrical_dict(parse_input('input2.txt')) # Part 2

    remaining_people = seating_dict.keys()[:]
    start_node = 'Alice'
    remaining_people.remove('Alice')
    return calculate_max_happiness(
            seating_dict,
            remaining_people,
            start_node,
            start_node,
    )
