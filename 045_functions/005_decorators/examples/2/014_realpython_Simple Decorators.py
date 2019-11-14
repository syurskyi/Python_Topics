def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)

say_whee()

# Something is happening before the function is called.
# Whee!
# Something is happening after the function is called.

# To understand what’s going on here, look back at the previous examples. We are literally just applying everything you have learned so far.
#
# The so-called decoration happens at the following line:

say_whee = my_decorator(say_whee)

print(say_whee)
# <function my_decorator.<locals>.wrapper at 0x7f3c5dfd42f0>

from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)

say_whee()