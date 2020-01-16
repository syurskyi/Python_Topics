# %%
'''
### Functions and Descriptors
'''

# %%
'''
As I mentioned in the lecture video, Python functions actually implement the non-data descriptor protocol, i.e. 
they implement the `__get__` method
'''

# %%
def add(a, b):
    return a + b

# %%
hasattr(add, '__get__')

# %%
'''
So what does that `__get__` actually return?
'''

# %%
'''
We know the arguments for `__get__` are `self, instance, owner_class`, so let's try to call the `__get__` method with 
`instance` set to `None` and `owner_class` set to our main module:
'''

# %%
import sys

# %%
me = sys.modules['__main__']

# %%
p = add.__get__(None, me)

# %%
p, id(p)

# %%
add, id(add)

# %%
'''
As you can see, when `instance` is `None`, the `__get__` method just returns the function itself, with owner set 
to `__main__` in this case.
'''

# %%
'''
Now let's see what happens when we define a function inside a class:
'''

# %%
class Person:
    def __init__(self, name):
        self.name = name
        
    def say_hello(self):
        return f'{self.name} says hello'

# %%
'''
Let's first access the `say_hello` callable from the class:
'''

# %%
Person.say_hello

# %%
'''
As you can see the owner class is now `__main__.Person`, and we get a plain function back.
'''

# %%
'''
What essentially happened is that when we retrieved the attribute `say_hello` from the `Person` class, 
since functions are descriptors, Python called the `__get__` method, in this case with `instance` set to `None`, 
and the owner class set to the `Person` class.
'''

# %%
'''
And when we call it from an instance:
'''

# %%
p = Person('Alex')

# %%
hex(id(p))

# %%
p.say_hello

# %%
'''
Again, since `say_hello` is actually a descriptor, Python invoked the `__get__` method, this time with an instance 
(`p`) and with owner class set to `Person`.
The descriptor then returns a method object, which it binds to the instance.
'''

# %%
'''
So we could retrieve it this way too:
'''

# %%
bound_method = Person.say_hello.__get__(p, Person)

# %%
bound_method

# %%
p.say_hello()

# %%
bound_method()

# %%
'''
So the question is, since `p.say_hello`, a non-data descriptor, does not return a function, but a `method` object, 
where is the *actual* function stored?
'''

# %%
'''
Turns out methods have a special attribute, `__func__` that is is used to keep a reference to the original function 
that can then be called when needed:
'''

# %%
p.say_hello.__func__, id(p.say_hello.__func__)

# %%
'''
As you can see, `__func__` is a reference to the `say_hello` function object defined in the `Person` class, 
and to make sure we can do this:
'''

# %%
p.say_hello.__func__ is Person.say_hello

# %%
'''
We could try to mimic this behavior ourselves by writing our own descriptor. The problem is that we need 
to define a function using Python functions, so this is a bit circular, but we can try to somewhat mimic 
instance methods to gain a better understanding of how they work.
'''

# %%
'''
Let's say we want to mimic something like this:
'''

# %%
class Person:
    def __init__(self, name):
        self.name = name
        
    def say_hello(self):
        return f'{self.name} says hello!'

# %%
'''
We want to write a descriptor to replace `say_hello`.
First we're going to write a plain function, directly in our main module:
'''

# %%
def say_hello(self):
    if self and hasattr(self, 'name'):
        return f'{self.name} says hello!'
    else:
        return 'Hello!'

# %%
'''
Now we can call this as an ordinary function:
'''

# %%
say_hello(None)

# %%
'''
But what we really want is to make a descriptor that either returns the function itself when accessed via the class it is contained in (`Person` in this case), or a bound method when it is accessed via an instance of that class.
'''

# %%
'''
First a slight detour to look at method types.
'''

# %%
'''
A `method` is an actual type in Python, and it is available in the `types` module:
'''

# %%
import types

# %%
help(types.MethodType)

# %%
'''
As we can see the constructor for the `MethodType` requires a function, and an object to bind it to.
'''

# %%
'''
Let's try this out:
'''

# %%
class Person:
    def __init__(self, name):
        self.name = name

# %%
p = Person('Alex')
m = types.MethodType(say_hello, p)

# %%
p, m

# %%
'''
As we can see, `m` is a `method` object, bound to the object `p`. And we can call this method:
'''

# %%
m()

# %%
'''
Ok, so now we can start planning how we are going to implement our descriptor.
When the `__get__` method is called from the class, we will want to return the plain `say_hello` function. 
But when `__get__` is called from an instance we'll want to return a method object bound to the specific instance.
'''

# %%
class MyFunc:
    def __init__(self, func):
        self._func = func
    
    def __get__(self, instance, owner):
        if instance is None:
            # called from class
            print('__get__ called from class')
            return self._func
        else:
            # called from instance
            print('__get__ called from an instance')
            return types.MethodType(self._func, instance)

# %%
'''
I made a slight tweak here to allow us to specify any function we want in the init - this make this descriptor 
a little more generic.
'''

# %%
'''
Now let's go ahead and use that in a class:
'''

# %%
def hello(self):
    print(f'{self.name} says hello!')
    
class Person:
    def __init__(self, name):
        self.name = name
        
    say_hello = MyFunc(hello)

# %%
'''
Now let's see what happens when we access `say_hello` from the class:
'''

# %%
Person.say_hello

# %%
'''
We get the original function back.
And when we access it from an instance of `Person`:
'''

# %%
p = Person('Alex')
p.say_hello

# %%
'''
We get a bound method.
'''

# %%
p.say_hello()

# %%
'''
Moreover, the original function `hello` is referenced by the bound method:
'''

# %%
p.say_hello.__func__

# %%
'''
Hopefully it is now a little clearer how methods actually work in Python!
'''