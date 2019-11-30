# %%
'''
### Classes are Callable
'''

# %%
'''
As we saw earlier, one of the things Python does for us when we create a class is to make it callable.
Calling a class creates a new instance of the class - an object of that particular type.
'''

# %%
class Program:
    language = 'Python'
    
    def say_hello():
        print(f'Hello from {Program.language}!')

# %%
p = Program()

# %%
print(type(p))

# %%
print(isinstance(p, Program))

# %%
'''
These instances have their own namespace, and their own `__dict__` that is distinct from the class `__dict__`:
'''

# %%
print(p.__dict__)

# %%
print(Program.__dict__)

# %%
'''
Instances also have attributes that may not be visible in their `__dict__` (they are being stored elsewhere,
 as we'll examine later):
'''

# %%
print(p.__class__)

# %%
'''
Although we can use `__class__` we can also use `type`:
'''

# %%
print(type(p) is p.__class__)

# %%
'''
Generally we use `type` instead of using `__class__` just like we usually use `len()` instead of accessing `__len__`.
'''

# %%
'''
Why? Well, one reason is that people can mess around with the `__class__` attribute:
'''

# %%
class MyClass:
    pass

# %%
m = MyClass()

# %%
print(type(m), m.__class__)

# %%
'''
But look at what happens here:
'''

# %%
class MyClass:
    __class__ = str

# %%
m = MyClass()

# %%
print(type(m), m.__class__)

# %%
'''
So as you can see, `type` wasn't fooled!
'''

# %%
