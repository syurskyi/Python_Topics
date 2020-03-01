# %%
'''
### Rich Comparisons
'''

# %%
'''
This is quite staightforward. We can choose to implement any number of these rich comparison operators in our classes.
Furthermore, if one comparison does not exist, Python will try to the reverse the operands and the operator 
(and unlike the arithmetic operators, both operands can be of the same type).
Let's use a 2D `Vector` class to check this out:
'''

# %%
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'

# %%
v1 = Vector(0, 0)
v2 = Vector(0, 0)
print(id(v1), id(v2))

# %%
v1 == v2

# %%
'''
By default, Python will use `is` when we do not provide an implementation for `==`. In this case we have two different 
objects, so they do not compare `==`.
Let's change that:
'''

# %%
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'
        
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

# %%
v1 = Vector(1, 1)
v2 = Vector(1, 1)
v3 = Vector(10, 10)

# %%
v1 == v2, v1 is v2

# %%
v1 == v3

# %%
'''
We could even support an equality comparison with  other iterable types. Let's say we want to support equality 
comparisons with tuples:
'''

# %%
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'
        
    def __eq__(self, other):
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

# %%
v1 = Vector(10, 11)

# %%
v1 == (10, 11)

# %%
'''
In fact, although tuples do not implement equality against a `Vector`, it will still work because Python will reflect 
the operation:
'''

# %%
(10, 11) == v1

# %%
'''
We can also implement the other rich comparison operators in the same way.
Let's implement the `<` operator:
'''

# %%
'''
We'll consider a Vector to be less than another vector if it's length (Euclidean) is less than the other.
We're actually going to make use of the `abs` function for this, so we'll define the `__abs__` method as well.
'''

# %%
from math import sqrt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'
        
    def __eq__(self, other):
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented
    
    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)
    
    def __lt__(self, other):
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return abs(self) < abs(other)
        return NotImplemented

# %%
v1 = Vector(0, 0)
v2 = Vector(1, 1)

# %%
v1 < v2

# %%
'''
What's interesting is that `>` between two vectors will work as well:
'''

# %%
v2 > v1

# %%
'''
What happened is that since `__gt__` was not implemented, Python decided to reflect the operation, so instead of 
actually running this comparison:
```v2 > v1```
Python actually ran:

```v1 < v2```
'''

# %%
'''
What about with tuples?
'''

# %%
v1 < (1, 1)

# %%
'''
And the reverse?
'''

# %%
(1, 1) > v1

# %%
'''
That worked too. How about `<=`, since we have `,` and `==` defined, will Python be able to use both to come up with a 
result?
'''

# %%
v1, v2

# %%
try:
    v1 <= v2
except TypeError as ex:
    print(ex)

# %%
'''
Nope - so we have to implement it ourselves. Let's do that:
'''

# %%
from math import sqrt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'
        
    def __eq__(self, other):
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented
    
    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)
    
    def __lt__(self, other):
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return abs(self) < abs(other)
        return NotImplemented
    
    def __le__(self, other):
        return self == other or self < other

# %%
v1 = Vector(0, 0)
v2 = Vector(0, 0)
v3 = Vector(1, 1)

# %%
v1 <= v2

# %%
v1 <= v3

# %%
v1 <= (0.5, 0.5)

# %%
'''
What about `>=`?
'''

# %%
v1 >= v2

# %%
'''
Again, Python was able to reverse the operation:
```v1 >= v2```
and run:
```v2 <= v1```
'''

# %%
'''
We also have the `!=` operator:
'''

# %%
v1 != v2

# %%
'''
How did that work?
Well Python could not find a `__ne__` method, so it delegated to `__eq__` instead:
```
not(v1 == v2)
```
We can easily see this by adding a print statement to our `__eq__` method:
'''

# %%
from math import sqrt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'
        
    def __eq__(self, other):
        print('__eq__ called...')
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented
    
    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)
    
    def __lt__(self, other):
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return abs(self) < abs(other)
        return NotImplemented
    
    def __le__(self, other):
        return self == other or self < other

# %%
v1 = Vector(0, 0)
v2 = Vector(1, 1)

# %%
v1 != v2

# %%
'''
In many cases, we can derive most of the rich comparisons from just two base ones: the `__eq__` and one other one, 
maybe `__lt__`, or `__le__`, etc.
For example, if `==` and `<` is defined, then:
- `a <= b` is `a == b or a < b`
- `a > b` is `b < a`
- `a >= b` is `a == b or b < a`
- `a != b` is `not(a == b)`

On the other hand if we define `==` and `<=`, then:
- `a < b` is `a <= b and not(a == b)`
- `a >= b` is `b <= a`
- `a > b` is `b <= a and not(b == a)`
- `a != b` is `not(a == b)`
'''

# %%
'''
So, instead of us defining all the various methods, we can use the `@total_ordering` decorator in the `functools` 
module, that will work with `__eq__` and **one** other rich comparison method, filling in all the gaps for us:
'''

# %%
from functools import total_ordering

@total_ordering
class Number:
    def __init__(self, x):
        self.x = x
        
    def __eq__(self, other):
        print('__eq__ called...')
        if isinstance(other, Number):
            return self.x == other.x
        return NotImplemented
    
    def __lt__(self, other):
        print('__lt__ called...')
        if isinstance(other, Number):
            return self.x < other.x
        return NotImplemented

# %%
a = Number(1)
b = Number(2)
c = Number(1)

# %%
a < b

# %%
a <= b

# %%
'''
You'll notice that `__eq__` was not called - that's because `a < b` was True, and short-circuit evaluation. 
In this next example though, you'll see both methods are called:
'''

# %%
a <= c

# %%
'''
One thing I want to point out, according to the documentation the `__eq__` is not actually **required**. 
That's because as we saw earlier, all objects have a **default** implementation for `==` based on the memory address. 
That's usually not what we want, so we normally end up defining a custom `__eq__` implementation as well.
'''

# %%
