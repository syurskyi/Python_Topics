from functools import wraps
from time import time

___ timer(func):
    @wraps(func)
    ___ wrapper(*args, **kwargs):
        start = time()
        answer = func(*args, **kwargs)
        end = time()
        print(f'Elapsed: {end-start}')
        return answer
    return wrapper

___ tracer(func):
    @wraps(func)
    ___ wrapper(*args, **kwargs):
        print('Entering...')
        func(*args, **kwargs)
        print('Existing....')
    return wrapper


@tracer
@timer
___ hello_world(*args, **kwargs):
    print(f'Hello World! {args}')


hello_world()