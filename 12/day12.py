import json

# Part 1
def convert_json(json_string):
    """Wrapper to convert json to a python obj"""

    jason = json.loads(json_string)

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

# Part 2
