____ functools _______ lru_cache

@lru_cache(maxsize=N..)
___ cached_fib(n):
    __ n < 0:
        r.. ValueError('cannot calculate negative fibonacci numbers')
    __ n < 2:
        r.. n
    ____:
        r.. (cached_fib(n - 1) + cached_fib(n - 2))


__ __name__ __ '__main__':
    ___ x __ r..(11):
        print(f'fib({x}) = {cached_fib(x)}')
