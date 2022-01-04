____ functools _______ wraps
____ time _______ time

___ timer(func):
    @wraps(func)
    ___ wrapper $ $$:
        start = time()
        answer = func $ $$
        end = time()
        print(f'Elapsed: {end-start}')
        r.. answer
    r.. wrapper

___ tracer(func):
    @wraps(func)
    ___ wrapper $ $$:
        print('Entering...')
        func $ $$
        print('Existing....')
    r.. wrapper


@tracer
@timer
___ hello_world $ $$:
    print(f'Hello World! {args}')


hello_world()