# Part 1

def count_presents(input_gifts):

    is_found = False
    house_num = 0
    while not is_found:
        house_num += 1
        total = 0
        for idx in range(1,2):
            if not house_num % idx:
                num_presents = idx * 10
                print "House %s gets %s presents" % (house_num, num_presents)
                total += num_presents 
            if total == input_gifts:
                in_found = True
    return total





