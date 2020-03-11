# super() function in Python:
# Python super function provides us the facility to refer to the parent class explicitly.
# It is basically useful where we have to call superclass functions. It returns the proxy object that allows us
# to refer parent class by super.
#
# To understand Python super function we must know about the inheritance. In Python inheritance, the subclasses
# are inherited from the superclass.
#
# Python Super function provides us the flexibility to do single level or multilevel inheritances and makes our
# work easier and comfortable. Keep one thing in mind that while referring the superclass from subclass,
# there is no need of writing the name of superclass explicitly.


# Here is one example of how to call the super function in Python3:

# # parent class also sometime called the super class

class Parentclass():
    def __init__(self):
        pass

# derived or subclass
# initialize the parent or base class within the subclass
class subclass(Parentclass):
    def __init__(self):
        # calling super() function to make process easier
        super()

# Python super() function with multilevel inheritance.
#
# As we have studied that the Python super() function allows us to refer the superclass implicitly.
# But in multi-level inheritances, the question arises that there are so many classes so which class did
# the super() function will refer?
# Well, the super() function has a property that it always refers the immediate superclass.
# Also, super() function is not only referring the __init__() but it can also call the other functions
# of the superclass when it needs.
#
# Here is the example of explaining the multiple inheritances.

# # Program to define the use of super()
# # function in multiple inheritance

class GFG1:
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG1)')

    def sub_GFG(self, b):
        print('Printing from class GFG1:', b)

# class GFG2 inherits the GFG1

class GFG2(GFG1):
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG2)')
        super().__init__()

    def sub_GFG(self, b):
        print('Printing from class GFG2:', b)
        super().sub_GFG(b + 1)

# class GFG3 inherits the GFG1 ang GFG2 both

class GFG3(GFG2):
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG3)')
        super().__init__()

    def sub_GFG(self, b):
        print('Printing from class GFG3:', b)
        super().sub_GFG(b + 1)


# main function
if __name__ == '__main__':

    # created the object gfg
    gfg = GFG3()

    # calling the function sub_GFG3() from class GHG3
    # which inherits both GFG1 and GFG2 classes
    gfg.sub_GFG(10)


# Output:
# HEY !!!!!! GfG I am initialised(Class GEG3)
# HEY !!!!!! GfG I am initialised(Class GEG2)
# HEY !!!!!! GfG I am initialised(Class GEG1)
# Printing from class GFG3: 10
# Printing from class GFG@: 11
# Printing from class GFG1: 12
