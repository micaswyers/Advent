from math import sqrt
# Part 1 - 36000000 gifts

def find_house(num_gifts):
    """Given a number of gifts, return the first house that gets at least that many.

        Each elf delivers 10 times its number in gifts.
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

# Part 2

def find_factors2(num):
    """Given num (int), return its factors, that we are calling elves.

        Each elf only visits 50 houses.
    """

    factors = set()
    x = int(sqrt(num))
    for idx in range(1, x + 1):
        if not num % idx:
            if num/idx <= 50:
                factors.add(idx)
            if idx <= 50:
                factors.add(num/idx)
    return factors

def find_house2(num_gifts):
    """Same as part 1, except each elf only visits 50 houses & delivers 11 times
    its number in gifts.

    """

    house = 0
    gifts = 0
    while gifts < num_gifts:
        house += 1
        elves = find_factors2(house)
        gifts = sum(elves) * 11
    return house
