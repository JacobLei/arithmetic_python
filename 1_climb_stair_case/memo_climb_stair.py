
def memo(func):
    cache = {}
    def wrap(*args):        # why need * 
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap
    
    
@memo
def memo_fib(i):
    if i < 2:
        return 1
    return memo_fib(i - 1) + memo_fib(i - 2)