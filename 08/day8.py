# Part 1
def total_chars():

    with open('input.txt') as f:
        code_chars = 0
        chars = 0
        for line in f:
            code_chars += len(line.strip())
            chars += len(eval(line.strip()))
        return code_chars - chars
