from collections import defaultdict

TARGET_SUE = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }

# Part 1
def parse_input():
    """Returns dict mapping Sue # to item & counts dict

    ex) {500: {'cats': 2, 'goldfish': 9, 'children': 8}}
    """

    sues = defaultdict(lambda: {})
    with open('input.txt') as f:
        for line in f:
            words = line.split()
            words = [word.strip(':,') for word in words]
            num_sue = int(words[1])
            items_counts = [word.strip(':,') for word in words[2:]]
            sues[num_sue][items_counts[0]] = int(items_counts[1])
            sues[num_sue][items_counts[2]] = int(items_counts[3])
            sues[num_sue][items_counts[4]] = int(items_counts[5])
    return sues

def find_sue(sues_dict):
    """Returns list containing numbers of possible Aunt Sues

    Args:
        sues_dict: dict mapping number to dict of known possessions & counts
    Returns:
        int representing possible Aunt Sue match
    """

    possible_sue = None
    for num_sue, items in sues_dict.iteritems():
        possible_match = []
        for item, number in items.iteritems():
            if number == TARGET_SUE[item]:
                possible_match.append(True)
        if len(possible_match) == 3:
            return num_sue

# Part 2
def find_sue2(sues_dict):
    """Returns list containing numbers of possible Aunt Sues

    Args:
        sues_dict: dict mapping number to dict of known possessions & counts
    Returns:
        int representing possible Aunt Sue match
    """

    for num_sue, items in sues_dict.iteritems():
        possible_match = []
        for item, number in items.iteritems():
            if item not in ['cats', 'trees', 'pomeranians', 'goldfish'] and number == TARGET_SUE[item]:
                possible_match.append(True)
            elif item in ['cats', 'trees'] and number > TARGET_SUE[item]:
                possible_match.append(True)
            elif item in ['pomeranians', 'goldfish'] and number < TARGET_SUE[item]:
                possible_match.append(True)
        if len(possible_match) == 3:
            return num_sue
