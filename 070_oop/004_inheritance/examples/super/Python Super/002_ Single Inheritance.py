# Python super function is a built-in function that returns the proxy object that allows you to refer parent class by
# super.  The super function in Python can be used to gain access to inherited methods, which is either from
# the parent or sibling class.

# Python super() builtin function returns a proxy object, a substitute object that can call the method of the base
# class via delegation. It is called indirection, which is the ability to reference base objects with super().
# The super function is versatile and can be used in a couple of ways.

# Python Super Function Example
# If Python's super() builtin doesn't wow you, chances are you don't know what super function is capable of doing or
# how to use it effectively.
#
# If we want to understand the python super function, we need to know about Inheritance in Python language.
# In Python Inheritance, the subclasses can inherit from the superclass.

# Python super function can refer to the superclass implicitly. So, the Python super () function makes
# our task more manageable.
#
# While referring to the superclass from the base class, we don't need to write the name of the superclass explicitly.

# #How to Call super in Python 3
# We can call using the following syntax. We will take a regular class definition and modify it by adding
# the super function. The final code with a super() keyword looks like below.

class MyParentClass():
    def __init__(self):
        pass

class SubClass(MyParentClass):
    def __init__(self):
        super()

# As you can see, this is the basic setup of single inheritance.
#
# We can see that there's the base or parent class (also sometimes called the superclass)
# and derived class or subclass, but we still need to initialize the parent or base class within the subclass
# or derived or child.
# We can call the super() function to process more accessible.
#
# The goal of Super function is to provide a much more abstract and portable solution for initializing classes.

# Let's see the example of the super() function in Python.
#
# app.py

class Computer():
    def __init__(self, computer, ram, ssd):
        self.computer = computer
        self.ram = ram
        self.ssd = ssd

class Laptop(Computer):
    def __init__(self, computer, ram, ssd, model):
        super().__init__(computer, ram, ssd)
        self.model = model

lenovo = Laptop('lenovo', 2, 512, 'l420')
print('This computer is:', lenovo.computer)
print('This computer has ram of', lenovo.ram)
print('This computer has ssd of', lenovo.ssd)
print('This computer has this model:', lenovo.model)


# In the above example, we have defined one base class which is a Computer, and one is derived class, which is Laptop.
# We have defined three properties inside the base class, and the derived class has a total of four properties.
#
# Three properties from the derived class are derived from the base class, and fourth is that's own property.
# In the derived or child class has its model property. The other three are obtained from a base class computer.

# So, now, if we only create an object of the derived class, we still have all the access to the base class's property
# because of super() function.
#
# The output of the above example is the following.

