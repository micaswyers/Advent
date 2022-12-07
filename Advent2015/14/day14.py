from collections import defaultdict

def parse_input():
    """Returns dict mapping reindeer name to various stats"""

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
    """Simulates a reindeer flying for a given amount of time

    Args:
        race_time: int representing race time in seconds
        fly_speed: int representing num km (per second)
        fly_duration: int representing num seconds the reindeer can fly at a time
        rest_duration: int representing num seconds the reindeer must rest
    Returns:
        distance: int representing distance traveled
    """

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
    """Returns dict containg name(s) & distance of winning reindeer.

        Args:
            race_time: int representing race in seconds
        Returns:
            ex) {'Vixen': 2640, 'Rudolph': 2640}
    """


    reindeer_dict = parse_input()
    distances = {}
    for reindeer, reindeer_stats in reindeer_dict.iteritems():
        fly_speed, fly_duration, rest_duration = reindeer_stats
        distance = simulate_reindeer(race_time, fly_speed, fly_duration, rest_duration)
        distances[reindeer] = distance
    return find_winners(distances)

def find_winners(d):
    """Returns dict of name(s) & distance of winning reindeer

        Args:
            d: dictionary mapping name to distance traveled
        Returns:
            winners: dictionary mapping name to distance for winning reindeer
            ex) {'Vixen': 2640, 'Rudolph': 2640}
    """

    winners = {}
    winner = None
    winning_distance = 0
    for name, distance in d.iteritems():
        if distance > winning_distance:
                winners.clear()
                winners[name] = distance
                winning_distance = distance
        elif distance == winning_distance:
                winners[name] = distance
        elif distance < winning_distance:
                continue
    return winners

# Part 2
def simulate_race2(race_time):
    """Returns dict with name & number of points of winning reindeer.

        Args:
            race_time: int representing time in seconds
        Returns:
            tuple containing name (string) & number of points received (int)
            ex) ("Donner", 1102)
    """

    reindeer_stats_dict = parse_input()
    points = defaultdict(lambda: 0)
    lead = None

    for i in range(1, race_time+1):
        winners_dict = simulate_race(i)
        for winner in winners_dict.keys():
            points[winner] += 1
    return max(points.items(), key=lambda x:x[1])
