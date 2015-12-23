from math import sqrt
# Part 1

def find_house(num_gifts):
    """Given a number of gifts, return the first house that gets at least that many.

        Args:
            num_gifts: int
        Returns:
            house: Number of house receiving at least as many gifts as num_gifts
    """
    house = 0
    gifts = 0
    while gifts < num_gifts:
        house += 1
        elves = find_factors(house)
        gifts = sum(elves) * 10
    return house

def find_factors(num):
    """Given num (int), return its factors, that we are calling elves."""

    factors = set()
    x = int(sqrt(num))
    for idx in range(1, x + 1):
        if not num % idx:
            factors.add(idx)
            factors.add(num/idx)
    return factors
