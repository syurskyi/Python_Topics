____ f.. _______ lru_cache

@lru_cache(maxsize=N..)
___ cached_fib(n
    __ n < 0:
        r.. V...('cannot calculate negative fibonacci numbers')
    __ n < 2:
        r.. n
    ____:
        r.. (cached_fib(n - 1) + cached_fib(n - 2))


__ _____ __ _____
    ___ x __ r..(11
        print _*fib({x}) = {cached_fib(x)}')
