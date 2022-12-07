MOVES = {
    "A": 1, #rock
    "B": 2, #paper
    "C": 3, #scissors
    "X": 1, #rock
    "Y": 2, #paper
    "Z": 3, #scissors
}

PART1_COMBINATIONS = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3,
}

PART2_COMBINATIONS = {
    # X = lose, Y = draw, Z = win
    "AX": "Z", 
    "AY": "X", 
    "AZ": "Y", 
    "BX": "X", 
    "BY": "Y",
    "BZ": "Z",
    "CX": "Y",
    "CY": "Z",
    "CZ": "X",
}

# Part 1
def calculate_score(filename="input.txt"):
    with open(filename,"r") as f:
        total_score = 0
        for line in f:
            score = 0
            line = line.split()
            them = line[0]
            me = line[1]
            score += MOVES[me]
            score += PART1_COMBINATIONS[f"{them}{me}"]
            total_score += score
    return total_score

# Part 2
def calculate_move(filename="input.txt"):
    with open(filename, "r") as f:
        total_score = 0
        for line in f:
            score = 0
            line = line.split()
            them = line[0]
            my_move = PART2_COMBINATIONS[f"{them}{line[1]}"]
            score += MOVES[my_move]
            score += PART1_COMBINATIONS[f"{them}{my_move}"]
            total_score += score
        return total_score

