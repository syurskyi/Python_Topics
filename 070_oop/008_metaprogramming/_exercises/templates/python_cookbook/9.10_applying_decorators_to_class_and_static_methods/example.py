import time
from functools import wraps

# A simple decorator
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return r
    return wrapper

# Class illustrating application of the decorator to different kinds of methods
class Spam:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1

if __name__ == '__main__':
    s = Spam()
    s.instance_method(10000000)
    Spam.class_method(10000000)
    Spam.static_method(10000000)

# Problem
# You want to apply a decorator to a class or static method.
# Solution
# Applying decorators to class and static methods is straightforward, but make sure that
# your decorators are applied before @classmethod or @staticmethod. For example:

# Discussion
# If you get the order of decorators wrong, you’ll get an error. For example, if you use the
# following:

# The problem here is that @classmethod and @staticmethod don’t actually create objects
# that are directly callable. Instead, they create special descriptor objects, as described in
# Recipe 8.9. Thus, if you try to use them like functions in another decorator, the decorator
# will crash. Making sure that these decorators appear first in the decorator list fixes the
# problem.
# One situation where this recipe is of critical importance is in defining class and static
# methods in abstract base classes, as described in Recipe 8.12. For example, if you want
# to define an abstract class method, you can use this code:

# In this code, the order of @classmethod and @abstractmethod matters. If you flip the
# two decorators around, everything breaks.