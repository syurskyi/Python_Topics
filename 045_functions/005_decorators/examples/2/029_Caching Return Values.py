from decorators import count_calls

@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

fibonacci(10)
# <Lots of output from count_calls>
# 55

fibonacci.num_calls
# 177

import functools
from decorators import count_calls

def cache(func):
    """Keep a cache of previous function calls"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache

@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

fibonacci(10)
# Call 1 of 'fibonacci'
# ...
# Call 11 of 'fibonacci'
# 55

fibonacci(8)
# 21

@functools.lru_cache(maxsize=4)
def fibonacci(num):
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

fibonacci(10)
# Calculating fibonacci(10)
# Calculating fibonacci(9)
# Calculating fibonacci(8)
# Calculating fibonacci(7)
# Calculating fibonacci(6)
# Calculating fibonacci(5)
# Calculating fibonacci(4)
# Calculating fibonacci(3)
# Calculating fibonacci(2)
# Calculating fibonacci(1)
# Calculating fibonacci(0)
# 55

fibonacci(8)
# 21

fibonacci(5)
# Calculating fibonacci(5)
# Calculating fibonacci(4)
# Calculating fibonacci(3)
# Calculating fibonacci(2)
# Calculating fibonacci(1)
# Calculating fibonacci(0)
# 5

fibonacci(8)
# Calculating fibonacci(8)
# Calculating fibonacci(7)
# Calculating fibonacci(6)
# 21

fibonacci(5)
# 5

fibonacci.cache_info()
# CacheInfo(hits=17, misses=20, maxsize=4, currsize=4)