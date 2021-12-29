from functools import wraps
from time import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        answer = func(*args, **kwargs)
        end = time()
        print(f'Elapsed: {end-start}')
        return answer
    return wrapper

def tracer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Entering...')
        func(*args, **kwargs)
        print('Existing....')
    return wrapper


@tracer
@timer
def hello_world(*args, **kwargs):
    print(f'Hello World! {args}')


hello_world()