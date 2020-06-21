# %%
'''
### Property Decorators
'''

# %%
'''
As I explain in the lecture video, the `property` callable actually returns itself:
'''

# %%
p = property(fget=lambda self: print('getting property'))

# %%
p

# %%
'''
As you can see `p` is a property, and in fact is the same property that was created.
'''

# %%
'''
Think back to how decorators work:
'''

# %%
def my_decorator(fn):
    print('decorating function')
    def inner(*args, **kwargs):
        print('running decorated function')
        return fn(*args, **kwargs)
    return inner

# %%
def undecorated_function(a, b):
    print('running original function')
    return a + b

# %%
'''
Now we can decorate our undecorated function this way:
'''

# %%
decorated_func = my_decorator(undecorated_function)

# %%
'''
And we can call the decorated function:
'''

# %%
decorated_func(10, 20)

# %%
'''
Now instead of giving the decorate function a new symbol, we could have just re-used the same symbol:
'''

# %%
def my_func(a, b):
    print('running original function')
    return a + b

my_func = my_decorator(my_func)

# %%
my_func(10, 20)

# %%
'''
And of course this is exactly what the decorator `@` syntax does:
'''

# %%
@my_decorator
def my_func(a, b):
    print('running original function')
    return a + b

# %%
my_func(10, 20)

# %%
'''
Ok, now that we've refreshed our memory on decorators, we should be ready to look at the `property` callable.
The `property` callable creates a property object, **and returns it**.
In other words, we could create our property this way, as usual:
'''

# %%
class Person:
    def __init__(self, name):
        self._name = name
        
    def name(self):
        return self._name
    
    name = property(name)

# %%
p = Person('Alex')

p.name

# %%
'''
But you'll notice that line: `name = property(name)` - that's exactly what the decorator syntax does for us!
So instead we can write:
'''

# %%
class Person:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name

# %%
p = Person('Guido')
print(p.name)

# %%
'''
If you refresh your memory on the single dispatch generic function decorator, you'll remember that the decorated
function included another property, the `register` property that was itself a decorator.
Well, the `property` object has some properties, like `setter` that will basically accept a reference to the setter
method, and return itself also.
'''

# %%
p = property(lambda self: 'getter')

# %%
dir(p)

# %%
'''
So, we can "register" and setter method, using the `setter` callable, and get our property back as well:
'''

# %%
p

# %%
p2 = p.setter(lambda self: 'setter')

# %%
id(p), id(p2)

# %%
'''
Now you'll notice that the property id has changed. The setter callable actually creates a new property 
(with both the original getter, and the new setter assigned).
But that does not really matter, we just have a new property object that we can use to assign to a symbol - 
and that property will have both the getter and the setter defined.
Let's do this manually (without the decorator syntax first):
'''

# %%
class Person:
    def __init__(self, name):
        self._name = name
        
    def name(self):
        return self._name
    
    name = property(name)
    
    # creating another symbol that holds on to 
    # the name property
    name_prop = name 
    
    # because herte I'm redefining name, so we lose 
    # our original reference to the property object
    def name(self, value):
        self._name = value
        
    name = name_prop.setter(name)
    
    # finally delete name_prop which we no longer need
    del name_prop

# %%
print(Person.__dict__)

# %%
'''
And we now have a `name` property that we created in two steps: first create the property with just a getter.
Then we replaced our property with a new property that had both the getter and the setter.
'''

# %%
p = Person('Alex')
print(p.name)

# %%
p.name = 'Raymond'
print(p.name)

# %%
'''
Hopefully you can now see where the original property (with just the getter), had a callable `setter` that "added" 
the setter to the property (by creating a new property with both getter and setter), that also returned the (new) 
property object.
So, we can simplify our code this way:
'''

# %%
class Person:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    # what's the property name now? --> name
    # so name has a setter callable
    @name.setter
    def name(self, value):
        self._name = value

# %%
'''
Note that if we had not named our setter function `name` the property name would have changed!
Remember that:
```
@dec
def my_func():
    pass
 ```
 returns a decorated function with the same name as the original function
'''

# %%
print(Person.__dict__)

# %%
p = Person('Alex')

# %%
print(p.name)

# %%
p.name = 'Guido'
print(p.name)

# %%
'''
Just to show you, if we had not used the same name for the setter function:
'''

# %%
class Person:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    # property is now called name
    
    @name.setter
    def full_name(self, value):
        self._name = value

# %%
print(Person.__dict__)

# %%
'''
As you can see we now have two properties on the class! The first one `name` will only work as a getter. 
And the second one `full_name` will work as both a getter and a setter:
'''

# %%
p = Person('Alex')

# %%
print(p.name)

# %%
print(p.full_name)

# %%
p.full_name = 'Raymond'

# %%
print(p.full_name)

# %%
'''
But this won't work:
'''

# %%
try:
    p.name = 'Guido'
except AttributeError as ex:
    print(ex)

# %%
'''
Technically, the property callable has both a getter and setter method - so we can create the setter first, 
then "add in" the getter. But since the first argument to `property` is the getter, we have to work a bit more to do it:
'''

# %%
class Person:
    def __init__(self, name):
        self._name = name
        
    name = property()  # an "empty" prroperty - no getter or setter
    
    @name.setter
    def name(self, value):
        self._name = value

# %%
'''
By the way, we now have a property that can be set, but not read back!
'''

# %%
p = Person('Alex')

# %%
print(p.__dict__)

# %%
p.name = 'Raymond'

# %%
print(p.__dict__)

# %%
try:
    p.name
except AttributeError as ex:
    print(ex)

# %%
'''
So, if you ever need an attribute that is "write-only" - you can do it. Maybe the data is sensitive, and you want 
to set it, but not show back to users... But the data is never truly private, so at best you're obfuscating the data - 
so in my experience I've never had to do something like that. Just wanted you to see this in case the need ever came up.
'''

# %%
'''
But let's finish this up and make the property read/write:
'''

# %%
class Person:
    def __init__(self, name):
        self._name = name
        
    name = property()  # an "empty" prroperty - no getter or setter
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @name.getter
    def name(self):
        return self._name

# %%
p = Person('Alex')

# %%
print(p.name)

# %%
p.name = 'Raymond'

# %%
print(p.name)

# %%
'''
The deleter works the same way, and we'll come back to it soon.
'''

# %%
'''
Lastly you'll recall that we could set up a docstring when using the `property` callable.
The standard technique is to simply define the docstring in the getter function:
'''

# %%
class Person:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        """The Person's name."""
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

# %%
# help(Person.name)

# %%
# help(Person)

# %%
'''
What happens if we set it in the setter instead?
'''

# %%
class Person:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        """The Person's name."""
        self._name = value

# %%
# help(Person.name)

# %%
# help(Person)

# %%
'''
As you can see, the property docstring is only set on the getter. So how to set a docstring with a write-only property? 
We can do that when we create the initial property:
'''

# %%
class Person:
    def __init__(self, name):
        self._name = name
        
    name = property(doc='Write-only name property.')
    
    @name.setter
    def name(self, value):
        self._name = value

# %%
# help(Person.name)

# %%
