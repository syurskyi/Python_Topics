# %%
'''
### Single Inheritance
'''

# %%
'''
For now we're just going to define classes that inherit from another class, but we aren't going to bother implementing 
any functionality or state for these classes.
We just want to explore the relationships between objects created from classes that inherit from each other.
'''

# %%
class Shape:
    pass

class Ellipse(Shape):
    pass

class Circle(Ellipse):
    pass

class Polygon(Shape):
    pass

class Rectangle(Polygon):
    pass

class Square(Rectangle):
    pass

class Triangle(Polygon):
    pass

# %%
'''
As you can see we created a single inheritance chain that looks something like this:

```
                         Shape
     Ellipse                            Polygon
     
      Circle                   Rectangle          Triangle
                               Square
```
'''

# %%
'''
It is important to understand that these **classes** are subclasses of each other - just remember that **subclass** 
contains the word **class** - so it defines a relationship between classes, not instances:
'''

# %%
issubclass(Ellipse, Shape)

# %%
'''
But if we create instances of those two classes:
'''

# %%
s = Shape()
e = Ellipse()
try:
    issubclass(e, s)
except TypeError as ex:
    print(ex)

# %%
'''
When we deal with instances of classes, we can instead use the `isinstance()` function:
'''

# %%
isinstance(e, Ellipse)

# %%
'''
But, not only is `e` an instance of an `Ellipse`, since `Ellipse` IS-A `Shape`, i.e. `Ellipse` is a **subclass** of 
`Shape`, it tunrs out thet `e` is also considered an instance of `Shape`:
'''

# %%
isinstance(e, Shape)

# %%
'''
Subclasses behave similarly in that a class may be a subclass of another class without being a **direct** subclass.
In our example here, every class we defined is a subclass of `Shape` because the inheritance chains all go back up to the `Shape` class:
'''

# %%
issubclass(Square, Shape)

# %%
'''
And of course, the same works for instances when we look at `isinstance`:
'''

# %%
sq = Square()

# %%
isinstance(sq, Square)

# %%
isinstance(sq, Rectangle)

# %%
isinstance(sq, Polygon)

# %%
isinstance(sq, Shape)

# %%
'''
But of course, a `Square` is not a subclass of `Ellipse` and `Square` instances are not instances of `Ellipse`:
'''

# %%
issubclass(Square, Ellipse)

# %%
isinstance(sq, Ellipse)

# %%
'''
We'll come back to this later, but when we define a class in Python 3 that does not explicitly inherit from another class:
'''

# %%
class Person:
    pass

# %%
'''
it is actually implicitly inheriting from a class!
'''

# %%
'''
There is a class in Python called `object` - yes, it is a **class**, even though the name says `object` 
(but classes are objects - everything in Python is an object):
'''

# %%
issubclass(Person, object)

# %%
p = Person()

# %%
isinstance(p, Person)

# %%
'''
This means that our `Shape` class we created actually inherits from `object`, and therefore every other class we created 
also inherits from `object`:
'''

# %%
issubclass(Square, object)

# %%
isinstance(sq, object)

# %%
'''
We'll look at the `object` class in the next lecture.
'''