import collections
import csv

# Part 1

def find_top_calories(filename="input.txt"):
    """Find the elf carrying the most calories

    Input is a list of calories, delimited by a new line for each elf.

    Returns: Max calorie count carried by one elf

    """
    with open(filename, 'r') as f:
        calories_list = []
        total = 0
        for line in f:
            if line == "\n":
                calories_list.append(total)
                total = 0
                continue
            else:
                total += int(line)
    return max(calories_list)

# Part 2
def find_top_three_total(filename="input.txt"):
    """Find the total calories carried by the three top elves

    Input is a list of calories, delimited by a new line for each elf.

    Returns: Sum of top three caloric totals

    """
    with open(filename, 'r') as f:
        calories_list = []
        total = 0
        for line in f:
            if line == "\n":
                calories_list.append(total)
                total = 0
                continue
            else:
                total += int(line)

    return sum(sorted(calories_list)[-3:])

