import functools

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


@debug
@do_twice
def greet(name):
    print(f"Hello {name}")

greet("Eva")
# Calling greet('Eva')
# Hello Eva
# Hello Eva
# 'greet' returned None

# observe the difference if we change the order of @debug and @do_twice:
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')

greet("Eva")
# Calling greet('Eva')
# Hello Eva
# 'greet' returned None
# Calling greet('Eva')
# Hello Eva
# 'greet' returned None

