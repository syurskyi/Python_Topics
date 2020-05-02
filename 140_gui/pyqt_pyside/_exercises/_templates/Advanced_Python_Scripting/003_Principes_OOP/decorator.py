___ decorator(f
    ___ wrapper , arg
        print 'before'
        f(arg)
        print 'after'
    return wrapper
@decorator
___ f1 , x
    print 'function', x

f1(12)
