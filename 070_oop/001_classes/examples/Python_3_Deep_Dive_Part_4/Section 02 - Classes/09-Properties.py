# %%
'''
### Properties
'''

# %%
'''
To be clear, here we are examining **instance** properties. That is, we define the property in the class 
we are defining, but the property itself is going to be **instance** specific, i.e. different instances will support 
different values for the property. Just like instance attributes. The main difference is that we will use accessor 
method to get, set (and optionally) delete the associated instance value.
'''

# %%
'''
As I mentioned in the lecture, because properties use the same dotted notation (and the same `getattr`, `setattr` 
and `delattr` functions), we do not need to **start** with properties. Often a bare attribute works just fine, and if,
later, we decide we need to manage getting/setting/deleting the attribute value, we can switch over to properties 
without breaking our class interface. This is unlike languages like Java - and hence why in those languages it is 
recommended to **always** use getter and setter functions. *Not so* in Python!
'''

# %%
'''
A **property** in Python is essentially a class instance - we'll come back to what that class looks like when we study 
descriptors. For now, we are going to use the `property` function in Python which is a convenience callable essentially.
'''

# %%
'''
Let's start with a simple example and a bare attribute:
'''

# %%
class Person:
    def __init__(self, name):
        self.name = name

# %%
'''
So this class has a single instance **attribute**, `name`.
'''

# %%
p = Person('Alex')

# %%
'''
And we can access and modify that attribute using either dotted notation or the `getattr` and `setattr` methods:
'''

# %%
print(p.name)

# %%
getattr(p, 'name')

# %%
'''
p.name = 'John'
'''

# %%
print(p.name)

# %%
setattr(p, 'name', 'Eric')

# %%
print(p.name)

# %%
'''
Now suppose we wan't to disallow setting an empty string or `None` for the name. Also, we'll require the name to be 
a string.
To do that we are going to create an instance method that will handle the logic and setting of the value. 
We also create an instance method to retrieve the attribute value.
We'll use `_name` as the instance variable to store the name.
'''

# %%
class Person:
    def __init__(self, name):
        self.set_name(name)
        
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            # this is valid
            self._name = value.strip()
        else:
            raise ValueError('name must be a non-empty string')

# %%
p = Person('Alex')

# %%
try:
    p.set_name(100)
except ValueError as ex:
    print(ex)

# %%
p.set_name('Eric')

# %%
p.get_name()

# %%
'''
Of course, our users can still manipulate the atribute directly if they want by using the "private" attribute `_name`. 
You can't stop anyone from doing this in Python - they should know better than to do that, but we're 
all good programmers, and know what and what not to do!
'''

# %%
'''
The way we set up our initializer, the validation will work too:
'''

# %%
try:
    p = Person('')
except ValueError as ex:
    print(ex)

# %%
'''
So this works, but it's a bit of pain to use the method names. So let's turn this into a property instead. 
We start with the class we just had and tweak it a bit:
'''

# %%
class Person:
    def __init__(self, name):
        self.name = name  # note how we are actually setting the value for name using the property!
        
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            # this is valid
            self._name = value.strip()
        else:
            raise ValueError('name must be a non-empty string')
            
    name = property(fget=get_name, fset=set_name)

# %%
p = Person('Alex')

# %%
print(p.name)

# %%
p.name = 'Eric'

# %%
try:
    p.name = None
except ValueError as ex:
    print(ex)

# %%
'''
So now we have the benefit of using accessor methods, without having to call the methods explicitly.
In fact, even `getattr` and `setattr` will work the same way:
'''

# %%
setattr(p, 'name', 'John')  # or p.name = 'John'

# %%
getattr(p, 'name')  # or simply p.name

# %%
'''
Now let's examine the instance dictionary:
'''

# %%
print(p.__dict__)

# %%
'''
You'll see we can find the underlying "private" attribute we are using to store the name. But the property itself 
(`name`) is not in the dictionary.
The property was defined in the class:
'''

# %%
print(Person.__dict__)

# %%
'''
And you can see it's type is `property`.
So when we type `p.name` or `p.name = value`, Python recognizes that `'name` is a `property` and therefore uses 
the accessor methods. (How it does we'll see later when we study descriptors).
What's interesting is that even if we muck around with the instance dictionary, Python does not get confused - 
(and as usual in Python, just because you **can** do something does not mean you **should**!)
'''

# %%
p = Person('Alex')

# %%
print(p.name)

# %%
print(p.__dict__)

# %%
p.__dict__['name'] = 'John'

# %%
print(p.__dict__)

# %%
'''
As you can see, we now have `name` in our instance dictionary.
Let's retrieve the `name` via dotted notation:
'''

# %%
print(p.name)

# %%
'''
That's obviously still using the getter method.
And setting the name:
'''

# %%
p.name = 'Raymond'

# %%
print(p.__dict__)

# %%
'''
As you can see, it used the setter method.
And the same thing happens with `setattr` and `getattr`:
'''

# %%
getattr(p, 'name')

# %%
setattr(p, 'name', 'Python')

# %%
print(p.__dict__)

# %%
'''
As you can see the `setattr` method used the property setter.
'''

# %%
'''
For completeness, let's see how the deleter method works:
'''

# %%
class Person:
    def __init__(self, name):
        self._name = name
        
    def get_name(self):
        print('getting name')
        return self._name
    
    def set_name(self, value):
        print('setting name')
        self._name = value
        
    def del_name(self):
        print('deleting name')
        del self._name  # or whatever "cleanup" we want to do
        
    name = property(get_name, set_name, del_name)

# %%
p = Person('Alex')

# %%
print(p.__dict__)

# %%
print(p.name)

# %%
p.name = 'Eric'

# %%
print(p.__dict__)

# %%
del p.name

# %%
print(p.__dict__)

# %%
'''
Now, the property still exists (since it is defined in the class) - all we did was remove the underlying value 
for the property (the `_name` instance attribute):
'''

# %%
try:
    p.name
except AttributeError as ex:
    print(ex)

# %%
'''
As you can see the issue is that the getter function is trying to find `_name` in the attribute, which no longer exists.
So the getter and setter still exist (i.e. the property still exists), so we can still assign to it:
'''

# %%
p.name = 'Alex'

# %%
print(p.name)

# %%
'''
The last param in `property` is just a docstring. So we could do this:
'''

# %%
class Person:
    """This is a Person object"""
    def __init__(self, name):
        self._name = name
        
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        self._name = value
        
    name = property(get_name, set_name, doc="The person's name.")

# %%
p = Person('Alex')

# %%
help(Person.name)

# %%
help(Person)