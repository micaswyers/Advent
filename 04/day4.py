import hashlib

# input: iwrupvqb

# Part 1
def find_numbers(secret_key):
    """Given a secret_key, find the lowest positive no. to get MD5 hash that begins with five 0s.

    Args:
        secret_key: string of letters, e.g., 'abcdef',
    Returns:
        num: lowest positive # in decimal that does NOT begin with 0 to produce the MD5 hash.
    """

    num = 1
    m = hashlib.md5(secret_key + str(num)).hexdigest()
    while m[:5] != '00000':
        num += 1
        m = hashlib.md5(secret_key + str(num)).hexdigest()
    return num

# Part 2
def find_numbers2(secret_key):
    """Now looking for the number that produces a hash beginning with six 0s"""

    num = 1
    m = hashlib.md5(secret_key + str(num)).hexdigest()
    while m[:6] != '000000':
        num += 1
        m = hashlib.md5(secret_key + str(num)).hexdigest()
    return num
