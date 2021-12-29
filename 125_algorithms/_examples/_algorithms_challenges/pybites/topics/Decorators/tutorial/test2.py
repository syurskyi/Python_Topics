from functools import wraps

def int_inputs(func):
    @wraps(func)
    def wrapper(*args):
        newargs = [int(a) for a in args]
        return func(*newargs)
    return wrapper




@int_inputs
def add(a,b):
    return a+b

@int_inputs
def subtract(a,b):
    return a-b


print(add('1',2))