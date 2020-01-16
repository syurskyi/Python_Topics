# %%
'''
### Overriding
'''

# %%
'''
As we saw in the lecture, classes that inherit from another class **inherit** the functionality from the parent class 
(and all parent classes up the chain).
Let's look at what happens when we override the `__str__` method in a custom class (which remember inherits it from 
the `object` class):
'''

# %%
class Person:
    pass

# %%
p = Person()
str(p)

# %%
'''
What happened here is that `str()` tries to call a `__str__` method. Since the `Person` class does not define it, 
Python continues looking up the inheritance chain until it finds it - in this case it finds it in the `object` class, 
so it uses it.
'''

# %%
'''
Now let's override the `__str__` method in the `Person` class:
'''

# %%
class Person:
    def __str__(self):
        return 'Person class'

# %%
p = Person()

# %%
str(p)

# %%
'''
What happens if we implement a `__repr__` method only, and still call the `str()` method:
'''

# %%
class Person:
    def __repr__(self):
        return 'Person()'

# %%
p = Person()

# %%
str(p)

# %%
'''
As you can see it ended calling `__repr__` **in the Person class**, even though we did not have a `__str__` method 
defined - that's because `objects` delegates `str` to `__repr__` which in turn will find it in our class.
'''

# %%
'''
As we discussed in the lecture, in an inheritance chain we have to be very aware of how overrides are handled.
'''

# %%
'''
Let's create a simple chain:
'''

# %%
class Shape:
    def __init__(self, name):
        self.name = name
        
    def info(self):
         return f'Shape.info called for Shape({self.name})'
    
    def extended_info(self):
        return f'Shape.extended_info called for Shape({self.name})'
    
class Polygon(Shape):
    def __init__(self, name):
        self.name = name  # we'll come back to this later in the context of using the super()
        
    def info(self):
        return f'Polygon info called for Polygon({self.name})'

# %%
p = Polygon('square')

# %%
p.info()

# %%
'''
But if we call `extended_info`:
'''

# %%
p.extended_info()

# %%
'''
That makes sense, it uses `extended_info` in the superclass - but now let's add a twist - let's have `extended_info` 
in the `Shape` class also call `info`:
'''

# %%
class Shape:
    def __init__(self, name):
        self.name = name
        
    def info(self):
         return f'Shape.info called for Shape({self.name})'
    
    def extended_info(self):
        return f'Shape.extended_info called for Shape({self.name})', self.info()
    
class Polygon(Shape):
    def __init__(self, name):
        self.name = name  # we'll come back to this later in the context of using the super()
        
    def info(self):
        return f'Polygon.info called for Polygon({self.name})'

# %%
p = Polygon('Square')

# %%
p.info()

# %%
'''
That works the same as before. But what about `extended_info`? Remember it will use the definition in `Shape`, 
which in turn calls `info`. Keep in mind that `self` in that context refers to `p` - a `Polygon` class which overrides 
`info`:
'''

# %%
print(p.extended_info())

# %%
'''
And this is the same mechanism that results in `str(Person)` ending up calling the `__repr__` method in the `Person` 
class instead of the `__repr__` method in the `object` class which would have just printed out the name and memory 
address of the `Person` instance.
'''

# %%
'''
In fact we can see how this happens exactly this way:
'''

# %%
class Person:
    def __str__(self):
        return 'Person.__str__ called'
    
class Student(Person):
    def __repr__(self):
        return 'Student.__repr__ called'

# %%
s = Student()

# %%
str(s)

# %%
repr(s)

# %%
'''
And if we now have `__str__` delegate to `__repr__` instead:
'''

# %%
class Person:
    def __str__(self):
        print('Person.__str__ called')
        return self.__repr__()
    
class Student(Person):
    def __repr__(self):
        return 'Student.__repr__ called'

# %%
s = Student()

# %%
str(s)

# %%
repr(s)

# %%
'''
Basically just keep track of which instance the methods are bound to and always start working you way from there to 
find the "closest" relevant method.
'''

# %%
