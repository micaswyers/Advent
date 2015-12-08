# Part 1

def is_nice(s):
    """Determines if a string is naughty or nice based on bizarre criteria

    Nice strings:
        - Contain at least three vowels
        - Contain at least one doubled letter
        - Do NOT contain ab, cd, pq, or xy, even in conjunction w/ other reqs.

    Args:
        s: some string
    Returns:
        Boolean (if string is nice)
    """
    disallowed_strings = ['ab', 'cd', 'pq', 'xy']
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    double_count = 0

    for idx in range(len(s)):
        if s[idx] in vowels:
            vowel_count += 1

        sub_string = s[idx:idx+2]
        if len(sub_string) < 2:
            break
        if sub_string[0] == sub_string[1]:
            double_count += 1
        if sub_string in disallowed_strings:
            return False
    if vowel_count < 3:
        return False
    if double_count < 1:
        return False
    return True

def naughty_or_nice():
    """Returns number of nice strings"""

    num_nice_strings = 0
    with open('input.txt') as f:
        for line in f:
            if is_nice(line):
                num_nice_strings += 1
    return num_nice_strings

