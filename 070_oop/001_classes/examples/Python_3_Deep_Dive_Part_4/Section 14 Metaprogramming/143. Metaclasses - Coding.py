# %%
'''
### Metaclasses
'''

# %%
'''
In the last lecture, we saw how we could create new types (new classes), using `type` or custom types 
(classes that inherit from `type`).
'''

# %%
'''
But the actual creation process in either case is difficult.
We have to get the code text somehow, execute it in the context of a dictionary, and then call `type(name, bases, dict)
` or `CustomType(name, bases, dict)`.
Not the best user experience!
'''

# %%
'''
When we define classes in Python:
'''

# %%
class Person:
    def __init__(self, name):
        self.name = name
        
class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self._major = major
        
    @property
    def major(self):
        return self._major

# %%
'''
This code is executed by Python and we end up with a new type (like `Person`, or `Student`) that has been created.
This means Python has done all the steps we were doing manually for us, and called `type` with the name, bases and class 
dictionary. Makes it a lot easier for us...
'''

# %%
'''
But why did Python call `type` to create our `Student` class?
'''

# %%
'''
This is where the concept of a `metaclass` comes in.
'''

# %%
'''
When Python encounters `class Student(Person):`, it decides what class to use to create the class.
'''

# %%
'''
This class is called the metaclass, and by default it is the `type` class.
'''

# %%
'''
But, there is a way we can actually tell Python to use something other than `type` to do this - we can specify 
a different **metaclass** in the class definition itself, by passing it as a named argument:
'''

# %%
'''
So technically, this is what happens by default:
'''

# %%
import math

class Circle(metaclass=type):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        
    def area(self):
        return math.pi * self.r ** 2

# %%
type(Circle), Circle.__name__

# %%
c = Circle(0, 0, 1)
c.area()

# %%
'''
As you can see this worked as normal, and the default `metaclass` is `type`.
'''

# %%
'''
The `metaclass` argument essentially allows us to specify what class we want to use to construct our class. So we could
 create a custom class that will build a new type, injecting whatever functionality we want into the creation process - 
 essentially allowing us to modify the definition/functionality of the class we are creating using code.
Python will call our metaclass with the same arguments it would pass to the `type` constructor: `name`, `bases` and 
`class_dict`, so we need to handle those arguments, but it does the work of creating the class dictionary and executing 
the code in that context, gathering the bases and the name of the class we are defining.
'''

# %%
class CustomType(type):
    def __new__(mcls, name, bases, class_dict):
        print(f'Using custom metaclass {mcls} to create class {name}...')
        cls_obj = super().__new__(mcls, name, bases, class_dict)
        cls_obj.circ = lambda self: 2 * math.pi * self.r
        return cls_obj

# %%
class Circle(metaclass=CustomType):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        
    def area(self):
        return math.pi * self.r ** 2

# %%
'''
As you can see from the print output, our custom metaclass was used, and here's the class info:
'''

# %%
print(Circle)

# %%
'''
And just like before, it has the `__init__`, `area` and `circ` functions:
'''

# %%
vars(Circle)

# %%
'''
And we can use it just like before:
'''

# %%
c = Circle(0, 0, 1)
print(c.area())
print(c.circ())

# %%
'''
And that's how we use metaclasses declaratively. Python handles the complexity of creating the instance of 
the metaclass, getting the name, bases and class dictionary we otherwise have to create ourselves and pass as arguments 
when we call the metaclass.
'''

# %%
'''
Much of the difficulty with metaclasses, is how to use them, and, especially, not overdoing it.
'''

# %%
'''
Just because you know how to create metaclasses, does not mean every problem you encounter should be solved with one!
Don't be the person who invents problems because they have a solution!
'''