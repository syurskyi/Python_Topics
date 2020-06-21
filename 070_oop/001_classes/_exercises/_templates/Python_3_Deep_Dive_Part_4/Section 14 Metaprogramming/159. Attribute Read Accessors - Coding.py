# %%
'''
### Attribute Read Accessors
'''

# %%
'''
We saw in the lecture how `__getattribute__` and `__getattr__` work.
'''

# %%
'''
The more common approach is to let Python's default `__getattribute__` method do it's thing, and then override 
`__getattr__` to handle cases where an attribute could not be found.
'''

# %%
'''
#### Overriding `__getattr__`
'''

# %%
'''
Let's first see how the override works:
'''

# %%
'''
If we do not override the `__getattr__` method, here's what happens when we try to look up an non-existent attribute:
'''

# %%
class Person:
    pass

# %%
p = Person()

try:
    p.name
except AttributeError as ex:
    print('AttributeError', ex)

# %%
'''
Now let's override the `__getattr__` method:
'''

# %%
class Person:
    def __getattr__(self, name):
        print(f'__getattribute__ did not find {name}')
        return 'not found!'

# %%
p = Person()
print(p.name)

# %%
'''
As you can see we did not get an `AttributeError`, and our custom `__getattr__` method was called.
'''

# %%
'''
You do have to be careful to avoid infinite recursion though - remember that every attribute lookup that does not exist 
calls the `__getattr__` method, so something like this is going to cause us problems:
'''

# %%
'''
Suppose we want to implement functionality where if an attribute is not found we try to look up the corresponding 
"private" variable, e.g. if `attr` is not found, maybe try to look up `_attr`:
'''

# %%
class Person:
    def __getattr__(self, name):
        print(f'Could not find {name}')
        alt_name = '_' + name
        if getattr(self, alt_name, None) is not None:
            return getattr(self, alt_name)
        else:
            raise AttributeError(f'Could not find {name} or {alt_name}')

# %%
p = Person()

# %%
print(p.age)

# %%
'''
The problem of course is the code `getattr(self, alt_name, None)`.
We have an attribute lookup for `alt_name` which does not exist, so `__getattr__` gets called again. and again.
 and again...
'''

# %%
'''
There's two ways we can fix this issue: reach directly into the instance dictionary, but attributes are not always 
stored in the instance dictionary, so instead we should use the attribute lookup mechanism in the `super()` object:
'''

# %%
class Person:
    def __getattr__(self, name):
        alt_name = '_' + name
        print(f'Could not find {name}, trying {alt_name}...')
        try:
            return super().__getattribute__(alt_name)
        except AttributeError:
            raise AttributeError(f'Could not find {name} or {alt_name}')

# %%
p = Person()

# %%
try:
    p.age
except AttributeError as ex:
    print(type(ex).__name__, ex)

# %%
'''
And of course if we have our class defined thus:
'''

# %%
class Person:
    def __init__(self, age):
        self._age = age
        
    def __getattr__(self, name):
        print(f'Could not find {name}')
        alt_name = '_' + name
        try:
            return super().__getattribute__(alt_name)
        except AttributeError:
            raise AttributeError(f'Could not find {name} or {alt_name}')

# %%
p = Person(100)

# %%
print(p.age)

# %%
'''
Here you can see it succesfully looked up `_age` and returned that for us.
'''

# %%
'''
#### Example 1
'''

# %%
'''
Here we're going to create a class that behaves a little bit like `defaultdict`. 
If an attribute is requested that does not exist, we're going to set in in the instance, to some default value, and then 
return it.
'''

# %%
class DefaultClass:
    def __init__(self, attribute_default=None):
        self._attribute_default = attribute_default
        
    def __getattr__(self, name):
        print(f'{name} not found. creating it and setting it to default...')
        setattr(self, name, self._attribute_default)
        return self._attribute_default

# %%
d = DefaultClass('NotAvailable')

# %%
print(d.test)

# %%
print(d.__dict__)

# %%
'''
And of course, the next time we request it, the `__getattr__` is no longer called:
'''

# %%
print(d.test)

# %%
'''
Which means we can set it to a different value and not have `__getattr__` stomp over the value we set:
'''

# %%
d.test = 'hello'

# %%
print(d.test)

# %%
print(d.__dict__)

# %%
'''
Now that we have this class defined, we could also inherit from it to provide this functionality to other classes:
'''

# %%
class Person(DefaultClass):
    def __init__(self, name):
        super().__init__('Unavailable')
        self.name = name

# %%
p = Person('Raymond')

# %%
print(p.name)

# %%
print(p.age)

# %%
'''
#### Example 2
'''

# %%
'''
Another use case might be logging the fact that a non-existent attribute was requested - sometimes useful in debugging 
complex applications and monitoring things.
When we do that we need to make sure we raise an `AttributeError` from our `__getattr__` method, since we don't actually 
want to provide a value for the attribute (in this particular case):
'''

# %%
class AttributeNotFoundLogger:
    def __getattr__(self, name):
        err_msg = f"'{type(self).__name__}' object has no attribute '{name}'"
        print(f'Log: {err_msg}')
        raise AttributeError(err_msg)

# %%
class Person(AttributeNotFoundLogger):
    def __init__(self, name):
        self.name = name

# %%
p = Person('Raymond')

# %%
print(p.name)

# %%
try:
    p.age
except AttributeError as ex:
    print(f'AttributeError raised: {ex}')

# %%
'''
#### Example 3: Overriding `__getattribute__`
'''

# %%
'''
As we discussed in the lecture, `__getattribute__` is called for **every** attribute access on our object.
'''

# %%
'''
We'll come back to more examples of this, but let's do a simple example, where we want to disallow accessing 
any attribute names that start with an underscore:
'''

# %%
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def __getattribute__(self, name):
        if name.startswith('_'):
            raise AttributeError(f'Forbidden access to {name}')
        return super().__getattribute__(name)

# %%
p = Person('Alex', 19)

# %%
try:
    p._name
except AttributeError as ex:
    print(ex)

# %%
'''
We have a problem now, we don't have access to `_name` and no property for `name`. We could try to reach into 
the instance dictionary (assuming the attribute was stored there):
'''

# %%
print(p.__dict__['_name'])

# %%
'''
Oh-oh... We have another problem - we can't even get to `__dict__`. LOL.
'''

# %%
'''
First let's fix the `__dict__` issue by preventing access to attribute names that start with `_` and not `__`:
'''

# %%
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def __getattribute__(self, name):
        if name.startswith('_') and not name.startswith('__'):
            raise AttributeError(f'Forbidden access to {name}')
        return super().__getattribute__(name)

# %%
p = Person('Eric', 78)

# %%
print(p.__dict__)

# %%
'''
Now let's implement properties for `name` and `age`:
'''

# %%
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def __getattribute__(self, name):
        if name.startswith('_') and not name.startswith('__'):
            raise AttributeError(f'Forbidden access to {name}')
        return super().__getattribute__(name)
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age

# %%
'''
I hope before we even run this, that you realize we are going to have an issue...
'''

# %%
'''
In the properties, what did we do? We accessed `self._name` and `self._age`.
'''

# %%
'''
How is Python going to look up those attributes? By using the `__getattribute__` method - and we just stopped access 
to variables that start with a single underscore!
'''

# %%
p = Person('Python', 42)

# %%
try:
    p.name
except AttributeError as ex:
    print(ex)

# %%
'''
Somehow we need to bypass our custom implementation of `__getattribute__`. And we do that by delegating the attribute 
lookup to `super()` - that will use the standard lookup method (define in `object` in this case), and not our custom 
method.
'''

# %%
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def __getattribute__(self, name):
        if name.startswith('_') and not name.startswith('__'):
            raise AttributeError(f'Forbidden access to {name}')
        return super().__getattribute__(name)
    
    @property
    def name(self):
        return super().__getattribute__('_name')
    
    @property
    def age(self):
        return super().__getattribute__('_age')

# %%
p = Person('Python', 42)

# %%
print(p.name)

# %%
'''
Now let's mix in the functionality we had for `DefaultClass` by inheriting it.
'''

# %%
'''
Here's what that class looked like:
'''

# %%
class DefaultClass:
    def __init__(self, attribute_default=None):
        self._attribute_default = attribute_default
        
    def __getattr__(self, name):
        print(f'{name} not found. creating it and setting it to default...')
        setattr(self, name, self._attribute_default)
        return self._attribute_default

# %%
'''
Now this is going to create some problems if we just use it. Because we are trying to get `self._attribute_default`.
Since our custom `__getattribute__` forbids that, we'll have a problem. So here again, we'll start by delegating back 
to `super()` to use the `__getattribute__` from the parent:
'''

# %%
class DefaultClass:
    def __init__(self, attribute_default=None):
        self._attribute_default = attribute_default
        
    def __getattr__(self, name):
        print(f'{name} not found. creating it and setting it to default...')
        default_value = super().__getattribute__('_attribute_default')
        setattr(self, name, default_value)
        return default_value

# %%
'''
And now we can inherit `DefaultClass`:
'''

# %%
class Person(DefaultClass):
    def __init__(self, name=None, age=None):
        super().__init__('Not Available')
        if name is not None:
            self._name = name
        if age is not None:
            self._age = age
        
    def __getattribute__(self, name):
        if name.startswith('_') and not name.startswith('__'):
            raise AttributeError(f'Forbidden access to {name}')
        return super().__getattribute__(name)
    
    @property
    def name(self):
        return super().__getattribute__('_name')
    
    @property
    def age(self):
        return super().__getattribute__('_age')


# %%
p = Person('Python', 42)

# %%
p.name, p.age

# %%
p.language

# %%
p.__dict__

# %%
'''
### Overriding Class Attribute Accessors
'''

# %%
'''
So far we've been overriding these accessors as instance methods in our class - this means we are dealing with instance 
attribute access.
'''

# %%
'''
What about class attributes instead?
'''

# %%
'''
Since `__getattribute__` and `__getattr__` are always instance methods, this means we need to define them in 
the **metaclass** in order to override our class attribute access.
'''

# %%
class MetaLogger(type):
    def __getattribute__(self, name):
        print('class __getattribute__ called...')
        return super().__getattribute__(name)
    
    def __getattr__(self, name):
        print('class __getattr__ called...')
        return 'Not Found'

# %%
class Account(metaclass=MetaLogger):
    apr = 10

# %%
Account.apr

# %%
Account.apy

# %%
'''
Apart from the fact that we defined these methods in the metaclass, everything else works the same way.
'''

# %%
'''
### Gets called for Method access as well
'''

# %%
'''
When we call our custom methods in a custom class, the method needs to be retrieved from the instance as well - 
so it uses the `__getattribute__` and `__getattr__` methods as well.
'''

# %%
class MyClass:
    def __getattribute__(self, name):
        print(f'__getattribute__ called... for {name}')
        return super().__getattribute__(name)
    
    def __getattr__(self, name):
        print(f'__getattr__ called... for {name}')
        raise AttributeError(f'{name} not found')
    
    def say_hello(self):
        return 'hello'

# %%
m = MyClass()

# %%
m.say_hello()

# %%
m.other()