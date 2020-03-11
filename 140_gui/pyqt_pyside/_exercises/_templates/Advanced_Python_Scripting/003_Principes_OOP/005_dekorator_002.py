def decorator(f):
    def wrapper():
        print('before')
        f()
        print('after')
    return wrapper

@decorator
def f1():
    print('function')

f1()

def decorator(f):
    def wrapper(arg):
        print('before')
        f(arg)
        print('after')
    return wrapper

@decorator
def f1(x):
    print('function', x)

print()
f1(12)

