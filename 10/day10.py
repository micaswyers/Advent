# Part 1
# Input: 3113322113

def count_chars(input_numbers):
    """Given input_numbers, return the counts of consecutive characters

        Args:
            input_numbers: A large int, e.g., 3113322113
        Returns:
            counts: A list of lists. The inner list contains the char (as a string)
                & the number of times in a row that it repeats
                e.g., [['3', 1], ['1', 2], ['3', 2], ['2', 2], ['1', 2], ['3', 1]]
    """

    s = str(input_numbers)
    last = ''
    count = 1
    counts = []
    for idx in range(len(s)):
        current = s[idx]

        if current == last:
            char_and_count = counts.pop()
            count = char_and_count.pop()
            updated_count = count + 1
            char_and_count.append(updated_count)
            counts.append(char_and_count)

        elif current != last:
            counts.append([current, count])
        last = s[idx]
        count = 1
    return counts

def make_next_number(counts_list):
    """Returns new number from list of characters & their consecutive counts"""

    new_number = ''
    for char_stats in counts_list:
        x = str(char_stats[1]) + char_stats[0]
        new_number += x
    return int(new_number)

def look_and_say(start, num_times):
    """Repeat this game for num_times iterations"""

    num = start
    for iteration in range(num_times):
        print "Iteration %s" % (iteration + 1,)
        counts = count_chars(num)
        num = make_next_number(counts)
    return len(str(num))

