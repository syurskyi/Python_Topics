# %%
'''
### Decorator Classes
'''

# %%
'''
I've already covered the topic of decorator classes, but let's review it quickly.
'''

# %%
'''
First off, don't confuse this with class decorators - here I'm talking about using a class to create decorators - that 
can be used to decorate functions, or classes - but instead of the decorator being a function, it is a class whose 
instances will act as decorators.
'''

# %%
'''
We do this by making instances of the decorator class **callable**, by implementing the `__call__` method.
'''

# %%
'''
Let's see a quick example of rewriting a regular decorator function into a decorator class:
'''

# %%
from functools import wraps

def logger(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        print(f'Log: {fn.__name__} called.')
        return fn(*args, **kwargs)
    return wrapped

# %%
'''
And we can use this decorator to log function calls:
'''

# %%
@logger
def say_hello():
    pass

# %%
say_hello()

# %%
'''
We can rewrite this decorator function into a class, by making `__init__` take the function being decorated as 
an argument, and implementing the `__call__` method to actually run the original function (and output the log):
'''

# %%
class Logger:
    def __init__(self, fn):
        self.fn = fn
        
    def __call__(self, *args, **kwargs):
        print(f'Log: {self.fn.__name__} called.')
        return self.fn(*args, **kwargs)

# %%
@Logger
def say_hello():
    pass

# %%
say_hello()

# %%
'''
Remember also that the decorator syntax we used is the same as having done it this way:
'''

# %%
def say_hello():
    pass

# %%
type(say_hello)

# %%
say_hello = Logger(say_hello)

# %%
say_hello()

# %%
'''
But the **big** difference is that `say_hello` is no longer a function, but a **callable** object - an instance of 
the `Logger` class.
'''

# %%
type(say_hello)

# %%
'''
And this actually leads us to an issue.
Let's try to use the same decorator to decorate methods in a class.
We'll start with instance methods first.
'''

# %%
class Person:
    def __init__(self, name):
        self.name = name
        
    @Logger
    def say_hello(self):
        return f'{self.name} says hello!'

# %%
p = Person('David')

# %%
p.say_hello()

# %%
'''
What's going on here? Why is Python complaining that `self` has not been passed to `say_hello`?
We called it from an instance, so why is `self` not being passed to it.
'''

# %%
'''
Well, you have to remember what `say_hello` is now that it has been decorated - it is an instance of a class, not 
a function!
'''

# %%
'''
And do you remember how functions are turned into methods?
'''

# %%
'''
The descriptor protocol... Functions implement a `__get__` method, and that is ultimately used to create the bound 
method.
'''

# %%
'''
Our class does not implement the `__get__` method, so that callable remain a plain callable, not a bound method, 
and that's why our implementation is broken.
'''

# %%
print(p.say_hello)

# %%
'''
But it's actually an easy fix, we can implement the `__get__` method in our class, to turn it into a (non-data) 
descriptor, just like a function does, and we just need to return a bound method.
'''

# %%
'''
Remember how we can create a method bound to an object.
We can use `types.MethodType`. the first argument is the callable we want to bind, and the second argument is 
the instance we want to bind it to.
'''

# %%
from types import MethodType

class Logger:
    def __init__(self, fn):
        self.fn = fn
        
    def __call__(self, *args, **kwargs):
        print(f'Log: {self.fn.__name__} called.')
        return self.fn(*args, **kwargs)
    
    def __get__(self, instance, owner_class):
        print(f'__get__ called: self={self}, instance={instance}')
        if instance is None:
            print('\treturning self unbound...')
            return self
        else:
            # self is callable, since it implements __call__
            print('\treturning self as a method bound to instance')
            return MethodType(self, instance)

# %%
class Person:
    def __init__(self, name):
        self.name = name
        
    @Logger
    def say_hello(self):
        return f'{self.name} says hello!'

# %%
p = Person('David')

# %%
print(p.say_hello)

# %%
'''
As you can see `say_hello` is now considered a bound method. And it bound the callable instance of Logger to 
the Person instance.
'''

# %%
p.say_hello()

# %%
'''
We can still use our `Logger` decorator class to decorate functions, since in that case `__get__` doesn't even come 
into play:
'''

# %%
@Logger
def say_bye():
    pass

# %%
print(say_bye)

# %%
'''
As you can see, the `__get__` method does not even get called.
'''

# %%
'''
The last thing we should check is that the decorator works with class and static methods too.
'''

# %%
'''
Just remember that the order of the decorators is important - we need to decorate with our logger before we decorate 
with the static and class decorators. that way we end up decorating the decorated function (so just a plain fuinction 
decorator), and then making it into a class or static method.
'''

# %%
class Person:
    @classmethod
    @Logger
    def cls_method(cls):
        print('class method called...')
        
    @staticmethod
    @Logger
    def static_method():
        print('static method called...')
        

# %%
Person.cls_method()

# %%
Person.static_method()