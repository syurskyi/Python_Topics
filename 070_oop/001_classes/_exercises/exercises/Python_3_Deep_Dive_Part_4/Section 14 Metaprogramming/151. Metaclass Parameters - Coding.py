# %%
'''
### Metaclass Parameters
'''

# %%
'''
When we use a metaclass we typically have something like this:
'''

# %%
class Metaclass(type):
    def __new__(mcls, name, bases, cls_dict):
        return super().__new__(mcls, name, bases, cls_dict)
    
class MyClass(metaclass=Metaclass):
    pass

# %%
type(MyClass), type(MyClass())

# %%
'''
But is there a way to pass *additional* arguments to the metaclass `__new__` method?
'''

# %%
'''
Starting in Python 3.6, the answer is yes. The restriction is that they **must** be passed as named arguments 
(positional args being used for specifying inheritance).
'''

# %%
'''
First let's just try out a simple example to understand the syntax:
'''

# %%
class Metaclass(type):
    def __new__(mcls, name, bases, cls_dict, arg1, arg2, arg3=None):
        print(arg1, arg2, arg3)
        return super().__new__(mcls, name, bases, cls_dict)

# %%
class MyClass(metaclass=Metaclass, arg1=10, arg2=20, arg3=30):
    pass

# %%
class MyClass(metaclass=Metaclass, arg1=10, arg2=20):
    pass

# %%
'''
As you can see our metaclass `__new__` method received those arguments.
'''

# %%
'''
Let's look at a more practical example of this:
'''

# %%
class AutoClassAttrib(type):
    def __new__(cls, name, bases, cls_dict, extra_attrs=None):
        if extra_attrs:
            print('Creating class with some extra attributes: ', extra_attrs)
            # here I'm going to things directly into the cls_dict namespace
            # but could also create the class first, then add using setattr
            for attr_name, attr_value in extra_attrs:
                cls_dict[attr_name] = attr_value
        return super().__new__(cls, name, bases, cls_dict)
                

# %%
class Account(metaclass=AutoClassAttrib, extra_attrs=[('account_type', 'Savings'), ('apr', 0.5)]):
    pass

# %%
vars(Account)

# %%
'''
As you can see the class now has these two extra attributes.
'''

# %%
'''
We could also have just done it this way:
'''

# %%
class AutoClassAttrib(type):
    def __new__(cls, name, bases, cls_dict, extra_attrs=None):
        new_cls = super().__new__(cls, name, bases, cls_dict)
        if extra_attrs:
            print('Creating class with some extra attributes: ', extra_attrs)
            for attr_name, attr_value in extra_attrs:
                setattr(new_cls, attr_name, attr_value)
        return new_cls
                

# %%
class Account(metaclass=AutoClassAttrib, extra_attrs=[('account_type', 'Savings'), ('apr', 0.5)]):
    pass

# %%
vars(Account)

# %%
'''
Of course, we could just use `**kwargs` instead, to make it easier:
'''

# %%
class AutoClassAttrib(type):
    def __new__(cls, name, bases, cls_dict, **kwargs):
        new_cls = super().__new__(cls, name, bases, cls_dict)
        if kwargs:
            print('Creating class with some extra attributes: ', kwargs)
            for attr_name, attr_value in kwargs.items():
                setattr(new_cls, attr_name, attr_value)
        return new_cls
                

# %%
class Account(metaclass=AutoClassAttrib, account_type='Savings', apr=0.5):
    pass

# %%
vars(Account)