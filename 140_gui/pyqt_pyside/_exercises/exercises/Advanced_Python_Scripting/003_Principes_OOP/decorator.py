___ decorator(f
    ___ wrapper , arg
        print 'before'
        f(arg)
        print 'after'
    r_ wrapper
@decorator
___ f1 , x
    print 'function', x

f1(12)
