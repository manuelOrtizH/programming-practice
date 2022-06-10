from functools import wraps

def memoize(fn):
    cache={}
    @wraps(fn)
    def inner(n):
        cache[n] = fn(n) 
        return cache[n]
    return inner

@memoize
def extraLongFactorials(n):
    return 1 if n < 2 else n * factorial(n-1)

if __name__ == '__main__':
    n = 30
    result = factorial(n)
    print(result)