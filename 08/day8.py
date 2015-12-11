# Part 1
def total_chars():
    """Given a set of strings, return the difference between # of code chars & chars"""

    with open('input.txt') as f:
        code_chars = 0
        chars = 0
        for line in f:
            code_chars += len(line.strip())
            chars += len(eval(line.strip()))
        return code_chars - chars

# Part 2
def total_chars2():
    """Escape all the escapes!"""

    chars_count = 0
    code_chars = 0
    with open('input.txt') as f:
        for line in f:
            code_chars += len(line.strip())
            line = line.replace("\\", r"\\")
            line = line.replace("\"", r'\"')
            chars_count += (len(line.strip()) + 2)
    return chars_count - code_chars
