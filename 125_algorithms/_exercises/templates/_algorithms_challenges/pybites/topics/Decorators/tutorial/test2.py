from functools import wraps

___ int_inputs(func):
    @wraps(func)
    ___ wrapper(*args):
        newargs = [int(a) for a in args]
        return func(*newargs)
    return wrapper




@int_inputs
___ add(a,b):
    return a+b

@int_inputs
___ subtract(a,b):
    return a-b


print(add('1',2))