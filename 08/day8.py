def count_code_chars(raw_string):
    """Given raw_string, return the number of characters of CODE that it requires."""
    count = len(raw_string)
    return count

def total_chars():

    return total_code_chars() - total_printed_chars()


def total_code_chars():
    code_chars = 0
    with open('input.txt') as f:
        for raw_string in f:
            code_chars += count_code_chars(raw_string.strip())
    return code_chars

def total_printed_chars():
    chars = 0
    with open('input.txt') as f:
        for line in f:
            chars += len(eval(line.strip()))
    return chars
