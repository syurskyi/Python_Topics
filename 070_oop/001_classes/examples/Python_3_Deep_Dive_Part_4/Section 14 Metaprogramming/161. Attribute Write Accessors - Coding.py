# %%
'''
### Attribute Write Accessors
'''

# %%
'''
As we saw in the lecture there is one special method for attribute writes: `__setattribute__`.
'''

# %%
'''
Let's just see when it gets called:
'''

# %%
class Person:
    def __setattr__(self, name, value):
        print('setting instance attribute...')
        super().__setattr__(name, value)

# %%
p = Person()

# %%
p.name = 'Guido'

# %%
'''
Of course, if we set a class attribute it does not get called:
'''

# %%
Person.class_attr = 'test'

# %%
'''
In order to override this setter for class attributes we would have to define it in the metaclass:
'''

# %%
class MyMeta(type):
    def __setattr__(self, name, value):
        print('setting class attribute...')
        return super().__setattr__(name, value)
    
class Person(metaclass=MyMeta):
    def __setattr__(self, name, value):
        print('setting instance attribute...')
        super().__setattr__(name, value)

# %%
Person.test = 'test'

# %%
p = Person()
p.test = 'test'

# %%
'''
And as we discussed in the lecture, if our `__setattr__` is setting a **data** descriptor, then it calls 
the descriptor's `__set__` method instead:
'''

# %%
class MyNonDataDesc:
    def __get__(self, instance, owner_class):
        print('__get__ called on non-data descriptor...')
        
class MyDataDesc:
    def __set__(self, instance, value):
        print('__set__ called on data descriptor...')
        
    def __get__(self, instance, owner_class):
        print('__get__ called on data descriptor...')

# %%
class MyClass:
    non_data_desc = MyNonDataDesc()
    data_desc = MyDataDesc()
    
    def __setattr__(self, name, value):
        print('__setattr__ called...')
        super().__setattr__(name, value)

# %%
m = MyClass()

# %%
print(m.__dict__)

# %%
m.data_desc = 100

# %%
m.non_data_desc = 200

# %%
print(m.__dict__)

# %%
'''
So `__setattr__` can be used to intercept and customize any attribute set operation on the instance that the method is 
defined for.
'''

# %%
'''
Just as with `__getattr__` or `__getattribute__` we have to extra careful with infinite recursion.
'''

# %%
'''
Suppose we want to disallow setting values for variables that start with a single underscore (but not a double 
underscore). We might try something like this:
'''

# %%
class MyClass:
    def __setattr__(self, name, value):
        print('__setattr__ called...')
        if name.startswith('_') and not name.startswith('__'):
            raise AttributeError('Sorry, this attribute is read-only.')
        setattr(self, name, value)

# %%
m = MyClass()

# %%
'''
This works fine:
'''

# %%
try:
    m._test = 'test'
except AttributeError as ex:
    print(ex)

# %%
'''
But this will not:
'''

# %%
try:
    m.test = 'test'
except RecursionError as ex:
    print(ex)

# %%
'''
And of course this is because the line `self.name = value` we have in `__setattr__` is itself calling `__setattr__`. 
So instead, we have to delegate this back to the parent:
'''

# %%
class MyClass:
    def __setattr__(self, name, value):
        print('__setattr__ called...')
        if name.startswith('_') and not name.startswith('__'):
            raise AttributeError('Sorry, this attribute is read-only.')
        super().__setattr__(name, value)

# %%
m = MyClass()

# %%
m.test = 'test'

# %%
print(m.__dict__)

# %%
'''
So, just as with the getters, when we want to actually get to the attributes in our instance, we just need to 
distinguish wether we want the default way of getting/setting the attribute, or our custom override, and use `super()` 
accordingly. As long as you remember that, you should be fine :-)
'''

# %%
