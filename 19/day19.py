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

    symbol_finder = re.compile('[A-Z][a-z]?').finditer
    symbols = []
    for match in symbol_finder(calib_str):
        symbol = calib_str[match.start():match.end()]
        symbols.append(symbol)
    return symbols

def make_substitutions(symbols_list, replacements_dict):

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

    replacements_dict = make_dict('replacements.txt')
    with open('calibration.txt') as f:
        calib_str = f.readline().strip()
    symbols_list = find_symbols(calib_str)
    new_strings = make_substitutions(symbols_list, replacements_dict)
    return len(new_strings)
