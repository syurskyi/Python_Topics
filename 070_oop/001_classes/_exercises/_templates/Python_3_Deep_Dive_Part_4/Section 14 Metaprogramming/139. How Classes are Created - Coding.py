# %%
'''
### How are Classes Constructed?
'''

# %%
'''
When we write a class such as this:
'''

# %%
import math

class Circle(object):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        
    def area(self):
        return math.pi * self.r ** 2

# %%
'''
Remember that a class is an **instance** of the `type` class:
'''

# %%
type(Circle)

# %%
'''
And `type` is a class itself, so it is callable (with some arguments), and is used to create classes, instances of the 
`type` class.
'''

# %%
'''
There are four main steps involved with creating instances of a class:

1. The class body is extracted - think of it as just a lump of text that contains code.
2. The class dictionary (used for the **class** state) is created for the class namespace
3. The body (extracted in 1), is executed in the class namespace (created in 2), thereby populating the class dictionary 
(in this case with two symbols, `__init__` and `area`)
4. A new `type` **instance** is constructed using the name of the class, the base classes (remember Python supports 
multiple inheritance), and that dictionary.
'''

# %%
'''
Let's actually step through this process manually ourselves:
'''

# %%
'''
First we need to look at the `exec` built-in method:
'''

# %%
'''
Let's try it out with a simple example first:
'''

# %%
namespace = {}

exec('''
a = 10
b = 20
''', globals(), namespace)

# %%
'''
And now let's see what's in the `namespace` dictionary:
'''

# %%
namespace

# %%
'''
As you can see, that dictionary was used as the local namespace when the code (in the string) was executed. Of course, 
the code can contain any valid Python code, including function definitions:
'''

# %%
exec('''
def add(a, b):
    return a + b
    
def mul(a, b):
    return a * b
''', globals(), namespace)

# %%
namespace

# %%
'''
And we can use those functions, since now they are actual function objects in the namespace (dictionary):
'''

# %%
namespace['add'](10, 20)

# %%
'''
Remember what I told you about the class body scope? Well, this is it! And you should now understand why functions 
defined in that scope do not actually know anything about what else is in that scope - those functions are created 
independently of the dictionary into which they are inserted.
'''

# %%
'''
So, this is how we are going to "run" the class **body** in the context of the class namespace dictionary.
'''

# %%
'''
We'll also need to create a new `type` instance, so let's see what the signature for the `type` constructor is:
'''

# %%
help(type)

# %%
'''
The constructor variant we are interested in is the third one. That one requires three things:
1. the `name` of the class
2. an tuple containing the `bases` - the classes this class inherits from (can be empty, in which case it just inherits 
from `object`)
3. the class namespace `dict`
'''

# %%
'''
Remember when I said that classes were basically just dictionaries? As you can see here, apart from the `name` and 
`bases`, all the functionality of the class is stored in the namespace dictionary!!
'''

# %%
'''
So now, let's go ahead and create our `Circle` class using this approach:
'''

# %%
class_name = 'Circle'

# %%
class_body = """
def __init__(self, x, y, r):
    self.x = x
    self.y = y
    self.r = r

def area(self):
    return math.pi * self.r ** 2
"""

# %%
class_bases = ()  # defaults to object

# %%
class_dict = {}

# %%
exec(class_body, globals(), class_dict)

# %%
'''
Now that we have executed that code in that namespace, that dictionary has some content:
'''

# %%
class_dict

# %%
'''
And we can now create the `Circle` class, or type, by creating a new instance of `type`:
'''

# %%
Circle = type(class_name, class_bases, class_dict)

# %%
Circle

# %%
type(Circle)

# %%
Circle.__dict__

# %%
'''
As you can see the `Circle` namespace dict contains our functions `__init__` and `area`.
'''

# %%
'''
And we now have a `Circle` class that we can use just like before:
'''

# %%
c = Circle(0, 0, 1)

# %%
c.x, c.y, c.r

# %%
c.area()

# %%
'''
So as you can see, we use the `type` class to construct new types (classes), basically creating instances of `type`.
This is why we refer to `type` as a **metaclass**. It is a class used to construct classes.
'''

# %%
'''
Also, make sure you understand that `type` is callable in two different ways - depending on what arguments are passed 
to `type()` it will do different things:
'''

# %%
'''
Creates a new `type` instance:
'''

# %%
Circle = type(class_name, class_bases, class_dict)

# %%
'''
Returns the `type` of an object:
'''

# %%
type(Circle)