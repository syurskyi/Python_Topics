# %%
'''
### Properties and Descriptors
'''

# %%
'''
Let's start by creating a property using the decorator syntax:
'''

# %%
from numbers import Integral

class Person:
    @property
    def age(self):
        return getattr(self, '_age', None)
    
    @age.setter
    def age(self, value):
        if not isinstance(value, Integral):
            raise ValueError('age: must be an integer.')
        if value < 0:
            raise ValueError('age: must be a non-negative integer.')
        self._age = value

# %%
p = Person()

# %%
try:
    p.age = -10
except ValueError as ex:
    print(ex)

# %%
'''
And notice how the instance dictionary does not contain `age`, even though we have that instance `age` attribute:
'''

# %%
p.age = 10

# %%
p.age, p.__dict__

# %%
'''
Next, let's rewrite this using a `property` class instead of the decorators:
'''

# %%
class Person:
    def get_age(self):
        return getattr(self, '_age', None)
    
    def set_age(self, value):
        if not isinstance(value, Integral):
            raise ValueError('age: must be an integer.')
        if value < 0:
            raise ValueError('age: must be a non-negative integer.')
        self._age = value
        
    age = property(fget=get_age, fset=set_age)

# %%
'''
And this works the exact same way as before:
'''

# %%
p = Person()

# %%
try:
    p.age = -10
except ValueError as ex:
    print(ex)

# %%
p.age = 10

# %%
p.age, p.__dict__

# %%
'''
Now, in both cases the property object instance can be accessed by using the class:
'''

# %%
prop = Person.age

# %%
prop

# %%
'''
And this property, is actually a data descriptor!
'''

# %%
hasattr(prop, '__set__')

# %%
hasattr(prop, '__get__')

# %%
'''
In this case, our property has both the `__get__` and `__set__` methods so we ended up with a data descriptor.
'''

# %%
'''
Even if we only defined a read-only property, we would still end up with a data descriptor:
'''

# %%
from datetime import datetime

class TimeUTC:
    @property
    def current_time(self):
        return datetime.utcnow().isoformat()

# %%
t = TimeUTC()
t.current_time

# %%
prop = TimeUTC.current_time

# %%
hasattr(prop, '__get__')

# %%
hasattr(prop, '__set__')

# %%
'''
But the internal implemetation of the `__set__` method would refuse to set a value:
'''

# %%
try:
    t.current_time = datetime.utcnow().isoformat()
except AttributeError as ex:
    print(ex)

# %%
'''
So, if properties are implemented using data descriptors - this means that instance attributes with the same name will 
not shadow the descriptor:
'''

# %%
t.__dict__

# %%
t.__dict__['current_time'] = 'not a time'

# %%
t.__dict__

# %%
t.current_time

# %%
'''
OK, so given what we know about data descriptors all this should make sense.
'''

# %%
'''
Now let's try to implement our own version of the property type, decorators and all!
'''

# %%
class MakeProperty:
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset
        
    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name
        
    def __get__(self, instance, owner_class):
        print('__get__ called...')
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError(f'{self.prop_name} is not readable.')
        return self.fget(instance)
            
    def __set__(self, instance, value):
        print('__set__ called...')
        if self.fset is None:
            raise AttributeError(f'{self.prop_name} is not writable.')
        self.fset(instance, value)

# %%
'''
This is now sufficient to start creating properties using this data descriptor:
'''

# %%
class Person:
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        self._name = value
        
    name = MakeProperty(fget=get_name, fset=set_name)

# %%
p = Person()

# %%
p.__dict__

# %%
p.name = 'Guido'

# %%
p.name

# %%
'''
And even if we try to shadow the property name in the instance, things will work just fine:
'''

# %%
p.__dict__['name'] = 'Alex'

# %%
p.__dict__

# %%
p.name

# %%
'''
Next we would like to have a decorator approach as well. To do that we're going to mimic the way the property 
decorators work (you may want to go back to those lectures and refresh your memory if needed).
'''

# %%
'''
So how should the `@MakeProperty` decorator work?
It should take a function and return a descriptor object. 
In turn, that descriptor object should have a `setter` method that we can call to *add* the setter method 
to the descriptor, that also returns the descriptor object - just like we have with `property` types:
'''

# %%
class MakeProperty:
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset
        
    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name
        
    def __get__(self, instance, owner_class):
        print('__get__ called...')
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError(f'{self.prop_name} is not readable.')
        return self.fget(instance)
            
    def __set__(self, instance, value):
        print('__set__ called...')
        if self.fset is None:
            raise AttributeError(f'{self.prop_name} is not writable.')
        self.fset(instance, value)
        
    def setter(self, fset):
        self.fset = fset
        return self
        

# %%
'''
So both the `__init__` and the `setter` methods can be used like decorators, and we can now use our `MakeProperty` 
class with decorator syntax:
'''

# %%
'''
We can do it the "long" way first:
'''

# %%
class Person:
    def get_first_name(self):
        return getattr(self, '_first_name', None)
    
    def set_first_name(self, value):
        self._first_name = value
        
    def get_last_name(self):
        return getattr(self, '_last_name', None)
    
    def set_last_name(self, value):
        self._last_name = value
        
    first_name = MakeProperty(fget=get_first_name, fset=set_first_name)
    last_name = MakeProperty(fget=get_last_name, fset=set_last_name)

# %%
'''
Or, we can use the "shorthand" decorator syntax:
'''

# %%
class Person:
    @MakeProperty
    def first_name(self):
        return getattr(self, '_first_name', None)
    
    @first_name.setter
    def first_name(self, value):
        self._first_name = value
        
    @MakeProperty
    def last_name(self):
        return getattr(self, '_last_name', None)
    
    @last_name.setter
    def last_name(self, value):
        self._last_name = value

# %%
p1 = Person()

# %%
p1.first_name = 'Raymond'

# %%
p1.last_name = 'Hettinger'

# %%
p1.first_name

# %%
p1.last_name

# %%
'''
And of course this will work with multiple instances of the `Person` class since we are using the instances themselves 
for the underlying storage:
'''

# %%
p2 = Person()
p2.first_name, p2.last_name = 'Alex', 'Martelli'

# %%
p1.first_name, p1.last_name, p2.first_name, p2.last_name

# %%
'''
Of course our implementation is quite simplistic, but it should help solidy our understanding of properties, 
descriptors, and decorators too!
'''

# %%
