# %%
'''
### Inheriting from type
'''

# %%
'''
In the last lectures, we saw how classes can be created by calling the `type` class.
But what if we wanted to use something other than `type` to construct classes?
'''

# %%
'''
Since `type` is a class, maybe we could define a class that inherits from `type` (so we can leverage the actual type 
creation process), and override some things that would enable us to inject something in the class creation process.
'''

# %%
'''
Here we want to intercept the creation of the `type` instance before it is created, so we would want to use 
the `__new__` method.
'''

# %%
'''
Remember that the `__new__` method basically needs to build and return the new instance. So we'll do the customizations 
we want, but ultimately we'll punt (delegate) to the `type` class to do the actual work, just adding the tweaks 
(before and/or after the class creation) we want.
'''

# %%
'''
Just a quick reminder of how the static `__new__` method works in general:
'''

# %%
class Test:
    def __new__(cls, *args, **kwargs):
        print(f'New instance of {cls} being created with these values:', args, kwargs)

# %%
t = Test(10, 20, kw='a')

# %%
'''
And it's really the same as doing this:
'''

# %%
Test.__new__(Test, 10, 20, kw='a')

# %%
'''
Of course, it's now up to us to return an object from the `__new__` function.
'''

# %%
'''
So, instead of calling `type` to create the class (type), let's create a custom type generator by subclassing `type`.
We'll inherit from `type`, and override the `__new__` function to create the instance of the class.
'''

# %%
import math

class CustomType(type):
    def __new__(cls, name, bases, class_dict):
        # above is the signature that type.__new__ has - 
        # and args are collected and passed by Python when we call a class (to create an instance of that class)
        # we'll see where those actually come from later
        print('Customized type creation!')
        cls_obj = super().__new__(cls, name, bases, class_dict)  # delegate to super (type in this case)
        cls_obj.circ = lambda self: 2 * math.pi * self.r  # basically attaching a function to the class
        return cls_obj

# %%
'''
Now let's go through the same process to create our `Circle` class that we used in the last lecture, the manual way, 
but using `CustomType` instead of `type`.
'''

# %%
class_body = """
def __init__(self, x, y, r):
    self.x = x
    self.y = y
    self.r = r

def area(self):
    return math.pi * self.r ** 2
"""

# %%
'''
And we create our class dictionary by executing the above code in the context of that dictionary:
'''

# %%
class_dict = {}
exec(class_body, globals(), class_dict)

# %%
'''
Then we create the `Circle` class:
'''

# %%
Circle = CustomType('Circle', (), class_dict)

# %%
'''
We basically customized the class creation, and `Circle` is just a standard object, but, as you can see below, the type 
of our class is no longer `type`, but `CustomType`.
'''

# %%
type(Circle)

# %%
'''
Of course, `Circle` is still an instance of `type` since `CustomType` is a subclass of `type`:
'''

# %%
isinstance(Circle, CustomType), issubclass(CustomType, type)

# %%
'''
And just like before, `Circle` still has the `__init__` and `area` methods:
'''

# %%
hasattr(Circle, '__init__'), hasattr(Circle, 'area')

# %%
'''
So we can use `Circle` just as normal:
'''

# %%
c = Circle(0, 0, 1)

# %%
c.area()

# %%
'''
Additionally, we injected a new function, `circ`, into the class while we were constructing it in the `__new__` method 
of `CustomType`:
'''

# %%
hasattr(Circle, 'circ')

# %%
c.circ()

# %%
'''
So, this is another example of metaprogramming!
'''

# %%
'''
But yeah, creating classes (types) this way is a bit tedious!!!
'''

# %%
'''
This is where the concept of a `metaclass` comes in, which we'll cover in the next set of lectures.
'''