from collections import defaultdict

# Part 1
def parse_input():

    sues = defaultdict(lambda: {})
    with open('input.txt') as f:
        for line in f:
            words = line.split()
            words = [word.strip(':,') for word in words]
            num_sue = words[1]
            items_counts = [word.strip(':,') for word in words[2:]]
            sues[num_sue][items_counts[0]] = items_counts[1]
            sues[num_sue][items_counts[2]] = items_counts[3]
            sues[num_sue][items_counts[4]] = items_counts[5]
    return sues
