import random
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)

PLUGINS
# {'say_hello': <function say_hello at 0x7f768eae6730>,
#  'be_awesome': <function be_awesome at 0x7f768eae67b8>}

randomly_greet("Alice")
# Using 'say_hello'
# 'Hello Alice  '

globals()
# {..., # Lots of variables not shown here.
#  'say_hello': <function say_hello at 0x7f768eae6730>,
#  'be_awesome': <function be_awesome at 0x7f768eae67b8>,
#  'randomly_greet': <function randomly_greet at 0x7f768eae6840>}