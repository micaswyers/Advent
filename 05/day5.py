# Part 1

def naughty_or_nice(s):
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
    for idx in range(len(s)-1):
        sub_string = s[idx:idx+2]
        print sub_string
        if sub_string in disallowed_strings:
            print "Has a disallowed string"
            return False
        if sub_string[0] == sub_string[1]:
            for vowel in vowels:
                if vowel in s:
                    return True
                else:
                    return False

        else:
            print "No double letters"
            return False
