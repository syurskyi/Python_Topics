from functools import lru_cache

@lru_cache
___ cached_fib(n):

    __ n <= 1:
        return n


    return fib(n - 1) + fib(n - 2)
