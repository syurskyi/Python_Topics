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

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"

make_greeting("Benjamin")
# Calling make_greeting('Benjamin')
# 'make_greeting' returned 'Howdy Benjamin!'
# 'Howdy Benjamin!'

make_greeting("Richard", age=112)
# Calling make_greeting('Richard', age=112)
# 'make_greeting' returned 'Whoa Richard! 112 already, you are growing up!'
# 'Whoa Richard! 112 already, you are growing up!'

make_greeting(name="Dorrisile", age=116)
# Calling make_greeting(name='Dorrisile', age=116)
# 'make_greeting' returned 'Whoa Dorrisile! 116 already, you are growing up!'
# 'Whoa Dorrisile! 116 already, you are growing up!'

