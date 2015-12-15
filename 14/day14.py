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

def simulate_reindeer(race_time, fly_speed, fly_duration, rest_duration):

    cycle_length = fly_duration + rest_duration
    num_cycles = race_time/cycle_length
    distance = num_cycles * fly_speed * fly_duration
    extra_time = race_time % cycle_length
    if extra_time <= fly_duration:
        distance += (fly_speed * extra_time)
    else:
        distance += (fly_speed * fly_duration)

    return distance

def simulate_race(race_time):
    """Returns name & distance of winning reindeer."""

    reindeer_dict = parse_input()
    distances = {}
    for reindeer, reindeer_stats in reindeer_dict.iteritems():
        fly_speed, fly_duration, rest_duration = reindeer_stats
        distance = simulate_reindeer(race_time, fly_speed, fly_duration, rest_duration)
        distances[reindeer] = distance
    return max(distances.items(), key=lambda x:x[1])


# Part 2
def simulate_race2(race_time):
    """Returns number of points of winning reindeer."""

    reindeer_stats_dict = parse_input()
    points = defaultdict(lambda: 0)
    lead = None

    for i in range(1, race_time+1):
        lead, distance = simulate_race(i)
        points[lead] += 1
    return max(points.items(), key=lambda x:x[1])
