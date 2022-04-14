____ f.. _______ w..
____ t__ _______ t__

___ timer(func
    $w.. f..
    ___ wrapper $ $$
        start t__
        answer func $ $$
        end t__
        print _*Elapsed: {end-start}')
        r.. answer
    r.. ?

___ tracer(func
    $w.. f..
    ___ wrapper $ $$
        print('Entering...')
        func $ $$
        print('Existing....')
    r.. ?


@tracer
@timer
___ hello_world $ $$
    print _*Hello World! {args}')


hello_world()