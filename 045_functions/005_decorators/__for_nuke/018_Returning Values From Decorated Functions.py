# # -*- coding: utf-8 -*-

# def do_twice(func):
#     def wrapper_do_twice():
#         func()
#         func()
#     return wrapper_do_twice

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

hi_adam = return_greeting("Adam")
# Creating greeting
# Creating greeting
print(hi_adam)
# None

# Oops, your decorator ate the return value from the function.
#
# Because the do_twice_wrapper() doesn’t explicitly return a value, the call return_greeting("Adam")
# ended up returning None.
#
# To fix this, you need to make sure the wrapper function returns the return value of the decorated function.

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

hi_adam = return_greeting("Adam")

return_greeting("Adam")
# Creating greeting
# Creating greeting
# 'Hi Adam'

