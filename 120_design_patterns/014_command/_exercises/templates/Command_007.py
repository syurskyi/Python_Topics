#=======================================================================================================================
from abc import ABCMeta, abstractmethod
#  Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods

class Chef():
    """chef"""

    def steamFood(self, originalMaterial):
        print("%s steaming .." % originalMaterial)
        return "Steamed" + originalMaterial

    def stirFriedFood(self, originalMaterial):
        print("%s s being fried ..." % originalMaterial)
        return "Spicy Fried" + originalMaterial

class Order(metaclass=ABCMeta):
    """Order"""

    def __init__(self, name, originalMaterial):
        self._chef = Chef()
        self._name = name
        self._originalMaterial = originalMaterial

    def getDisplayName(self):
        return self._name + self._originalMaterial

    @abstractmethod
    def processingOrder(self):
        pass

class SteamedOrder(Order):
    """Steamed"""

    def __init__(self, originalMaterial):
        super().__init__("Steamed", originalMaterial)

    def processingOrder(self):
        if(self._chef is not None):
            return self._chef.steamFood(self._originalMaterial)
        return ""


class SpicyOrder(Order):
    """Spicy Fried"""

    def __init__(self, originalMaterial):
        super().__init__("Spicy Fried", originalMaterial)

    def processingOrder(self):
        if (self._chef is not None):
            return self._chef.stirFriedFood(self._originalMaterial)
        return ""


class Waiter:
    """Waiter"""

    def __init__(self, name):
        self.__name = name
        self.__order = None

    def receiveOrder(self, order):
        self.__order = order
        print("Waiter %s: Your order for %s  has been received, please be patient" % (self.__name, order.getDisplayName()) )

    def placeOrder(self):
        food = self.__order.processingOrder()
        print("Waite %s  Your meal %s is ready, please use it slowly!" % (self.__name, food) )



# class Customer:
#     "Customer"
#
#     def __init__(self, name):
#         self.__name = name
#
#     def order(self):

# Version 2.0
#=======================================================================================================================
# Code framework
#==============================
from abc import ABCMeta, abstractmethod
# Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods

class Command(metaclass=ABCMeta):
    """Command's Abstract Class"""

    @abstractmethod
    def execute(self):
        pass

class CommandImpl(Command):
    """The concrete implementation class of the command"""

    def __init__(self, receiver):
        self.__receiver = receiver

    def execute(self):
        self.__receiver.doSomething()

class Receiver:
    """Recipient of the command"""

    def doSomething(self):
        print("do something...")

class Invoker:
    """Scheduler"""

    def __init__(self):
        self.__command = None

    def setCommand(self, command):
        self.__command = command

    def action(self):
        if self.__command is not None:
            self.__command.execute()


# Framework-based implementation
#==============================

# Test
#=======================================================================================================================

def Order():
    waiter = Waiter("Anna")
    steamedOrder = SteamedOrder("Hairy crab")
    print(" Customer David I want a copy %s" % steamedOrder.getDisplayName())
    waiter.receiveOrder(steamedOrder)
    waiter.placeOrder()
    print()

    spicyOrder = SpicyOrder("Hair crab")
    print("Customer Tony I want a copy %s" % spicyOrder.getDisplayName())
    waiter.receiveOrder(spicyOrder)
    waiter.placeOrder()


def client():
    invoker = Invoker()
    command = CommandImpl(Receiver())
    invoker.setCommand(command)
    invoker.action()


# Order()
client()

