from collections import defaultdict

def parse_input():

    reindeer_dict = {}
    with open('input.txt') as f:
        for line in f:
            words = line.split()
            name = words[0]
            fly_speed = int(words[3])
            fly_duration = int(words[6])
            rest_duration = int(words[-2])
            reindeer_dict[name] = (fly_speed, fly_duration, rest_duration)
    return reindeer_dict

def simulate_race():

