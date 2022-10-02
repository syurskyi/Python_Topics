# -*- coding: utf-8 -*-

def some_decorator(f):
    def wraps(*args):
        print(f"Calling function ' {f.__name__}'")
        return f(args)

    return wraps

@some_decorator
def decorated_function(x):
    print(f"With argument ' {x}'")

decorated_function(2)

print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')

# Defining a decorator
___ trace f
    ___ wrap $ $$
        print _*[TRACE] func: ?. -n| args: a..| kwargs: k..|*|
        r_ _|$ $$

    r_ ?

# Applying decorator to a function
??
___ add_two x
    r_ ? + 2

# Calling the decorated function
? 3

# Applying decorator to a lambda
print t00|l_____ x x ** 2 | 3

print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')


li.. ma. t..|l_____ x ? * 2 |ra.. 3
