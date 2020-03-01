# %%
'''
### Metaprogramming - Application 1
'''

# %%
'''
Are you tired of writing boiler-plate code like this:
'''

# %%
class Point2D:
    __slots__ = ('_x', '_y')
    
    def __init__(self, x, y):
        self._x = x
        self._y = y
        
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    def __eq__(self, other):
        return isinstance(other, Point) and (self.x, self.y) == (other.x, other.y)
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __repr__(self):
        return f'Point2D({self.x}, {self.y})'
    
    def __str__(self):
        return f'({self.x}, {self.y})'
        
class Point3D:
    __slots__ = ('_x', '_y', '_z')
    
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    def __eq__(self, other):
        return isinstance(other, Point) and (self.x, self.y, self.z) == (other.x, other.y, other.z)
    
    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __repr__(self):
        return f'Point2D({self.x}, {self.y}, {self.z})'
    
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'


# %%
'''
It's basically the opposite of DRY!
'''

# %%
'''
Let's try to solve this problem using metaclasses (because we might care about inheritance).
'''

# %%
'''
First we are going to define our fields using a class attribute, like so:
'''

# %%
class Point2D:
    _fields = ['x', 'y']
    
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
class Point3D:
    _fields = ['x', 'y', 'z']
    
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

# %%
'''
For now, we'll keep the `__init__` in our classes themselves, but we'll come back to that later.
'''

# %%
'''
Next we are going to define a metaclass that will create the properties and slots, as well as implement the `__eq__`, 
`__hash__`, `__repr__` and `__str__` methods.
'''

# %%
class SlottedStruct(type):
    def __new__(cls, name, bases, class_dict):
        cls_object = super().__new__(cls, name, bases, class_dict)
        
        # setup the __slots__
        setattr(cls_object, '__slots__', [f'_{field}' for field in cls_object._fields])
            
        # create read-only property for each field
        for field in cls_object._fields:
            slot = f'_{field}'
            # this will not work!
            # remember about how closures work! The free variable is resolved when the function is called!
            #     setattr(cls_object, field, property(fget=lambda self: getattr(self, slot)))
            # so instead we have to use this workaround, by specifying the slot as a defaulted argument
            setattr(cls_object, field, property(fget=lambda self, attrib=slot: getattr(self, attrib)))

        return cls_object

# %%
'''
Let's see how this is looking so far:
'''

# %%
class Person(metaclass=SlottedStruct):
    _fields = ['name', 'age']
    
    def __init__(self, name, age):
        self._name = name
        self._age = age

# %%
vars(Person)

# %%
'''
As you can see we have `__slots__` defined, and properties for `name` and `age`. Let's try it out:
'''

# %%
p = Person('Alex', 19)

# %%
print(p.name)

# %%
print(p.age)

# %%
'''
So far so good, now let's continue implementing the rest of the functions:
'''

# %%
class SlottedStruct(type):
    def __new__(cls, name, bases, class_dict):
        cls_object = super().__new__(cls, name, bases, class_dict)
        
        # setup the __slots__
        setattr(cls_object, '__slots__', [f'_{field}' for field in cls_object._fields])
            
        # create read-only property for each field
        for field in cls_object._fields:
            slot = f'_{field}'
            # this will not work!
            #     setattr(cls_object, field, property(fget=lambda self: getattr(self, slot)))
            # Remember about how closures work! The free variable is resolved when the function is called!
            # So instead we have to use this workaround, by specifying the slot as a defaulted argument
            setattr(cls_object, field, property(fget=lambda self, attrib=slot: getattr(self, attrib)))

        # create __eq__ method
        def eq(self, other):
            if isinstance(other, cls_object):
                # ensure each corresponding field is equal
                self_fields = [getattr(self, field) for field in cls_object._fields]
                other_fields = [getattr(other, field) for field in cls_object._fields]
                return self_fields == other_fields
            return False
        setattr(cls_object, '__eq__', eq)

        # create __hash__ method
        def hash_(self):
            field_values = (getattr(self, field) for field in cls_object._fields)
            return hash(tuple(field_values))
        setattr(cls_object, '__hash__', hash_)
        
        # create __str__ method
        def str_(self):
            field_values = (getattr(self, field) for field in cls_object._fields)
            field_values_joined = ', '.join(map(str, field_values))  # make every value a string
            return f'{cls_object.__name__}({field_values_joined})'
        setattr(cls_object, '__str__', str_)
        
        # create __repr__ method
        def repr_(self):
            field_values = (getattr(self, field) for field in cls_object._fields)
            field_key_values = (f'{key}={value}' for key, value in zip(cls_object._fields, field_values))
            field_key_values_str = ', '.join(field_key_values)
            return f'{cls_object.__name__}({field_key_values_str})'
        setattr(cls_object, '__repr__', repr_)
        
        return cls_object

# %%
class Person(metaclass=SlottedStruct):
    _fields = ['name']
    
    def __init__(self, name):
        self._name = name

# %%
'''
Let's try this out:
'''

# %%
type(Person)

# %%
p1 = Person('Alex')
p2 = Person('Alex')

# %%
type(p1), isinstance(p1, Person)

# %%
print(p1 == p2)

# %%
hash(p1), hash(p2)

# %%
repr(p1)

# %%
str(p1)

# %%
'''
And now, we can use this metaclass for any of our other classes too that need to follow the same pattern: slots for all 
the fields, read-only properties for all the fields, and equality, hashing, repr and str as implemented.
'''

# %%
class Point2D(metaclass=SlottedStruct):
    _fields = ['x', 'y']
    
    def __init__(self, x, y):
        self._x = x
        self._y = y
        
class Point3D(metaclass=SlottedStruct):
    _fields = ['x', 'y', 'z']
    
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

# %%
p1 = Point2D(1, 2)
p2 = Point2D(1, 2)
p3 = Point2D(0, 0)

# %%
repr(p1), str(p1), hash(p1), p1.x, p1.y

# %%
repr(p2), str(p2), hash(p2), p2.x, p2.y

# %%
print(p1 is p2, p1 == p2)

# %%
print(p1 is p3, p1 == p3)

# %%
'''
And `Point3D` works exactly the same:
'''

# %%
p1 = Point3D(1, 2, 3)
p2 = Point3D(1, 2, 3)
p3 = Point3D(0, 0, 0)

# %%
print(p1.x, p1.y, p1.z)

# %%
print(p1 == p2, p1 == p3)

# %%
'''
Here's an additional twist!
'''

# %%
'''
I don't like writing `metaclass=SlottedStruct` every time - so I'm going to use a class decorator to do that for me!!
'''

# %%
'''
We already know that a class has properties named `__name__` and `__dict__`.
An additional property it has is `__bases__`:
'''

# %%
print(Point2D.__name__, Point2D.__bases__, Point2D.__dict__)

# %%
'''
So, our class decorator will need to take the class, and rebuild it, but specifying the metaclass we want to use:
'''

# %%
def struct(cls):
    return SlottedStruct(cls.__name__, cls.__bases__, dict(cls.__dict__))

# %%
@struct
class Point2D:
    _fields = ['x', 'y']
    
    def __init__(self, x, y):
        self._x = x
        self._y = y

# %%
type(Point2D)

# %%
p = Point2D(1, 2)

# %%
type(p)

# %%
print(p.x, p.y)

# %%
repr(p)

# %%
'''
All this takes a little bit of getting used to, but the basic concepts are not particularly difficult. The applications 
thereof do mean you have to use just about everything you've learned about Python in this series!
'''

# %%
'''
This was a good exercise to see metaprogramming in action, but as far as this example is concerned we have a much better 
alternative, starting in Python 3.7 - **dataclasses**.

We'll come back to those later.
'''