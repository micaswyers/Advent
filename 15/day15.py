# Part 1
from collections import defaultdict

def parse_input(file_name):
    """Returns a dict mapping properties to ingredients & stats

    ex) {
            'capacity': {'sprinkles': 5, 'peanutbutter': -1, 'frosting': 0, 'sugar': -1},
        }
    """

    with open(file_name) as f:
        properties = defaultdict(lambda: {})
        for line in f:
            name_stats = line.split(":")
            ingredient = name_stats[0].lower()
            props = name_stats[1].split(',')
            prop_amounts = [x.strip() for x in props]
            for prop_amount in prop_amounts:
                property_and_amount = prop_amount.split()
                prop = property_and_amount[0]
                amount = int(property_and_amount[1])
                properties[prop][ingredient] = amount
        return properties

def optimize_cookie_points(properties):
    """Returns the highest possible cookie score

    Args:
        properties: dict mapping property to ingredient & multiplier
    Returns:
        int of highest score
    """


    all_scores = []
    properties.pop('calories')
    for num1 in range(101):
        for num2 in range(101-num1):
            for num3 in range(101-num1-num2):
                num4 = (100 - num1 - num2 - num3)
                totals = []
                for prop, ingredient_amount in properties.iteritems():
                    total_prop_score = sum([
                                            num1 * ingredient_amount['sprinkles'],
                                            num2 * ingredient_amount['peanutbutter'],
                                            num3 * ingredient_amount['frosting'],
                                            num4 * ingredient_amount['sugar'],
                                        ])
                    if total_prop_score < 0:
                        total_prop_score = 0
                    totals.append(total_prop_score)
                    total_cookie_score = reduce(lambda x, y: x*y, totals)
                    all_scores.append(total_cookie_score)
    return max(all_scores)



