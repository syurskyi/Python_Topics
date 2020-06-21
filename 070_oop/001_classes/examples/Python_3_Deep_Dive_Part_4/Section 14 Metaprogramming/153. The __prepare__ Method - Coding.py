# %%
'''
### The `__prepare__` Method
'''

# %%
'''
We know that when we create a class, the metaclass `__new__` method is invoked with an argument (`cls_dict`) 
for the class dictionary. It is not in fact an empty dictionary at first:
'''

# %%
class MyMeta(type):
    def __new__(mcls, name, bases, cls_dict, **kwargs):
        print('MyMeta.__new__ called...')
        print('\tcls: ', mcls, type(mcls))
        print('\tname:', name, type(name))
        print('\tbases: ', bases, type(bases))
        print('\tcls_dict:', cls_dict, type(cls_dict))
        print('\tkwargs:', kwargs)
        return super().__new__(mcls, name, bases, cls_dict)

# %%
class MyClass(metaclass=MyMeta):
    pass

# %%
'''
So, as we see, `cls_dict` is a dictionary and it also contains some information already. It is obviously being created 
somewhere before being passed to the `__new__` method.
'''

# %%
'''
The class dictionary is actually created by calling the `__prepare__` method, which the `type` class implements.
When the class is created, Python calls `__prepare__` and uses the return value of that method as the initialized class 
dictionary.
Then right before calling `__new__` it adds a few items into that dictionary, and then calls the `__new__` method using 
that pre-created and initialized dictionary.
'''

# %%
'''
Since `__prepare__` is just a method in `type`, we can override it.
'''

# %%
class MyMeta(type):
    @staticmethod
    def __prepare__(name, bases, **kwargs):
        print('MyMeta.__prepare__ called...')
        print('\tname:', name)
        print('\tkwargs:', kwargs)
        return {'a': 100, 'b': 200}
    
    def __new__(mcls, name, bases, cls_dict, **kwargs):
        print('MyMeta.__new__ called...')
        print('\tcls: ', mcls, type(mcls))
        print('\tname:', name, type(name))
        print('\tbases: ', bases, type(bases))
        print('\tcls_dict:', cls_dict, type(cls_dict))
        print('\tkwargs:', kwargs)
        return super().__new__(mcls, name, bases, cls_dict)

# %%
class MyClass(metaclass=MyMeta, kw1=10, kw2=20):
    pass

# %%
'''
Notice how the `__prepare__` method was called **before** the `__new__` method was called.
'''

# %%
'''
Also notice how it contains the items `'a': 100` and `'b': 200` which we injected in the `__prepare__` method.
The `cls_dict` argument in `__new__` has a couple of extra items that it injects for us prior to calling the `__new__` 
method.
'''

# %%
'''
Of course, if we do not specify a `__prepare__` method in our metaclass, we inherit the one that is already defined in 
`type` - which returns an empty dictionary.
'''

# %%
type.__prepare__()

# %%
'''
Here's an example where using this method can simplify things somewhat.
'''

# %%
'''
Recall the example where we passed named arguments to the metaclass in order to create some additional class attributes:
'''

# %%
class MyMeta(type):
    def __new__(mcls, name, bases, class_dict, **kwargs):
        class_dict.update(kwargs)
        return super().__new__(mcls, name, bases, class_dict)
    
class MyClass(metaclass=MyMeta, arg1=100, arg2=200):
    pass        

# %%
vars(MyClass)

# %%
'''
We were able to override the `__new__` method and inject the additional arguments right into the class dictionary.
'''

# %%
'''
But we could just as easily inject those items in the class dictionary right in the `__prepare__` method.
'''

# %%
'''
What's important to understand is that whatever extra arguments we pass to the metaclass are also passed along to the `
__prepare__` method, just like they are eventually passed to `__new__`.
'''

# %%
class MyMeta(type):
    def __prepare__(name, bases, **kwargs):
        print(f'MyMeta.__prepare__ called... with {kwargs}')
        # we could create a new dictionary and insert everything we need from kwargs
        # or we could just use the kwargs dictionary directly
        kwargs['bonus_attr'] = 'Python rocks!'
        return kwargs
    
    def __new__(cls, name, bases, cls_dict, **kwargs):
        print('MyMeta.__new__ called...')
        print('\tcls: ', cls, type(cls))
        print('\tname:', name, type(name))
        print('\tbases: ', bases, type(bases))
        print('\tcls_dict:', cls_dict, type(cls_dict))
        print('\tkwargs:', kwargs)
        return super().__new__(cls, name, bases, cls_dict)

# %%
class MyClass(metaclass=MyMeta, kw1=1, kw2=2):
    pass

# %%
vars(MyClass)

# %%
'''
And as you can see, we have our class attributes, and we did not have to use `__new__`. So often, `__prepare__` is a 
much simpler alternative to overriding `__new__`.
'''

# %%
'''
The return value of `__prepare__` must be a mapping type:
'''

# %%
class MyMeta(type):
    def __prepare__(name, bases):
        return 'some string'

# %%
class MyClass(metaclass=MyMeta):
    pass

# %%
'''
This exception is raised because Python is trying to use the class dictionary as a mapping type.
'''

# %%
cls_dict = 'some string'
cls_dict['__module__']

# %%
'''
The return value must therefore be a mapping type, but it does not have to be a dict - it could be an OrderedDict
 for example, or even a custom dictionary.
'''

# %%
from collections import OrderedDict

# %%
class MyMeta(type):
    def __prepare__(name, bases):
        d = OrderedDict()
        d['bonus'] = 'Python rocks!'
        return d

# %%
class MyClass(metaclass=MyMeta):
    pass

# %%
vars(MyClass)

# %%
'''
Or it could even be a custom dictionary type:
'''

# %%
from collections import UserDict

# %%
class CustomDict(UserDict):
    def __setitem__(self, key, value):
        print(f'Setting {key} = {value} in custom dictionary')
        super().__setitem__(key, value)
        
    def __getitem__(self, key):
        print(f'Getting {key} from custom dictionary')
        return int(super().__getitem__(key))   

# %%
class MyMeta(type):
    def __prepare__(name, bases):
        return CustomDict()

# %%
class MyClass(metaclass=MyMeta):
    pass

# %%
'''
As you can see, we have a slight problem here. The `__new__` method actually expects a `dict`. Even though `CustomDict`
essentially behaves like a dictionary, it is not in fact a subclass of `dict`:
'''

# %%
issubclass(CustomDict, dict)

# %%
'''
But as long as our custom dictionary inherits from `dict` we should be fine:
'''

# %%
class CustomDict(dict):
    def __setitem__(self, key, value):
        print(f'Setting {key} = {value} in custom dictionary')
        super().__setitem__(key, value)
        
    def __getitem__(self, key):
        print(f'Getting {key} from custom dictionary')
        return int(super().__getitem__(key))   

# %%
class MyMeta(type):
    def __prepare__(name, bases):
        return CustomDict()
    
    def __new__(mcls, name, bases, cls_dict):
        print('metaclass __new__ called...')
        print(f'\ttype(cls_dict) = {type(cls_dict)}')
        print(f'\tcls_dict={cls_dict}')

# %%
class MyClass(metaclass=MyMeta):
    pass

# %%
'''
As you can see, the dictionary we returned from `__prepare__` was a `CustomDict` instance that is eventually passed 
to `__new__` when it is called. 
And between `__prepare__` and `__new__`, Python accessed our dictionary to read/write a few items.
'''