# %%
'''
### Application - Example 1
'''

# %%
'''
Now let's look at some further examples of using descriptors that provides better better reusability than using 
`property` types (remember the repeated code issue we were trying to solve in the first place!)
'''

# %%
'''
We have already seen that data validation works well with descriptors.
For example, we may want our object attributes to have valid values for some of it's attributes:
'''

# %%
class Int:
    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name
        
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'{self.prop_name} must be an integer.')
        instance.__dict__[self.prop_name] = value
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)
            

# %%
class Float:
    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name
        
    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise ValueError(f'{self.prop_name} must be a float.')
        instance.__dict__[self.prop_name] = value
        
    def __get__(self, instance, value):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)

# %%
class List:
    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name
        
    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise ValueError(f'{self.prop_name} must be a list.')
        instance.__dict__[self.prop_name] = value
        
    def __get__(self, instance, value):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)
        
    

# %%
'''
We can now use these descriptors in multiple class definitions, and as many times as we want in each class:
'''

# %%
class Person:
    age = Int()
    height = Float()
    tags = List()
    favorite_foods = List()

# %%
p = Person()

# %%
try:
    p.age = 12.5
except ValueError as ex:
    print(ex)

# %%
try:
    p.height = 'abc'
except ValueError as ex:
    print(ex)

# %%
try:
    p.tags = 'python'
except ValueError as ex:
    print(ex)

# %%
'''
One thing here, is that I got rather tired of writing the same code multiple times for the descriptor classes! 
(beats having to re-write the same code over and over again that we would have had with properties, but still, 
we can do better than that!)
'''

# %%
'''
So let's rewrite this to be a bit more generic:
'''

# %%
class ValidType:
    def __init__(self, type_):
        self._type = type_
        
    def __set_name__(self, owner_clasds, prop_name):
        self.prop_name = prop_name
        
    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise ValueError(f'{self.prop_name} must be of type '
                             f'{self._type.__name__}'
                            )
        instance.__dict__[self.prop_name] = value
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)

# %%
'''
And now we can achieve the same functionality as before:
'''

# %%
class Person:
    age = ValidType(int)
    height = ValidType(float)
    tags = ValidType(list)
    favorite_foods = ValidType(tuple)
    name = ValidType(str)

# %%
p = Person()

# %%
try:
    p.age = 10.5
except ValueError as ex:
    print(ex)

# %%
try:
    p.height = 10
except ValueError as ex:
    print(ex)

# %%
'''
Now I'd like to allow setting the height to an integer value, since those are a subset of floats 
(in the mathematicel sense). That's easy, all I need to do is to use the `numbers.Real` class:
'''

# %%
import numbers

# %%
isinstance(10.1, numbers.Real)

# %%
isinstance(10, numbers.Real)

# %%
'''
So let's tweak our `Person` class:
'''

# %%
class Person:
    age = ValidType(int)
    height = ValidType(numbers.Real)
    tags = ValidType(list)
    favorite_foods = ValidType(tuple)
    name = ValidType(str)

# %%
p = Person()

# %%
p.height = 10

# %%
p.height