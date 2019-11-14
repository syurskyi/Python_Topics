def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice


@do_twice
def greet(name):
    print(f"Hello {name}")

greet("World")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeErr
#or: wrapper_do_twice() takes 0 positional arguments but 1 was given

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")


@do_twice
def say_whee():
    print("Whee!")

say_whee()
# Whee!
# Whee!

greet("World")
# Hello World
# Hello World