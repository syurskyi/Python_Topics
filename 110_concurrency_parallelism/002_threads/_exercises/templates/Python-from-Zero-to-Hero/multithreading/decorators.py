_______ t___
____ functools _______ wraps


___ async_m...(func):
    @wraps(func)
    async ___ wrap(*args, **kwargs):
        start = t___.perf_counter()
        result = await func(*args, **kwargs)
        elapsed = t___.perf_counter() - start
        print(f'Executed {func} in {elapsed:0.2f} seconds')
        r_ result

    r_ wrap


___ m...(func):
    @wraps(func)
    ___ wrap(*args, **kwargs):
        start = t___.perf_counter()
        result = func(*args, **kwargs)
        elapsed = t___.perf_counter() - start
        print(f'Executed {func} in {elapsed:0.2f} seconds')
        r_ result

    r_ wrap
