# Concrete Methods in Abstract Base Classes :
# Concrete classes contain only concrete (normal)methods whereas abstract class contains both concrete methods
# as well as abstract methods. Concrete class provide an implementation of abstract methods, the abstract base class
# can also provide an implementation by invoking the methods via super().
# Let look over the example to invoke the method using super():

# Python program invoking a
# method using super()

import abc
from abc import ABC, abstractmethod


class R(ABC):
    def rk(self):
        print("Abstract Base Class")


class K(R):
    def rk(self):
        super().rk()
        print("subclass ")

    # Driver code


r = K()
r.rk()

# Output:
#
# Abstract Base Class
# subclass
# In the above program, we can invoke the methods in abstract classes by using super().
