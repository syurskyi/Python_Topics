# %%
'''
### Decorators and Descriptors - Review
'''

# %%
'''
#### Decorators
'''

# %%
'''
Decorators are in fact a form of metaprogramming.
'''

# %%
'''
Decorators are pieces of code that modify the behavior of another piece of code.
'''

# %%
'''
For example, if we want to write a "super duper debugger", that prints out every function call and the arguments it was 
called with, we can easily modify (decorate) any function we want to "debug" without modifying the function body 
directly:
'''

# %%
from functools import wraps

# %%
def debugger(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        print(f'{fn.__qualname__}', args, kwargs)
        return fn(*args, **kwargs)
    return inner

# %%
'''
And now we can just decorate our functions:
'''

# %%
@debugger
def func_1(*args, **kwargs):
    pass

@debugger
def func_2(*args, **kwargs):
    pass

# %%
func_1(10, 20, kw='a')

# %%
func_2(10)

# %%
'''
The advantage of this decorator approach is that if we want to modify our debugger output, we only need to modify 
the decorator function once, and when we re-run our program the new changes take effect for every decorated function.
'''

# %%
'''
#### Descriptors
'''

# %%
'''
Although it may not seem like it, descriptors are also a form of metaprogramming.
'''

# %%
'''
Descriptors essentially allow us to modify the behavior of the dot (`.`) operator.
'''

# %%
'''
If we have a simple class like so:
'''

# %%
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# %%
'''
Then the dot operator works directly against the object's dictionary (namespace):
'''

# %%
p = Point(10, 20)

# %%
p.x

# %%
p.x=100

# %%
p.__dict__

# %%
'''
So here, `p.x` was basically referencing the instance dictionary. But descriptors allows us to essentially redefine how 
the `.` operator works.
'''

# %%
'''
We saw properties, and properties are based on descriptors, but they are not always conducive to DRY code as we saw 
earlier.
'''

# %%
'''
Let's say we want to provide type checking on the `x` and `y` components of the `Point` class.
'''

# %%
'''
We can use a data descriptor to essentially modify the way the `.` operator works by passing it through getter and 
setter (and deleter) functions - and we also eliminate repetitive code:
'''

# %%
class IntegerField:
    def __set_name__(self, owner, name):
        self.name = name
        
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)
    
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Must be an integer.')
        instance.__dict__[self.name] = value

# %%
class Point:
    x = IntegerField()
    y = IntegerField()
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# %%
p = Point(10, 20)

# %%
p.x, p.y

# %%
try:
    p.x = 10.5
except TypeError as ex:
    print(ex)

# %%
'''
So, without changing the interface of our class, we replaced the default functionality of the `.` operator with another 
piece of code (that implemented the descriptor protocol).
'''

# %%
'''
We'll come back to decorators, and see how we can actually decorate entire classes (so-called **class decorators**).
'''