____ functools _______ wraps
____ time _______ time

___ timer(func):
    @wraps(func)
    ___ wrapper(*args, **kwargs):
        start = time()
        answer = func(*args, **kwargs)
        end = time()
        print(f'Elapsed: {end-start}')
        r.. answer
    r.. wrapper

___ tracer(func):
    @wraps(func)
    ___ wrapper(*args, **kwargs):
        print('Entering...')
        func(*args, **kwargs)
        print('Existing....')
    r.. wrapper


@tracer
@timer
___ hello_world(*args, **kwargs):
    print(f'Hello World! {args}')


hello_world()