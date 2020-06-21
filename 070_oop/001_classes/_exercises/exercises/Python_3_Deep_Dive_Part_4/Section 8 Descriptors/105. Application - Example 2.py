# %%
'''
### Application - Example 2
'''

# %%
'''
Suppose we have a `Polygon` class that has a vertices property that needs to be defined as a sequence 
of `Point2D` instances. So here, not only do we want the `vertices` attribute of our `Polygon` to be an iterable 
of some kind, we also want the elements to all be instances of the `Point2D` class. In turn we'll also want 
to make sure that coordinates for `Point2D` are non-negative integer values (as might be expected in computer screen 
coordinates):
'''

# %%
'''
Let's start by defining the `Point2D` class, but we'll need a descriptor for the coordinates to ensure they are integer 
values, possibly bounded between min and max values:
'''

# %%
class Int:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
        
    def __set_name__(self, owner_class, name):
        self.name = name
        
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'{self.name} must be an int.')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'{self.name} must be at least {self.min_value}')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'{self.name} cannot exceed {self.max_value}')
        instance.__dict__[self.name] = value
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.name, None)

# %%
class Point2D:
    x = Int(min_value=0, max_value=800)
    y = Int(min_value=0, max_value=400)
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Point2D(x={self.x}, y={self.y})'
    
    def __str__(self):
        return f'({self.x}, {self.y})'

# %%
'''
And our `Point2D` class will now only allow integer values within the defined range:
'''

# %%
p = Point2D(0, 10)

# %%
str(p)

# %%
repr(p)

# %%
p.x, p.y

# %%
'''
But:
'''

# %%
try:
    p = Point2D(0, 500)
except ValueError as ex:
    print(ex)

# %%
'''
Next let's create a validator that checks that we have a sequence (mutable or immutable, does not matter) of `Point2D` 
objects. 
'''

# %%
'''
To check of something is a sequence, we can use the abstract base classes defined in the `collections` module:
'''

# %%
import collections

# %%
isinstance([1, 2, 3], collections.abc.Sequence)

# %%
isinstance([1, 2, 3], collections.abc.MutableSequence)

# %%
isinstance((1, 2, 3), collections.abc.Sequence)

# %%
isinstance((1, 2, 3), collections.abc.MutableSequence)

# %%
'''
So let's write the validator:
'''

# %%
class Point2DSequence:
    def __init__(self, min_length=None, max_length=None):
        self.min_length = min_length
        self.max_length = max_length
        
    def __set_name__(self, cls, name):
        self.name = name
        
    def __set__(self, instance, value):
        if not isinstance(value, collections.abc.Sequence):
            raise ValueError(f'{self.name} must be a sequence type.')
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f'{self.name} must contain at least '
                             f'{self.min_length} elements'
                            )
        if self.max_length is not None and len(value) > self.max_length:
            raise ValueError(f'{self.name} cannot contain more than  '
                             f'{self.max_length} elements'
                            )
        for index, item in enumerate(value):
            if not isinstance(item, Point2D):
                raise ValueError(f'Item at index {index} is not a Point2D instance.')
                
        # value passes checks - want to store it as a mutable sequence so we can 
        # append to it later
        instance.__dict__[self.name] = list(value)
        
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            if self.name not in instance.__dict__:
                # current point list has not been defined,
                # so let's create an empty list
                instance.__dict__[self.name] = []
            return instance.__dict__.get(self.name)

# %%
'''
And now we can use this for our `Polygon` class:
'''

# %%
class Polygon:
    vertices = Point2DSequence(min_length=3)
    
    def __init__(self, *vertices):
        self.vertices = vertices

# %%
try:
    p = Polygon()
except ValueError as ex:
    print(ex)

# %%
try:
    p = Polygon(Point2D(-100,0), Point2D(0, 1), Point2D(1, 0))
except ValueError as ex:
    print(ex)

# %%
p = Polygon(Point2D(0,0), Point2D(0, 1), Point2D(1, 0))

# %%
p.vertices

# %%
'''
OK, so, for completeness, let's write a method that we can use to append new points to the vertices list 
(that's why we made it a mutable sequence type!)
'''

# %%
class Polygon:
    vertices = Point2DSequence(min_length=3)
    
    def __init__(self, *vertices):
        self.vertices = vertices
        
    def append(self, pt):
        if not isinstance(pt, Point2D):
            raise ValueError('Can only append Point2D instances.')
        max_length = type(self).vertices.max_length
        if max_length is not None and len(self.vertices) >= max_length:
            # cannot add more points!
            raise ValueError(f'Vertices length is at max ({max_length})')
        self.vertices.append(pt)
                

# %%
p = Polygon(Point2D(0,0), Point2D(1,0), Point2D(0,1))

# %%
p.vertices

# %%
p.append(Point2D(10, 10))

# %%
p.vertices

# %%
'''
Now we could set a `max_length` directly when we define the `Polygon` class:
'''

# %%
class Polygon:
    vertices = Point2DSequence(min_length=3, max_length=3)
    
    def __init__(self, *vertices):
        self.vertices = vertices
        
    def append(self, pt):
        if not isinstance(pt, Point2D):
            raise ValueError('Can only append Point2D instances.')
        max_length = type(self).vertices.max_length
        if max_length is not None and len(self.vertices) >= max_length:
            # cannot add more points!
            raise ValueError(f'Vertices length is at max ({max_length})')
        self.vertices.append(pt)
                

# %%
p = Polygon(Point2D(0,0), Point2D(1,0), Point2D(0,1))

# %%
try:
    p.append(Point2D(10, 10))
except ValueError as ex:
    print(ex)

# %%
'''
But instead, let's use inheritance to create special `Polygon` types!
'''

# %%
'''
First let's go back to our original `Polygon` definition:
'''

# %%
class Polygon:
    vertices = Point2DSequence(min_length=3)
    
    def __init__(self, *vertices):
        self.vertices = vertices
        
    def append(self, pt):
        if not isinstance(pt, Point2D):
            raise ValueError('Can only append Point2D instances.')
        max_length = type(self).vertices.max_length
        if max_length is not None and len(self.vertices) >= max_length:
            # cannot add more points!
            raise ValueError(f'Vertices length is at max ({max_length})')
        self.vertices.append(pt)
                

# %%
class Triangle(Polygon):
    vertices = Point2DSequence(min_length=3, max_length=3)

# %%
'''
So `Triangle` redefines the vertices property, but inherits both the `__init__` and `append` methods:
'''

# %%
p = Polygon(Point2D(0,0), Point2D(1,0), Point2D(0,1))

# %%
p.append(Point2D(10, 10))

# %%
p.vertices

# %%
'''
That works fine, but this does not:
'''

# %%
t = Triangle(Point2D(0,0), Point2D(1,0), Point2D(0,1))

# %%
try:
    t.append(Point2D(10, 10))
except ValueError as ex:
    print(ex)

# %%
'''
And we can also do a square:
'''

# %%
class Square(Polygon):
    vertices = Point2DSequence(min_length=4, max_length=4)

# %%
s = Square(Point2D(0,0), Point2D(1,0), Point2D(0,1), Point2D(1, 1))

# %%
s.vertices

# %%
try:
    s.append(Point2D(10, 10))
except ValueError as ex:
    print(ex)

# %%
'''
We could actually improve this even more by making our `Polygon` class an actual sequence type. To do that we only 
need to implement a few special methods:
'''

# %%
class Polygon:
    vertices = Point2DSequence(min_length=3)
    
    def __init__(self, *vertices):
        self.vertices = vertices
        
    def append(self, pt):
        if not isinstance(pt, Point2D):
            raise ValueError('Can only append Point2D instances.')
        max_length = type(self).vertices.max_length
        if max_length is not None and len(self.vertices) >= max_length:
            # cannot add more points!
            raise ValueError(f'Vertices length is at max ({max_length})')
        self.vertices.append(pt)
                
    def __len__(self):
        return len(self.vertices)
        
    def __getitem__(self, idx):
        return self.vertices[idx]
        

# %%
p = Polygon(Point2D(0,0), Point2D(1,0), Point2D(1,1))

# %%
len(p)

# %%
list(p)

# %%
p[0], p[1], p[2]

# %%
p[0:2]

# %%
'''
We could even implement in-place addition and containment:
'''

# %%
class Polygon:
    vertices = Point2DSequence(min_length=3)
    
    def __init__(self, *vertices):
        self.vertices = vertices
        
    def append(self, pt):
        if not isinstance(pt, Point2D):
            raise ValueError('Can only append Point2D instances.')
        max_length = type(self).vertices.max_length
        if max_length is not None and len(self.vertices) >= max_length:
            # cannot add more points!
            raise ValueError(f'Vertices length is at max ({max_length})')
        self.vertices.append(pt)
                
    def __len__(self):
        return len(self.vertices)
        
    def __getitem__(self, idx):
        return self.vertices[idx]
        
    def __iadd__(self, pt):
        self.append(pt)
        return self
    
    def __contains__(self, pt):
        return pt in self.vertices

# %%
p = Polygon(Point2D(0,0), Point2D(1,0), Point2D(1,1))

# %%
list(p)

# %%
p += Point2D(10, 10)

# %%
list(p)

# %%
'''
What about containment?
'''

# %%
Point2D(0, 0) in p

# %%
'''
Why `False`? The point (0,0) is in the vertices list... 
'''

# %%
'''
Well, we didn't override the `__eq__` method in our `Point2D` class, so it's using the implementation in `object`, 
which uses object identity.

We can easily fix that:
'''

# %%
class Point2D:
    x = Int(min_value=0, max_value=800)
    y = Int(min_value=0, max_value=400)
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Point2D(x={self.x}, y={self.y})'
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __eq__(self, other):
        return isinstance(other, Point2D) and self.x == other.x and self.y == other.y
        
    def __hash__(self):
        return hash((self.x, self.y))

# %%
class Polygon:
    vertices = Point2DSequence(min_length=3)
    
    def __init__(self, *vertices):
        self.vertices = vertices
        
    def append(self, pt):
        if not isinstance(pt, Point2D):
            raise ValueError('Can only append Point2D instances.')
        max_length = type(self).vertices.max_length
        if max_length is not None and len(self.vertices) >= max_length:
            # cannot add more points!
            raise ValueError(f'Vertices length is at max ({max_length})')
        self.vertices.append(pt)
                
    def __len__(self):
        return len(self.vertices)
        
    def __getitem__(self, idx):
        return self.vertices[idx]
        
    def __iadd__(self, pt):
        self.append(pt)
        return self
    
    def __contains__(self, pt):
        return pt in self.vertices

# %%
p = Polygon(Point2D(0,0), Point2D(1,0), Point2D(1,1))

# %%
Point2D(0,0) in p