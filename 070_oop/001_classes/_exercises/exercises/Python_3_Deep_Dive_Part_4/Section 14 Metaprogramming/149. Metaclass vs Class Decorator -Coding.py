# %%
'''
### Metaclasses vs Class Decorators
'''

# %%
'''
As we have seen, class decorators can achieve a lot of the metaprogramming goals we might have.
'''

# %%
'''
But there is one area where they fall short of metaclasses - inheritance.
'''

# %%
'''
Metaclasses are carried through inheritance, whereas decorators are not.
'''

# %%
'''
Let's go back to the previous class decorator example we had (and I'll use the original one to keep the code simple):
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

def class_logger(cls):
    for name, obj in vars(cls).items():
        if callable(obj):
            print('decorating:', cls, name)
            setattr(cls, name, func_logger(obj))
    return cls

# %%
'''
And as we saw, we can decorate a class with it:
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
Person('Alex', 10).greet()

# %%
'''
We could do this with a metaclass too:
'''

# %%
class ClassLogger(type):
    def __new__(mcls, name, bases, class_dict):
        new_cls = super().__new__(mcls, name, bases, class_dict)
        for key, obj in vars(new_cls).items():
            if callable(obj):
                setattr(new_cls, key, func_logger(obj))
        return new_cls        

# %%
class Person(metaclass=ClassLogger):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f'Hello, my name is {self.name} and I am {self.age}'

# %%
p = Person('John', 78).greet()

# %%
'''
So, why not just use a class decorator?
'''

# %%
'''
Now let's see how inheritance works with both those methods.
'''

# %%
'''
Let's do the decorator approach first:
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
'''
Now let's inherit `Person`:
'''

# %%
class Student(Person):
    def __init__(self, name, age, student_number):
        super().__init__(name, age)
        self.student_number = student_number
        
    def study(self):
        return f'{self.name} studies...'

# %%
s = Student('Alex', 19, 'abcdefg')

# %%
'''
So first off, you can see that the print worked, but only for the `__init__` in the `Person` class, no logs were 
generated for the `__init__` in the `Student` class.
'''

# %%
'''
By the same token, we don't get logging on the `study` method:
'''

# %%
s.study()

# %%
'''
So we would need to remember to decorate the `Student` class as well:
'''

# %%
@class_logger
class Student(Person):
    def __init__(self, name, age, student_number):
        super().__init__(name, age)
        self.student_number = student_number
        
    def study(self):
        return f'{self.name} studies...'

# %%
s = Student('Alex', 19, 'abcdefg')

# %%
s.greet()

# %%
s.study()

# %%
'''
So, we just have to remember to decorate **every** subclass as well.
'''

# %%
'''
But if we use a metaclass, watch what happens when inherit:
'''

# %%
class Person(metaclass=ClassLogger):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f'Hello, my name is {self.name} and I am {self.age}'
    
class Student(Person):
    def __init__(self, name, age, student_number):
        super().__init__(name, age)
        self.student_number = student_number
        
    def study(self):
        return f'{self.name} studies...'

# %%
s = Student('Alex', 19, 'abcdefg')

# %%
s.study()

# %%
'''
This works because `Student` inherits from `Person`, and since `Person` uses a metaclass for the creation, this follows
 down to the `Student` class as well.
'''

# %%
type(Person)

# %%
type(Student)

# %%
'''
As you can see the type of both the parent and the subclass is `ClassLogger` even though we did not explicitly state 
that `Student` shouls use the metaclass for creation.
It happened automatically because we did not have a `__new__` method in the `Student` class, so the parent's `__new__` 
was essentially used, and that one uses the metaclass.
'''

# %%
'''
We can see this more explicitly this way:
'''

# %%
class Student(Person):
    def __new__(cls, name, age, student_number):
        return super().__new__(cls)
    
    def __init__(self, name, age, student_number):
        super().__init__(name, age)
        self.student_number = student_number
        
    def study(self):
        return f'{self.name} studies...'

# %%
s = Student('Alex', 19, 'ABC')

# %%
s.study()

# %%
'''
One of the disadvantages of metaclasses vs class decorators is that only a "single" metaclass can be used. (Actually 
it's a bit more subtle than that, we can use a different metaclass in for a subclass if the metclass is a subclass of 
the parent's metaclass - we'll cover this point again when we look at multiple inheritance.)
'''

# %%
class Metaclass1(type):
    pass

class Metaclass2(type):
    pass

# %%
class Person(metaclass=Metaclass1):
    pass

# %%
class Student(Person, metaclass=Metaclass2):
    pass

# %%
'''
As you can see we cannot specify a custom metaclass for `Student` because that would conflict with the class it is 
inheriting from.
'''

# %%
'''
An exception is if we inherit from a parent who has `type` as its metaclass:
'''

# %%
class Person:
    pass

class Student(Person, metaclass=Metaclass1):
    pass

# %%
p = Person()
s = Student()

# %%
type(Person), type(Student)

# %%
'''
It can also cause problems in multiple inheritance.
We haven't covered multiple inheritance yet, but let me show you the issue at least:
'''

# %%
class Class1(metaclass=Metaclass1):
    pass

class Class2(metaclass=Metaclass2):
    pass

# %%
'''
Here we have created two classes that use different custom metaclasses.
If we try to create a new class that inherits from both:
'''

# %%
class MultiClass(Class1, Class2):
    pass

# %%
'''
Again, if one of the base classes is `type` and the other is a custom metaclass, then this is allowed (this is because
`Metaclass1` is itself a subclass of `type`:
'''

# %%
class Class1(metaclass=type):
    pass

class Class2(metaclass=Metaclass1):
    pass

# %%
class MultiClass(Class1, Class2):
    pass

# %%
'''
On the other hand we can stack decorators as much as we want (we just have to be careful with the order in which we 
stack them sometimes).
'''