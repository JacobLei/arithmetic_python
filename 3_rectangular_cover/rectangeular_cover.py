
def solution(n):
    if n == 0:
        return 0
    a, b = 1, 1
    for _ in range(n):
        a, b, = b, a + b
    return a
