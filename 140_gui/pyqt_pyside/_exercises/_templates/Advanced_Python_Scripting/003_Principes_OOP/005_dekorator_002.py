___ decorator(f
    ___ wrapper(
        print('before')
        f()
        print('after')
    return wrapper

@decorator
___ f1(
    print('function')

f1()

___ decorator(f
    ___ wrapper(arg
        print('before')
        f(arg)
        print('after')
    return wrapper

@decorator
___ f1(x
    print('function', x)

print()
f1(12)

