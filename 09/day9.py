# Part 1

def save_directions(path):
    """Given list of distances, return dict of places to distance.

    Args:
        path: string representing filepath of input

    Sample input:
        London to Dublin = 464
        London to Belfast = 518
        Dublin to Belfast = 141
    Sample ouput:
        {
            ('London', 'Dublin'): 464,
            ('London', 'Belfast'): 518,
            ('Dublin', 'Belfast'): 141,
        }
    """

    directions_dict = {}
    with open(path) as f:
        for line in f:
            directions = line.split(" = ")
            places = directions[0].split(" to ")
            directions_dict[(places[0], places[1])] = int(directions[1].strip())
    return directions_dict


def find_all_nodes(distances_dict):
    """Return list of possible starting points for TSP

    Args:
        distances_dict: dict mapping two points to their distance
            {('pointA', 'pointB'): 100}
    Returns:
        places_list: list of place names (strings)
            ['pointA', 'pointB']
    """

    places_list = []
    for points in distances_dict.keys():
        for point in points:
            if point not in places_list:
                places_list.append(point)
    return places_list

def calculate_lowest_distance(places_list):

    pass


def create_distances_dict(nodes_list, node_dict):
    """Return a dict mapping each node to a dict of nodes & distances

    Args:
        nodes_list: list of all possible nodes (strings)
        node_dict: dict where keys are tuples of two nodes mapped to the
            distance between them
    Returns:
        distances_dict: dict mapping a node to a dict where the keys are
            nodes & the values are distances
    """

    distances_dict = {}
    for node in nodes_list:
        distances_dict[node] = {}
        for path, distance in node_dict.iteritems():
            if node not in path:
                continue
            if node == path[0]:
                if not distances_dict[node].get(path[1]):
                    distances_dict[node][path[1]] = distance
            elif node == path[1]:
                if not distances_dict[node].get(path[0]):
                    distances_dict[node][path[0]] = distance

    return distances_dict

def calculate_route(distances_dict, remaining_nodes, current_node=None):
    """Calculate shortest route between nodes

    Args:
        - current_node: string representing the node being appended to the route
        - distances_dict: dict mapping node to dict of other nodes & distances
            ex) {'a': {'b': 10, 'c': 5}, 'b': {'a': 10, 'c': 2}, 'c': {'a': 5, 'b', 2}
        - remaining_nodes: list of strings, each representing a node that has
            not yet been visited
    Returns:
        distance: int representing the shortest distance (in miles) to hit
            each node exactly once
    """

    distances = []
    if not remaining_nodes:
        return 0
    for next_node in remaining_nodes:
        distance = 0
        possible_next_nodes = remaining_nodes[:]
        if current_node:
            distance += distances_dict[current_node][next_node]
        distance += calculate_route(
            distances_dict,
            possible_next_nodes,
            possible_next_nodes.pop(remaining_nodes.index(next_node)),
        )
        distances.append(distance)
    # return min(distances) # Part 1 - shortest route
    return max(distances) # Part 2 - longest route


def index():

    nodes_and_distances = save_directions('input.txt')
    all_nodes = find_all_nodes(nodes_and_distances)
    distances_dict = create_distances_dict(all_nodes, nodes_and_distances)


    return calculate_route(distances_dict, all_nodes)
