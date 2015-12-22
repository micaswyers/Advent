from collections import defaultdict
import re

# Part 1

def make_dict(filename):
    """Returns dictionary mapping chars to possible replacements"""

    replacements_dict = defaultdict(lambda:[])
    with open(filename) as f:
        for line in f:
            words = line.split("=>")
            words = [word.strip() for word in words]
            replacements_dict[words[0]].append(words[1])
    return replacements_dict

def find_symbols(calib_str):
    """Returns list of symbols (strings) in a given string

        Args:
            calib_str: string used for calibration
        Returns:
            sumbols: list of strings, each representing on symbol
    """

    symbol_finder = re.compile('e|[A-Z][a-z]?').finditer
    symbols = []
    for match in symbol_finder(calib_str):
        symbol = calib_str[match.start():match.end()]
        symbols.append(symbol)
    return symbols

def make_substitutions(symbols_list, replacements_dict):
    """Returns set of new strings, each made by sub-ing one symbol

        Args:
            symbols_list: list of symbols (string) representing original calibration string
            replacements_dict: dict mapping strings to what they can be replaced with
        Returns:
            new_strings: set of all possible unique new strings
    """

    new_strings = set()
    for idx in range(len(symbols_list)):
        symbol = symbols_list[idx]
        if not replacements_dict.get(symbol):
            continue
        else:
            possible_replacements = replacements_dict.get(symbol)
            for replacement in possible_replacements:
                new_string = "".join(symbols_list[:idx])
                new_string += replacement
                new_string += "".join(symbols_list[idx+1:])
                new_strings.add(new_string)
    return new_strings

def count_all_strings():
    """Returns number of all possible new strings for Part 1"""

    replacements_dict = make_dict('replacements.txt')
    with open('calibration.txt') as f:
        calib_str = f.readline().strip()
    symbols_list = find_symbols(calib_str)
    new_strings = make_substitutions(symbols_list, replacements_dict)
    return len(new_strings)

# Part 2
def make_new_molecule(start, target, replacements_dict, depth):
    """Returns number of steps required to make target molecule out of start"""
    if depth == 0:
        #print "Start ", start
        #print "Target ", target
        if start == target:
            return True
        else:
            return False
    symbols = find_symbols(start)
    new_strings = make_substitutions(symbols, replacements_dict)
    for new_string in new_strings:
        if make_new_molecule(new_string, target, replacements_dict, depth-1):
            return True
    return False

def find_path(start="e", target="HOH"):

    depth = 0
    replacements_dict = make_dict("test_input2.txt")
    is_found = False
    while not is_found:
        depth += 1
        print depth
        is_found = make_new_molecule(start, target, replacements_dict, depth)
    return depth
