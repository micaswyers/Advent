import hashlib

def find_numbers(secret_key):
    """Given a secret_key, find the lowest positive no. to get MD5 hash.

    Args:
        secret_key: string of letters, e.g., 'abcdef',
    Returns:
        num: lowest positive # in decimal that does NOT begin with 0 to produce the MD5 hash.
    """

    num = 1
    m = hashlib.md5(secret_key + str(num)).hexdigest()
    while m[0-4] != '00000':
        print num
        m = hashlib.md5(secret_key + str(num)).hexdigest()
        print m
        num += 1
    return num

