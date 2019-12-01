### file: decorator1.py

class tracer:
    def __init__(self, func):             # On @ decoration: save original func
        self.calls = 0
        self.func = func
    def __call__(self, *args):            # On later calls: run original func
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)

@tracer
def spam(a, b, c):           # spam = tracer(spam)
    print(a + b + c)         # Wraps spam in a decorator object

# from decorator1 import spam

print('#' * 23 + ' Really calls the tracer wrapper object')
spam(1, 2, 3)            # Really calls the tracer wrapper object
# call 1 to spam
# 6
#

print('#' * 23 + ' Invokes __call__ in class')
spam('a', 'b', 'c')      # Invokes __call__ in class
# call 2 to spam
# abc
#
print('#' * 23 + ' Number calls in wrapper state information')
print(spam.calls)               # Number calls in wrapper state information
# 2
print(spam)
# <decorator1.tracer object at 0x02D9A730>
#

calls = 0
def tracer(func, *args):
    global calls
    calls += 1
    print('call %s to %s' % (calls, func.__name__))
    func(*args)
#
def spam(a, b, c):
    print(a, b, c)
#

print('#' * 23 + ' Normal non-traced call: accidental?')
spam(1, 2, 3)            # Normal non-traced call: accidental?
# 1 2 3
#
print('#' * 23 + ' Special traced call without decorators')
tracer(spam, 1, 2, 3)    # Special traced call without decorators
# call 1 to spam
# 1 2 3
#
#