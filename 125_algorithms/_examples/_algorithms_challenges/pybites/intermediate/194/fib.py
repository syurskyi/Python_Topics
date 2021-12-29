from functools import lru_cache

@lru_cache
def cached_fib(n):

    if n <= 1:
        return n


    return fib(n - 1) + fib(n - 2)
