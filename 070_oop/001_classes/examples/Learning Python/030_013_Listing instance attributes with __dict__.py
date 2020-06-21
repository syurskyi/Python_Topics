from lister import ListInstance
class Spam(ListInstance):                    # Inherit a __str__ method
    def __init__(self):
        self.data1 = 'food'

x = Spam()
print(x)                                     # print() and str() run __str__
# <Instance of Spam, address 40240880:
#         name data1=food


str(x)
# '<Instance of Spam, address 40240880:\n\tname data1=food\n>'
x                                            # The __repr__ still is a default
# <__main__.Spam object at 0x026606F0>



### File: testmixin.py

from lister import *                  # Get lister tool classes

class Super:
    def __init__(self):               # Superclass __init__
        self.data1 = 'spam'           # Create instance attrs
    def ham(self):
        pass

class Sub(Super, ListInstance):       # Mix in ham and a __str__
    def __init__(self):               # listers have access to self
        Super.__init__(self)
        self.data2 = 'eggs'           # More instance attrs
        self.data3 = 42
    def spam(self):                   # Define another method here
        pass

if __name__ == '__main__':
    X = Sub()
    print(X)                          # Run mixed-in __str__


import lister
class C(lister.ListInstance): pass

x = C()
x.a = 1; x.b = 2; x.c = 3
print(x)
# <Instance of C, address 40961776:
#         name a=1
#         name b=2
#         name c=3



