import json

# Part 1
def convert_json(json_string):
    """Wrapper to convert json to a python obj"""

    jason = json.loads(json_string)
    return jason

def get_number(some_input):

    try:
        num = int(some_input)
    except Exception:
        return False
    return num

def walk(jason):
    """Walks through a complex list"""

    total = 0
    num = get_number(jason)
    # base case
    if num:
        return num
    else:
        if type(jason) == list:
            for item in jason:
                total += walk(item)
        elif type(jason) == dict:
            for item in jason.values():
                total += walk(item)
    return total

def part1():
    """Solves part 1 of day 12"""

    with open('input.txt') as f:
        line = eval(f.readline().strip())
    return walk(line)

# Part 2
def walk2(jason):
    """Walks through a complex list, ignoring dicts containing 'red'"""

    total = 0
    num = get_number(jason)
    # base case
    if num:
        return num
    else:
        if type(jason) == list:
            for item in jason:
                total += walk2(item)
        elif type(jason) == dict:
            if 'red' in jason.values():
                total += 0
            else:
                for item in jason.values():
                    total += walk2(item)
    return total

def part2():
    """Solves part 2 of day 12"""

    with open('input.txt') as f:
        line = eval(f.readline().strip())
    return walk2(line)
