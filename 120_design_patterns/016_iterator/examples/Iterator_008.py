#=======================================================================================================================

class Customer:
    """client"""

    def __init__(self, name):
        self.__name = name
        self.__num = 0
        self.__clinics = None

    def getName(self):
        return self.__name

    def register(self, system):
        system.pushCustomer(self)

    def setNum(self, num):
        self.__num = num

    def getNum(self):
        return self.__num

    def setClinic(self, clinic):
        self.__clinics = clinic

    def getClinic(self):
        return self.__clinics


class NumeralIterator:
    """Iterator"""

    def __init__(self, data):
        self.__data = data
        self.__curIdx = -1

    def next(self):
        """Move to next element"""
        if (self.__curIdx < len(self.__data) - 1):
            self.__curIdx += 1
            return True
        else:
            return False

    def current(self):
        """Get the current element"""
        return self.__data[self.__curIdx] if (self.__curIdx < len(self.__data) and self.__curIdx >= 0) else None


class NumeralSystem:
    """Ranking system"""

    __clinics = ("Screening Room No. 1", "Screening Room 2", "Screening Room 3")

    def __init__(self, name):
        self.__customers = []
        self.__curNum = 0
        self.__name = name

    def pushCustomer(self, customer):
        customer.setNum(self.__curNum + 1)
        click = NumeralSystem.__clinics[self.__curNum % len(NumeralSystem.__clinics)]
        customer.setClinic(click)
        self.__curNum += 1
        self.__customers.append(customer)
        print("%s Hello! You are already %s Registered successfully, serial number:%04d, please wait patiently!"
              % (customer.getName(), self.__name, customer.getNum()) )

    def getIterator(self):
        return NumeralIterator(self.__customers)


    def visit(self):
        for customer in self.__customers:
            print("Next patient %04d(%s) Please go %s See a doctor."
                  % (customer.getNum(), customer.getName(), customer.getClinic()) )


# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================
class BaseIterator:
    """Iterator"""

    def __init__(self, data):
        self.__data = data
        self.toBegin()

    def toBegin(self):
        """Move the pointer to the starting position"""
        self.__curIdx = -1

    def toEnd(self):
        """Move the pointer to the end"""
        self.__curIdx = len(self.__data)

    def next(self):
        """Move to next element"""
        if (self.__curIdx < len(self.__data) - 1):
            self.__curIdx += 1
            return True
        else:
            return False

    def previous(self):
        "Move to previous element"
        if (self.__curIdx > 0):
            self.__curIdx -= 1
            return True
        else:
            return False

    def current(self):
        """Get the current element"""
        return self.__data[self.__curIdx] if (self.__curIdx < len(self.__data) and self.__curIdx >= 0) else None


# 基于框架的实现
#==============================


# Test
#=======================================================================================================================

def testHospital():
    numeralSystem = NumeralSystem("Registration desk")
    lily = Customer("Lily")
    lily.register(numeralSystem);
    pony = Customer("Pony")
    pony.register(numeralSystem)
    nick = Customer("Nick")
    nick.register(numeralSystem)
    tony = Customer("Tony")
    tony.register(numeralSystem)
    print()

    iterator = numeralSystem.getIterator()
    while(iterator.next()):
        customer = iterator.current()
        print("Next patient %04d(%s) Please go %s See a doctor."
              % (customer.getNum(), customer.getName(), customer.getClinic()) )

    # numeralSystem.visit()



def testBaseIterator():
    print("Traverse: ")
    iterator = BaseIterator(range(0, 10))
    while(iterator.next()):
        customer = iterator.current()
        print(customer, end="\t")
    print()

    print("Traverse from back to front: ")
    iterator.toEnd()
    while (iterator.previous()):
        customer = iterator.current()
        print(customer, end="\t")


def testLoop():
    arr = [0, 1, 2, 3, 4, 5, 6, 7 ,8 , 9];
    for e in arr:
        print(e, end="\t")


#  Method 1: Use () to define the generator
gen = (x * x for x in range(10))

#  Method 2: Define the generator function using yield
def fibonacci(maxNum):
    """Fibonacci generator"""
    a = b = 1
    for i in range(maxNum):
        yield a
        a, b = b, a + b

def testIterable():
    print("Method one, the square of 0-9：")
    for e in gen:
        print(e, end="\t")
    print()

    print("Method two, Fibonacci sequence: ")
    fib = fibonacci(10)
    for n in fib:
        print(n, end="\t")
    print()

    print("The for loop of the built-in container:")
    arr = [x * x for x in range(10)]
    for e in arr:
        print(e, end="\t")
    print()

    print()
    print(type(gen))
    print(type(fib))
    print(type(arr))


from collections import Iterable, Iterator
# Introducing Iterable and Iterator

def testIsIterator():
    print("Whether it is an Iterable object:")
    print(isinstance([], Iterable))
    print(isinstance({}, Iterable))
    print(isinstance((1, 2, 3), Iterable))
    print(isinstance(set([1, 2, 3]), Iterable))
    print(isinstance("string", Iterable))
    print(isinstance(gen, Iterable))
    print(isinstance(fibonacci(10), Iterable))
    print("Whether it is an Iterator object: ")
    print(isinstance([], Iterator))
    print(isinstance({}, Iterator))
    print(isinstance((1, 2, 3), Iterator))
    print(isinstance(set([1, 2, 3]), Iterator))
    print(isinstance("string", Iterator))
    print(isinstance(gen, Iterator))
    print(isinstance(fibonacci(10), Iterator))


def testNextItem():
    print("Turn Iterable object into Iterator object: ")
    l = [1, 2, 3]
    itrL = iter(l)
    print(next(itrL))
    print(next(itrL))
    print(next(itrL))

    print("next() The function iterates over the iterator elements:")
    fib = fibonacci(4)
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    # print(next(fib))


class NumberSequence:
    """Generate a series of numbers spaced in steps"""

    def __init__(self, init, step, max = 100):
        self.__data = init
        self.__step = step
        self.__max = max

    def __iter__(self):
        return self

    def __next__(self):
        if(self.__data < self.__max):
            tmp = self.__data
            self.__data += self.__step
            return tmp
        else:
            raise StopIteration


def NumberSequence():
    numSeq = NumberSequence(0, 5, 20)
    print(isinstance(numSeq, Iterable))
    print(isinstance(numSeq, Iterator))
    for n in numSeq:
        print(n, end="\t")


# testHospital()
# testBaseIterator()
# testLoop()
# testIterable()
testIsIterator()
# testNextItem()
# testNumberSequence()

