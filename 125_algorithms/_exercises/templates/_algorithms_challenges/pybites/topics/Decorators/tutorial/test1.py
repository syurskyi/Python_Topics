____ f.. _______ wraps
____ time _______ time

___ timer(func
    $w.. f..
    ___ wrapper $ $$:
        start = time()
        answer = func $ $$
        end = time()
        print _*Elapsed: {end-start}')
        r.. answer
    r.. wrapper

___ tracer(func
    $w.. f..
    ___ wrapper $ $$:
        print('Entering...')
        func $ $$
        print('Existing....')
    r.. wrapper


@tracer
@timer
___ hello_world $ $$:
    print _*Hello World! {args}')


hello_world()