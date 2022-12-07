# Part 1

def parse_input():
    """Returns list of possible bottle volumes (as ints)"""

    bottles = []
    with open('input.txt') as f:
        for line in f:
            bottles.append(int(line.strip()))
    return bottles

def decant_nog(bottles_list, nog_volume=150):
    """Uses recursion to find number of combinations for making up nog_volume

        Args:
            bottles_list: list of ints, each representing bottle volumn
            nog_volume: int representing num liters of egg nog to decant
        Returns:
            num_combos: number of possible combinations (int)
    """

    num_combos = 0
    if not nog_volume:
        return 1
    elif nog_volume < 0:
        return 0
    for idx in range(len(bottles_list)):
        new_vol = nog_volume - bottles_list[idx]
        num_combos += decant_nog(bottles_list[idx+1:], new_vol)
    return num_combos

def find_combinations():
    """Finds total combinations given input.txt & nog_volume of 150"""

    bottles_list = parse_input()
    num_combos = decant_nog(bottles_list)
    return num_combos

# Part 2
def decant_nog2(bottles_list, depth, nog_volume=150):
    """Finds number of combinations of bottles in bottles_list where number of bottles used equals depth

        Args:
            bottles_list: list of ints, each representing bottle volume
            depth: number of times (int) that the function is allowed to be called
            nog_volume: int representing num liters of egg nog to decant
        Returns:
            num_combos: number of possible combinations (int)
    """

    num_combos = 0
    if not nog_volume:
        return 1
    elif nog_volume < 0:
        return 0
    if depth == 0:
        return 0
    for idx in range(len(bottles_list)):
        new_vol = nog_volume - bottles_list[idx]
        num_combos += decant_nog2(bottles_list[idx+1:], depth-1, new_vol)
    return num_combos

def find_combinations2():
    """Returns number of combinations for the minimum number of bottles to decant nog

        (Also prints the number of bottles)
    """

    bottles_list = parse_input()
    for idx in range(len(bottles_list)):
        num_combos = decant_nog2(bottles_list, idx+1)
        if num_combos != 0:
            print idx + 1
            return num_combos
