# %%
'''
### Property Lookup Resolution
'''

# %%
'''
As we saw in the last set of lectures, something odd is happening when our class uses a data descriptor, 
and instances contain the same attribute name in the instance dictionary.
'''

# %%
'''
Contrary to what we expected, the descriptor was **still** used.
'''

# %%
'''
This boils down to data vs non-data descriptors. Python has a default way of where it looks for attributes depending on 
whether the descriptor is a data-descriptor or not.
'''

# %%
'''
As I explain the lecture video, for data descriptors Python will choose to use the descriptor attribute (in the class), 
even if the same symbol is found in the instance dictionary.
'''

# %%
'''
Let's see this again with a simple example:
'''

# %%
class IntegerValue:
    def __set__(self, instance, value):
        print('__set__ called...')
        
    def __get__(self, instance, owner_class):
        print('__get__ called...')

# %%
class Point:
    x = IntegerValue()

# %%
p = Point()

# %%
p.x = 100

# %%
p.x

# %%
'''
Ok, so the descriptor's `__set__` and `__get__` methods were called.
'''

# %%
'''
Let's set an attribute named `x` directly on the instance dictionary:
'''

# %%
p.__dict__

# %%
p.__dict__['x'] = 'hello'

# %%
p.__dict__

# %%
'''
And now let's get the value:
'''

# %%
p.x

# %%
'''
As you can see the descriptor was **still** used. The same if we set the value:
'''

# %%
p.x = 100

# %%
'''
This works this way because we have a **data descriptor** - the instance attributes do not shadow class descriptors 
of the same name!
'''

# %%
'''
The behavior for a non-data descriptor is different, and the shadowing effect is present:
'''

# %%
from datetime import datetime

class TimeUTC:
    def __get__(self, instance, owner_class):
        print('__get__ called...')
        return datetime.utcnow().isoformat()

# %%
class Logger:
    current_time = TimeUTC()

# %%
l = Logger()

# %%
l.current_time

# %%
'''
As you can see the descriptor's `__get__` was called. 
Now let's inject the same symbol directly into our instance dictionary:
'''

# %%
l.__dict__

# %%
l.__dict__['current_time'] = 'this is not a timestamp'

# %%
l.__dict__

# %%
'''
And if we try to get the value for that key:
'''

# %%
l.current_time

# %%
'''
we get the value stored in the instance dictionary, **not** the descriptor's `__get__` method.
'''

# %%
'''
Of course we can go back to "normal" by removing that key from the instance dictionary:
'''

# %%
del l.__dict__['current_time']

# %%
'''
And now:
'''

# %%
l.current_time

# %%
'''
What this means is that for data descriptors, where we usually need instance-based storage, we can actually use 
the property name itself to store the value in the instance **under the same name**. It will **not** shadow 
the class attribute (the descriptor instance), and it has no risk of overwriting any existing instance attributes 
our class may have!
'''

# %%
'''
Of course, this assume that the class does not use slots, or at least specifies `__dict__` as one of the slots if it 
does.
'''

# %%
'''
Let's apply this to a data descriptor under that assumption:
'''

# %%
class ValidString:
    def __init__(self, min_length):
        self.min_length = min_length
        
    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name
        
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.prop_name} must be a string.')
        if len(value) < self.min_length:
            raise ValueError(f'{self.prop_name} must be '
                             f'at least {self.min_length} characters.'
                            )
        instance.__dict__[self.prop_name] = value
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)

# %%
class Person:
    first_name = ValidString(1)
    last_name = ValidString(2)

# %%
p = Person()

# %%
p.__dict__

# %%
p.first_name = 'Alex'
p.last_name = 'Martelli'

# %%
p.__dict__

# %%
p.first_name, p.last_name

# %%
'''
Note that I am **not** using attributes (either dot notation or `getattr`/`setattr`) when setting and getting 
the values from the instance `__dict__`. If I did, it would actually be calling the descriptors `__get__` and `__set__` 
methods, resulting in an infinite recursion!!
So becareful with that!
'''

# %%
class ValidString:
    def __init__(self, min_length):
        self.min_length = min_length
        
    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name
        
    def __set__(self, instance, value):
        print('calling __set__ ...')
        if not isinstance(value, str):
            raise ValueError(f'{self.prop_name} must be a string.')
        if len(value) < self.min_length:
            raise ValueError(f'{self.prop_name} must be '
                             f'at least {self.min_length} characters.'
                            )
        setattr(instance, self.prop_name, value)
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)

# %%
class Person:
    name = ValidString(1)

# %%
p = Person()

# %%
p.name = 'Alex'

# %%
