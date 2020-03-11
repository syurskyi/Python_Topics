# Now that you've worked through an overview and some examples of super() and single inheritance,
# ou will be introduced to an overview and some examples that will demonstrate how multiple inheritance works
# and how super() enables that functionality.
#
# Multiple Inheritance Overview
# There is another use case in which super() really shines, and this one isn't as common as the single inheritance
# scenario. In addition to single inheritance, Python supports multiple inheritance, in which a subclass
# can inherit from multiple superclasses that don't necessarily inherit from each other (also known as sibling classes).
#
# I'm a very visual person, and I find diagrams are incredibly helpful to understand concepts like this.
# The image below shows a very simple multiple inheritance scenario, where one class inherits from two unrelated
# (sibling) superclasses:


# To better illustrate multiple inheritance in action, here is some code for you to try out, showing how you can
# build a right pyramid (a pyramid with a square base) out of a Triangle and a Square:

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

# Note: The term slant height may be unfamiliar, especially if it's been a while since you've taken a geometry class
# or worked on any pyramids.
# The slant height is the height from the center of the base of an object (like a pyramid) up its face to the peak

# of that object. You can read more about slant heights at WolframMathWorld.
#
# This example declares a Triangle class and a RightPyramid class that inherits from both Square and Triangle.
# You'll see another .area() method that uses super() just like in single inheritance, with the aim
# of it reaching the .perimeter() and .area() methods defined all the way up in the Rectangle class.
#
# Note: You may notice that the code above isn't using any inherited properties from the Triangle class yet.
# Later examples will fully take advantage of inheritance from both Triangle and Square.
#
# The problem, though, is that both superclasses (Triangle and Square) define a .area(). Take a second and think
# about what might happen when you call .area() on RightPyramid, and then try calling it like below:
#
pyramid = RightPyramid(2, 4)
pyramid.area()

# Traceback (most recent call last):
#   File "shapes.py", line 63, in <module>
#     print(pyramid.area())
#   File "shapes.py", line 47, in area
#     base_area = super().area()
#   File "shapes.py", line 38, in area
#     return 0.5 * self.base * self.height
# AttributeError: 'RightPyramid' object has no attribute 'height'
# Did you guess that Python will try to call Triangle.area()? This is because of something called the method resolution order.
#
# Note: How did we notice that Triangle.area() was called and not, as we hoped, Square.area()?
# If you look at the last line of the traceback (before the AttributeError), you'll see a reference to a specific line
# of code:
#
# return 0.5 * self.base * self.height
# You may recognize this from geometry class as the formula for the area of a triangle.
# Otherwise, if you're like me, you might have scrolled up to the Triangle and Rectangle class definitions and
# seen this same code in Triangle.area().
