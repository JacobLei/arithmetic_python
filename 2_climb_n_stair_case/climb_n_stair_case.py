
def climb_n(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, 2 * b
    return a
