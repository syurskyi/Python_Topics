# example1.py
#
# Not allowing direct instantiation

class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")

class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print('Spam.grok')

if __name__ == '__main__':
    try:
        s = Spam()
    except TypeError as e:
        print(e)

    Spam.grok(42)

# Problem
# You want to change the way in which instances are created in order to implement singletons,
# caching, or other similar features.
# Solution
# As Python programmers know, if you define a class, you call it like a function to create
# instances. For example:

# If you want to customize this step, you can do it by defining a metaclass and reimplementing
# its __call__() method in some way. To illustrate, suppose that you didn’t want
# anyone creating instances at all:

# In this case, users can call the defined static method, but it’s impossible to create an
# instance in the normal way. For example:

# Now, suppose you want to implement the singleton pattern (i.e., a class where only one
# instance is ever created). That is also relatively straightforward, as shown here:

# Finally, suppose you want to create cached instances, as described in Recipe 8.25. Here’s
# a metaclass that implements it:

# Discussion
# Using a metaclass to implement various instance creation patterns can often be a much
# more elegant approach than other solutions not involving metaclasses. For example, if
# you didn’t use a metaclass, you might have to hide the classes behind some kind of extra
# factory function. For example, to get a singleton, you might use a hack such as the
# following:

# Although the solution involving metaclasses involves a much more advanced concept,
# the resulting code feels cleaner and less hacked together.
# See Recipe 8.25 for more information on creating cached instances, weak references,
# and other details.