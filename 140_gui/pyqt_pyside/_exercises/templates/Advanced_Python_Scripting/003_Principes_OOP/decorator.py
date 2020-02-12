def decorator(f):
    def wrapper(self, arg):
        print 'before'
        f(arg)
        print 'after'
    return wrapper
@decorator
def f1(self, x):
    print 'function', x

f1(12)
