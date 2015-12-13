def iterate_password(current_password):

    num = pword_to_num(current_password) # Turn password into list of ints
    to_change = num.pop()
    if to_change != 122:
        num.append(to_change+1)
    else:
        num.append(ord('a'))
    return num_to_pword(num)

def pword_to_num(pword):
    return [ord(char) for char in pword]

def num_to_pword(num):
    pword = ''
    for char in num:
        pword += chr(char)
    return pword
