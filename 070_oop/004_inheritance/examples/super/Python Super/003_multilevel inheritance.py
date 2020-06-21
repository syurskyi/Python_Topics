# We have stated previously that Python's super() function allows us to refer to the superclass implicitly.
#
# But in the scenario of multi-level inheritances, which class will it refer to? Well, the super() function will
# always refer to an immediate superclass.
#
# Also, a Python super() function not only can refer to the __init()__ function but also can call all other function
# of a superclass.
#
# See the following example.

# app.py

class A:
    def __init__(self):
        print('Initializing: class A')

    def sub_method(self, b):
        print('Printing from class A:', b)


class B(A):
    def __init__(self):
        print('Initializing: class B')
        super().__init__()

    def sub_method(self, b):
        print('Printing from class B:', b)
        super().sub_method(b + 1)


class C(B):
    def __init__(self):
        print('Initializing: class C')
        super().__init__()

    def sub_method(self, b):
        print('Printing from class C:', b)
        super().sub_method(b + 1)


if __name__ == '__main__':
    c = C()
    c.sub_method(1)

# See the output below.
#
# Super() Method Tutorial Example
# So, from the output, we can see that the __init()__ function of class C had been called at first,
# then class B and after that class A.
# The same thing happened by calling the sub_method() function.
# If your program contains the multi-level inheritance, then the super() function is beneficial for you as well.

