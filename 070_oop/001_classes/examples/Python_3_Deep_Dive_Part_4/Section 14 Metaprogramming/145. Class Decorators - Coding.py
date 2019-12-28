# %%
'''
### Class Decorators
'''

# %%
'''
Let's come back to decorators.
So far, we have been using decorators to decorate functions - but of course, we could also use them to decorate classes:
'''

# %%
'''
Let's start with a simple example first, like we saw in the lecture:
'''

# %%
def savings(cls):
    cls.account_type = 'savings'
    return cls
    
def checking(cls):
    cls.account_type = 'checking'
    return cls

# %%
class Account:
    pass

@savings
class Bank1Savings(Account):
    pass

@savings
class Bank2Savings(Account):
    pass

@checking
class Bank1Checking(Account):
    pass

@checking
class Bank2Checking(Account):
    pass

# %%
'''
And if we inspect our classes, we'll see that the `account_type` attribute has been injected by the decorator:
'''

# %%
print(Bank1Savings.account_type, Bank1Checking.account_type)

# %%
'''
Of course, we could make even this simple example a little DRYer, by making a parameterized decorator:
'''

# %%
def account_type(type_):
    def decorator(cls):
        cls.account_type = type_
        return cls
    return decorator

# %%
@account_type('Savings')
class Bank1Savings:
    pass

@account_type('Checking')
class Bank1Checking:
    pass

# %%
print(Bank1Savings.account_type, Bank1Checking.account_type)

# %%
'''
We're not restricted to just adding data attributes either.
'''

# %%
'''
Let's create a class decorator to inject a new function into the class before we return it:
'''

# %%
def hello(cls):
    cls.hello = lambda self: f'{self} says hello!'
    return cls

# %%
@hello
class Person:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name

# %%
vars(Person)

# %%
'''
As you can see, the `Person` class now has an attribute `hello` which is a function.
'''

# %%
'''
So, it will then become a bound method when we call it from an instance of `Person`:
'''

# %%
p = Person('Guido')

# %%
p.hello()

# %%
'''
These examples are simple enough to understand what's going on, but not very useful.
'''

# %%
'''
But we can do some interesting things.
'''

# %%
'''
For example, suppose we want to log every call to every callable in some class.
We could certainly do it this way:
'''

# %%
from functools import wraps

def func_logger(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(f'log: {fn.__qualname__}({args}, {kwargs}) = {result}')
        return result
    return inner    

# %%
class Person:
    @func_logger
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @func_logger
    def greet(self):
        return f'Hello, my name is {self.name} and I am {self.age}'

# %%
p = Person('John', 78)

# %%
p.greet()

# %%
'''
But this is kind of tedious if we have many methods in our class. Not very DRY!
'''

# %%
'''
Instead, how about creating a class decorator that will decorate every callable in a given class with the logger 
decorator:
'''

# %%
def class_logger(cls):
    for name, obj in vars(cls).items():
        if callable(obj):
            print('decorating:', cls, name)
            setattr(cls, name, func_logger(obj))
    return cls

# %%
'''
So now we could do this:
'''

# %%
@class_logger
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f'Hello, my name is {self.name} and I am {self.age}'

# %%
vars(Person)

# %%
p = Person('John', 78)

# %%
p.greet()

# %%
'''
Now we have to be a bit careful. Although this class decorator seems to work fine, it will have issues with static and 
class methods!
'''

# %%
@class_logger
class Person:
    @staticmethod
    def static_method():
        print('static_method invoked...')
    
    @classmethod
    def cls_method(cls):
        print(f'cls_method invoked for {cls}...')
        
    def instance_method(self):
        print(f'instance_method invoked for {self}')

# %%
Person.static_method()

# %%
Person.cls_method()

# %%
Person().instance_method()

# %%
'''
You'll notice that in the `cls_method` and `instance_method` cases, the logger printout never showed up! In fact, 
we did not get the message that these methods had been decorated.
'''

# %%
'''
What happened?
'''

# %%
'''
The problem is that static and class methods are not functions, they are actually descriptors, not callables.
'''

# %%
class Person:
    @staticmethod
    def static_method():
        pass

# %%
print(Person.__dict__['static_method'])

# %%
callable(Person.__dict__['static_method'])

# %%
'''
So, they were not decorated at all.
'''

# %%
'''
Which is probably a good thing, because our decorator is expecting to decorate a function, not a class!
'''

# %%
'''
This, by the way, is why when you decorate static or class methods using a function decorator in your classes, 
you should do so before you decorate it with the `@staticmethod` or `@classmethod` decorators:
'''

# %%
class Person:
    @staticmethod
    @func_logger
    def static_method():
        pass

# %%
Person.static_method()

# %%
'''
But if you try it this way around, things aren't so happy:
'''

# %%
class Person:
    @func_logger
    @staticmethod
    def static_method():
        pass

# %%
Person.static_method()

# %%
'''
We can actually fix this problem in our class decorator if we really wanted to.
'''

# %%
'''
Let's first examine two things separately.
First let's make sure we can recognize the type of a class or static method in our class:
'''

# %%
class Person:
    @staticmethod
    def static_method():
        pass
    
    @classmethod
    def class_method(cls):
        pass

# %%
type(Person.__dict__['static_method'])

# %%
type(Person.__dict__['class_method'])

# %%
'''
Next, can we somehow get back to the original function that was wrapped by the `@staticmethod` and `@classmethod` 
decorators?
'''

# %%
'''
The answer is yes, since these are method objects - we've seen this before when we studied the relationship between 
functions and descriptors and how methods were created.
'''

# %%
Person.__dict__['static_method'].__func__

# %%
Person.__dict__['class_method'].__func__

# %%
'''
So now, we could modify our class decorator needs to unwrap any class or static methods, decorate the original function, 
and then re-wrap it with the appropriate `classmethod` or `instancemethod` decorator:
'''

# %%
def class_logger(cls):
    for name, obj in vars(cls).items():
        if callable(obj):
            print('decorating:', cls, name)
            setattr(cls, name, func_logger(obj))
        elif isinstance(obj, staticmethod):
            original_func = obj.__func__
            print('decorating static method', original_func)
            decorated_func = func_logger(original_func)
            method = staticmethod(decorated_func)
            print(method, type(method))
            setattr(cls, name, method)
        elif isinstance(obj, classmethod):
            original_func = obj.__func__
            print('decorating class method', original_func)
            decorated_func = func_logger(original_func)
            method = classmethod(decorated_func)
            setattr(cls, name, method)
    return cls

# %%
@class_logger
class Person:
    @staticmethod
    def static_method(a, b):
        print('static_method called...', a, b)
        
    @classmethod
    def class_method(cls, a, b):
        print('class_method called...', cls, a, b)
        
    def instance_method(self, a, b):
        print('instance_method called...', self, a, b)

# %%
Person.static_method(10, 20)

# %%
Person.class_method(10, 20)

# %%
Person().instance_method(10, 20)

# %%
'''
Not bad... Not what about properties?
'''

# %%
@class_logger
class Person:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name

# %%
'''
Hmm, the property was not decorated...
'''

# %%
'''
Let's see what the type of that property is (you should already know this):
'''

# %%
type(Person.__dict__['name'])

# %%
isinstance(Person.__dict__['name'], property)

# %%
'''
And how do we get the original functions on a property?
'''

# %%
prop = Person.__dict__['name']

# %%
prop.fget

# %%
prop.fset, prop.fdel

# %%
'''
Hmm, so maybe we can decorate the `fget`, `fset`, and `fdel` functions of the property (if they are not `None`).
We can't just replace the functions, because `fget`, `fset` and `fdel` are actually read-only properties themselves, 
that return the original functions. But we could create a new property based off thge original one, substituting our 
decorated getter, setter and deleter.
Recall that the `getter()`, `setter()` and `deleter()` methods are methods that will create a copy of the original 
property, but substitute the `fget`, `fset` and `fdel` methods (that's how these are used as decorators).
'''

# %%
def class_logger(cls):
    for name, obj in vars(cls).items():
        if callable(obj):
            print('decorating:', cls, name)
            setattr(cls, name, func_logger(obj))
        elif isinstance(obj, staticmethod):
            original_func = obj.__func__
            print('decorating static method', original_func)
            decorated_func = func_logger(original_func)
            method = staticmethod(decorated_func)
            print(method, type(method))
            setattr(cls, name, method)
        elif isinstance(obj, classmethod):
            original_func = obj.__func__
            print('decorating class method', original_func)
            decorated_func = func_logger(original_func)
            method = classmethod(decorated_func)
            setattr(cls, name, method)
        elif isinstance(obj, property):
            print('decorating property', obj)
            if obj.fget:
                obj = obj.getter(func_logger(obj.fget))
            if obj.fset:
                obj = obj.setter(func_logger(obj.fset))
            if obj.fdel:
                obj = obj.deleter(func_logger(obj.fdel))
            setattr(cls, name, obj)
    return cls

# %%
@class_logger
class Person:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name

# %%
p = Person('David')

# %%
print(p.name)

# %%
'''
Ha!! Pretty cool...
'''

# %%
'''
Let's make sure it works if we have setters and deleters as well:
'''

# %%
@class_logger
class Person:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @name.deleter
    def name(self):
        print('deleting name...')

# %%
p = Person('David')

# %%
print(p.name)

# %%
p.name = 'Beazley'

# %%
del p.name

# %%
'''
Success!!

A bit mind-bending, but nonetheless, cool stuff!
'''

# %%
'''
Still, this is not perfect... :(
'''

# %%
'''
We can still run into trouble because not every callable is a function that can be decorated:
'''

# %%
@class_logger
class Person:
    class Other:
        def __call__(self):
            print('called instance of Other...')
            
    other = Other()

# %%
'''
So, as you see it decorated both the class `Other` (since classes are callables), and it decorated `other` since we made 
instances of `Other` callable too.
How does that work with the logger though:
'''

# %%
print(Person.Other)

# %%
print(Person.other)

# %%
'''
And that's the problem, because `Other` and `other` are callables, they have been replaced in our class by what comes 
out of the decorator - a function.
'''

# %%
'''
So maybe we can use the `inspect` module to restrict our callables further:
'''

# %%
import inspect

# %%
class MyClass:
    @staticmethod
    def static_method():
        pass
    
    @classmethod
    def cls_method(cls):
        pass
    
    def inst_method(self):
        pass
    
    @property
    def name(self):
        pass
    
    def __add__(self, other):
        pass
    
    class Other:
        def __call__(self):
            pass
        
    other = Other()
    

# %%
keys = ('static_method', 'cls_method', 'inst_method', 'name', '__add__', 'Other', 'other')
inspect_funcs = ('isroutine', 'ismethod', 'isfunction', 'isbuiltin', 'ismethoddescriptor')

# %%
print(keys)

# %%
max_header_length = max(len(key) for key in keys)
max_fname_length = max(len(func) for func in inspect_funcs)
print(format('', f'{max_fname_length}s'), '\t'.join(format(key, f'{max_header_length}s') for key in keys))
for inspect_func in inspect_funcs:
    fn = getattr(inspect, inspect_func)
    inspect_results = (format(str(fn(MyClass.__dict__[key])), f'{max_header_length}s') for key in keys)
    print(format(inspect_func, f'{max_fname_length}s'), '\t'.join(inspect_results))

# %%
'''
As you can see we could use inspect to only pick things that are routines instead of more general callables. Properties, 
static and class methods we are already handling specially, so I'm going to move the callable check last in 
the `if...elif` block so we handle static and class methods first (since they are classified as routines too).
'''

# %%
import inspect

def class_logger(cls):
    for name, obj in vars(cls).items():
        if isinstance(obj, staticmethod):
            original_func = obj.__func__
            print('decorating static method', original_func)
            decorated_func = func_logger(original_func)
            method = staticmethod(decorated_func)
            setattr(cls, name, method)
        elif isinstance(obj, classmethod):
            original_func = obj.__func__
            print('decorating class method', original_func)
            decorated_func = func_logger(original_func)
            method = classmethod(decorated_func)
            setattr(cls, name, method)
        elif isinstance(obj, property):
            print('decorating property', obj)
            if obj.fget:
                obj = obj.getter(func_logger(obj.fget))
            if obj.fset:
                obj = obj.setter(func_logger(obj.fset))
            if obj.fdel:
                obj = obj.deleter(func_logger(obj.fdel))
            setattr(cls, name, obj)
        elif inspect.isroutine(obj):
            print('decorating:', cls, name)
            setattr(cls, name, func_logger(obj))
    return cls

# %%
@class_logger
class MyClass:
    @staticmethod
    def static_method():
        print('static_method called...')
    
    @classmethod
    def cls_method(cls):
        print('class method called...')
    
    def inst_method(self):
        print('instance method called...')
    
    @property
    def name(self):
        print('name getter called...')
    
    def __add__(self, other):
        print('__add__ called...')
    
    class Other:
        def __call__(self):
            print(f'{self}.__call__ called...')
        
    other = Other()
    

# %%
print(MyClass.Other, MyClass.other)

# %%
MyClass.other()

# %%
'''
No log, that was expected.
'''

# %%
MyClass.static_method()

# %%
MyClass.cls_method()

# %%
MyClass().inst_method()

# %%
print(MyClass().name)

# %%
MyClass() + MyClass()

# %%
'''
If we really wanted to, we could also decorate the `Other` class:
'''

# %%
@class_logger
class MyClass:
    @staticmethod
    def static_method():
        print('static_method called...')
    
    @classmethod
    def cls_method(cls):
        print('class method called...')
    
    def inst_method(self):
        print('instance method called...')
    
    @property
    def name(self):
        print('name getter called...')
    
    def __add__(self, other):
        print('__add__ called...')
    
    @class_logger
    class Other:
        def __call__(self):
            print(f'{self}.__call__ called...')
        
    other = Other()
    

# %%
MyClass.other()

# %%
'''
We could also do a bit of DRYing on our decorator code.

First let's handle the static and class methods:
'''

# %%
import inspect

def class_logger(cls):
    for name, obj in vars(cls).items():
        if isinstance(obj, staticmethod) or isinstance(obj, classmethod):
            type_ = type(obj)
            original_func = obj.__func__
            print(f'decorating {type_.__name__} method', original_func)
            decorated_func = func_logger(original_func)
            method = type_(decorated_func)
            setattr(cls, name, method)
        elif isinstance(obj, property):
            print('decorating property', obj)
            if obj.fget:
                obj = obj.getter(func_logger(obj.fget))
            if obj.fset:
                obj = obj.setter(func_logger(obj.fset))
            if obj.fdel:
                obj = obj.deleter(func_logger(obj.fdel))
            setattr(cls, name, obj)
        elif inspect.isroutine(obj):
            print('decorating:', cls, name)
            setattr(cls, name, func_logger(obj))
    return cls

# %%
@class_logger
class MyClass:
    @staticmethod
    def static_method():
        print('static_method called...')
    
    @classmethod
    def cls_method(cls):
        print('class method called...')
    
    def inst_method(self):
        print('instance method called...')
    
    @property
    def name(self):
        print('name getter called...')
    
    def __add__(self, other):
        print('__add__ called...')
    
    @class_logger
    class Other:
        def __call__(self):
            print(f'{self}.__call__ called...')
        
    other = Other()

# %%
MyClass.static_method()

# %%
MyClass.cls_method()

# %%
'''
Finally, let's see if we can clean up the block to handle properties - I don't like these repeated nested if statements 
that basically do the almost same thing:
'''

# %%
import inspect

def class_logger(cls):
    for name, obj in vars(cls).items():
        if isinstance(obj, staticmethod) or isinstance(obj, classmethod):
            type_ = type(obj)
            original_func = obj.__func__
            print(f'decorating {type_.__name__} method', original_func)
            decorated_func = func_logger(original_func)
            method = type_(decorated_func)
            setattr(cls, name, method)
        elif isinstance(obj, property):
            print('decorating property', obj)
            methods = (('fget', 'getter'), ('fset', 'setter'), ('fdel', 'deleter'))
            for prop, method in methods:
                if getattr(obj, prop):
                    obj = getattr(obj, method)(func_logger(getattr(obj, prop)))
            setattr(cls, name, obj)
        elif inspect.isroutine(obj):
            print('decorating:', cls, name)
            setattr(cls, name, func_logger(obj))
    return cls

# %%
@class_logger
class MyClass:
    @staticmethod
    def static_method():
        print('static_method called...')
    
    @classmethod
    def cls_method(cls):
        print('class method called...')
    
    def inst_method(self):
        print('instance method called...')
    
    @property
    def name(self):
        print('name getter called...')
        
    @name.setter
    def name(self, value):
        print('name setter called...')
        
    @name.deleter
    def name(self):
        print('name deleter called...')
    
    def __add__(self, other):
        print('__add__ called...')
    
    @class_logger
    class Other:
        def __call__(self):
            print(f'{self}.__call__ called...')
        
    other = Other()

# %%
print(MyClass().name)

# %%
MyClass().name = 'David'

# %%
del MyClass().name

# %%
