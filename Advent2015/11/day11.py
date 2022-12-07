import re

COMBOS = []
for i in range(97,121):
    combo = chr(i) + chr(i+1) + chr(i+2)
    COMBOS.append(combo)

def iterate_pword(current_password):
    """Get the next possible password starting from the rightmost character"""

    num = _pword_to_num(current_password) # Turn password into list of ints
    for idx in reversed(range(len(num))):
        char_ord = num[idx]
        if char_ord != 122:
            char_ord += 1
            num[idx] = char_ord
            break
        else:
            char_ord = 97
            num[idx] = char_ord
    return _num_to_pword(num)

def _pword_to_num(pword):
    """Changes pword to a list of ord values"""

    return [ord(char) for char in pword]

def _num_to_pword(num):
    """Changes a list of ord values to a string password"""
    pword = ''
    for char in num:
        pword += chr(char)
    return pword

def vet_password(pword):
    while not (increasing_straight(pword) and no_disallowed_letters(pword) and two_pairs(pword)):
        pword=iterate_pword(pword)
    return pword

def increasing_straight(pword):
    """Returns True if there is one increasing straight of at least three letters"""

    combo_finders = [re.compile(combo) for combo in COMBOS]
    for combo_finder in combo_finders:
        if re.search(combo_finder, pword):
            return True
    return False

def no_disallowed_letters(pword):
    """Returns True if pword contains NO disallowed letters: i, l, o"""

    disallowed_finder = re.compile('[ilo]')
    return not bool(re.search(disallowed_finder, pword))

def two_pairs(pword):
    """Returns True if pword contains two different, non-overlapping pairs of letters"""

    last = ''
    count = 1
    counts = []
    for char in pword:
        if char == last:
            char_and_count = counts.pop()
            count = char_and_count.pop()
            updated_count = count + 1
            char_and_count.append(updated_count)
            counts.append(char_and_count)
        elif char != last:
            counts.append([char, count])
        last = char
        count = 1

    distinct_pairs = set()
    for char_and_count in counts:
        if char_and_count[1] >= 2:
            distinct_pairs.update(char_and_count[0])
    if len(distinct_pairs) >= 2:
        return True
    return False
