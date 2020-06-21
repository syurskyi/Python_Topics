# %%
'''
### Deleting Properties
'''

# %%
'''
Just like we can delete an attribute from an instance object, we can also delete a property from an instance object.
Note that this action simply runs the deleter method, but the propertu remains defined **on the class**. 
It does not remove the property from the class, instead it is generally used to remove the property value from the 
**instance**.
'''

# %%
'''
Properties, like attributes, can be deleted by using the `del` keyword, or the `delattr` function.
'''

# %%
class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print('getting name property value...')
        return self._name
    
    def set_name(self, value):
        print(f'setting name property to {value}...')
        self._name = value
    
    def del_name(self):
        # delete the underlying data
        print('deleting name property value...')
        del self._name
        
    name = property(fget=get_name, fset=set_name, fdel=del_name, doc='Person name.')


# %%
p = Person('Guido')

# %%
print(p.name)

# %%
'''
And the underlying `_name` property is in our instance dictionary:
'''

# %%
print(p.__dict__)

# %%
del p.name

# %%
'''
As we can see, the underlying `_name` attribute is no longer present in the instance dictionary:
'''

# %%
print(p.__dict__)

# %%
try:
    print(p.name)
except AttributeError as ex:
    print(ex)

# %%
'''
As you can see, the property deletion did not remove the property definition, that still exists.
'''

# %%
'''
Alternatively, we can use the `delattr` function as well:
'''

# %%
p = Person('Raymond')

# %%
delattr(p, 'name')

# %%
'''
And we can of course use the decorator syntax as well:
'''

# %%
class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        print('getting name property value...')
        return self._name
    
    @name.setter
    def name(self, value):
        """Person name"""
        print(f'setting name property to {value}...')
        self._name = value
    
    @name.deleter
    def name(self):
        # delete the underlying data
        print('deleting name property value...')
        del self._name

# %%
p = Person('Alex')

# %%
print(p.name)

# %%
del p.name

# %%
