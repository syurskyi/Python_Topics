# %%
'''
### The `__set_name__`  Method
'''

# %%
'''
Starting in Python 3.6, the `__set_name__` method is an additional method defined in the descriptor protocol.
'''

# %%
'''
It gets called once when the descriptor instance is created (so when the class containing it is compiled), 
and passes the property name as the argument.
'''

# %%
'''
Let's see a simple example illustrating this:
'''

# %%
c_ ValidString:
    def __set_name__(self, owner_class, property_name):
        print(f'__set_name__ called: owner={owner_class}, prop={property_name}')

# %%
c_ Person:
    name = ValidString()

# %%
'''
As you can see `__set_name__` was called when the `Person` c_ was created. This is the only time it gets called.
The main advantage of this is that we can capture the property name:
'''

# %%
c_ ValidString:
    def __set_name__(self, owner_class, property_name):
        print(f'__set_name__ called: owner={owner_class}, prop={property_name}')
        self.property_name = property_name
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            print(f'__get__ called for property {self.property_name} '
                  f'of instance {instance}')

# %%
c_ Person:
    first_name = ValidString()
    last_name = ValidString()

# %%
'''
Now watch what happens when we get the property form the instances:
'''

# %%
p = Person()

# %%
p.first_name

# %%
p.last_name

# %%
'''
So basically we know which property name was assigned to the instance of the descriptor. 
That can be handy for messages that can reference the property name, or even storing values in the instance dictionary 
(assuming we can):
'''

# %%
c_ ValidString():
    def __init__(self, min_length):
        self.min_length = min_length
        
    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be a string.')
        if len(value) < self.min_length:
            raise ValueError(f'{self.property_name} must be at least '
                             f'{self.min_length} characters'
                            )
        key = '_' + self.property_name
        setattr(instance, key, value)
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            key = '_' + self.property_name
            return getattr(instance, key, None)

# %%
c_ Person:
    first_name = ValidString(1)
    last_name = ValidString(2)

# %%
p = Person()

# %%
try:
    p.first_name = 'Alex'
    p.last_name = 'M'
except ValueError as ex:
    print(ex)

# %%
'''
Nice to know that `last_name` is the property raising the exception!
'''

# %%
'''
We also used the property name as the basis for an attribute in the instance itself:
'''

# %%
p = Person()
p.first_name = 'Alex'

# %%
p.first_name, p.__dict__

# %%
'''
So although this now fixes the issue we saw at the beginning of this section (having the user specify the property 
name twice), we still have the issue of potentially overwriting an existing instance attribute:
'''

# %%
p = Person()

# %%
p._first_name = 'some data I need to store'

# %%
p.__dict__

# %%
p.first_name = 'Alex'

# %%
p.__dict__

# %%
'''
So that wiped away our data - this is not good, so we need to do something about it.
'''

# %%
'''
How about storing the value in the instance using the exact same name?
'''

# %%
'''
Think back to how instance attributes shadow class attributes:
'''

# %%
class BankAccount:
    apr = 10

# %%
b = BankAccount()

# %%
b.apr, b.__dict__

# %%
b.apr = 20

# %%
b.apr, b.__dict__

# %%
'''
So as you can see, the descriptor is a **class** attribute. So if we store the value under the same name in 
the instance, are we not going to run into this shadowing issue where the attribute will now use the attribute 
in the instance rather than using the class descriptor attribute?
'''

# %%
'''
And the answer is it depends!
Data vs non-data descriptors - that distinction is important, and we'll look at this in the next lectures.
'''

# %%
'''
Let's preview this quickly:
'''

# %%
class ValidString:
    def __init__(self, min_length):
        self.min_length = min_length
        
    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be a string.')
        if len(value) < self.min_length:
            raise ValueError(f'{self.property_name} must be at least '
                             f'{self.min_length} characters'
                            )
        instance.__dict__[self.property_name] = value
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            print (f'calling __get__ for {self.property_name}')
            return instance.__dict__.get(self.property_name, None)

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

# %%
p.__dict__

# %%
'''
So, `first_name` is in the instance dictionary, and we would expect that accessing `first_name` would use 
the instance dictionary:
'''

# %%
p.first_name

# %%
'''
Aha, it used the descriptor!!
Let's look at that in detail next.
'''

# %%
