
def get_value(l, r, c):
    return l[r][c]

def find(l, number):
    m = len(l) - 1
    n = len(l[0]) - 1 
    r = 0
    c = n
    while r <= m and c >=0:
        value = get_value(l, r, c)
        if value == number:
            return True
        elif value < number:
            r += 1
        else:
            c -= 1
    return False
