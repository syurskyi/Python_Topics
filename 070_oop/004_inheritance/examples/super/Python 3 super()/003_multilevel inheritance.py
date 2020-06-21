# As we have stated previously that Python super() function allows us to refer the superclass implicitly.
# But in the case of multi-level inheritances which class will it refer? Well, Python super() will always refer
# the immediate superclass.  Also Python super() function not only can refer the __init__() function but also
# can call all other function of the superclass. So, in the following example, we will see that.
#
#
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

# Let's see the output of above python 3 super example with multi-level inheritance.
#
#
# Initializing: class C
# Initializing: class B
# Initializing: class A
# Printing from class C: 1
# Printing from class B: 2
# Printing from class A: 3

# So, from the output we can clearly see that the __init__() function of class C had been called at first,
# then class B and after that class A. Similar thing happened by calling sub_method() function.
# Why do we need Python super function
# If you have previous experience in Java language, then you should know that the base class is also called by
# a super object there. So, this concept is actually useful for the coders. However, Python also keeps the facility
# for the programmer to use superclass name to refer them. And, if your program contains multi-level inheritance,
# then this super() function is helpful for you.
#
# So, that's all about python super function. Hopefully, you understood this topic. Please use the comment box for
# any query.
