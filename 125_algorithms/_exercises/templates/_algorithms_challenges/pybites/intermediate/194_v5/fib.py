from functools import lru_cache

@lru_cache(maxsize=None)
___ cached_fib(n):
    __ n < 0:
        raise ValueError('cannot calculate negative fibonacci numbers')
    __ n < 2:
        return n
    else:
        return (cached_fib(n - 1) + cached_fib(n - 2))


__ __name__ == '__main__':
    for x in range(11):
        print(f'fib({x}) = {cached_fib(x)}')
