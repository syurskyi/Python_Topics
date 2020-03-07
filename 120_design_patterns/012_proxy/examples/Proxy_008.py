#=======================================================================================================================
from abc import ABCMeta, abstractmethod
# Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods

class ReceiveParcel(metaclass=ABCMeta):
    """Receive Parcel Abstract Class"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def receive(self, parcelContent):
        pass


# class TonyReception(ReceiveParcel):
#     """Tony receives"""
#
#     def __init__(self, name, phoneNum):
#         super().__init__(name)
#         self.__phoneNum = phoneNum
#
#     def getPhoneNum(self):
#         return self.__phoneNum
#
#     def receive(self, parcelContent):
#         print("Cargo owner：%s，phone number：%s" % (self.getName(), self.getPhoneNum()) )
#         print("Received a parcel，Package contents:%s" % parcelContent)
#
#
# class WendyReception(ReceiveParcel):
#     """Wendy Collection"""
#
#     def __init__(self, name, receiver):
#         super().__init__(name)
#         self.__receiver = receiver
#
#     def receive(self, parcelContent):
#         print("I'm a friend of %s, I'll help him collect the delivery!" % (self.__receiver.getName() + "") )
#         if(self.__receiver is not None):
#             self.__receiver.receive(parcelContent)
#         print("Income:%s" % self.getName())


# Version 2.0
#=======================================================================================================================
# Code framework
#==============================
from abc import ABCMeta, abstractmethod
# Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods

class Subject(metaclass=ABCMeta):
    """Theme class"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def request(self, content = ''):
        pass


class RealSubject(Subject):
    """Real theme"""

    def request(self, content):
        print("RealSubject todo something...")


class ProxySubject(Subject):
    """Agent theme class"""

    def __init__(self, name, subject):
        super().__init__(name)
        self._realSubject = subject

    def request(self, content = ''):
        self.preRequest()
        if(self._realSubject is not None):
            self._realSubject.request(content)
        self.afterRequest()

    def preRequest(self):
        print("preRequest")

    def afterRequest(self):
        print("afterRequest")


# Framework-based implementation
#==============================

class TonyReception(Subject):
    """Tony receives"""

    def __init__(self, name, phoneNum):
        super().__init__(name)
        self.__phoneNum = phoneNum

    def getPhoneNum(self):
        return self.__phoneNum

    def request(self, content):
        print("Cargo owner: %s，phone number: %s" % (self.getName(), self.getPhoneNum()))
        print("Received a package, package content: %s" % str(content))


class WendyReception(ProxySubject):
    """Wendy Collection"""

    def __init__(self, name, receiver):
        super().__init__(name, receiver)

    def preRequest(self):
        print("I'm a friend of %s  I'll help him collect the delivery!" % (self._realSubject.getName() + ""))

    def afterRequest(self):
        print("Recipient: %s" % self.getName())


# Test
#=======================================================================================================================
def ReceiveParcel():
    tony = TonyReception("Tony", "18512345678")
    print("Tony receives:")
    tony.receive("Snow boots")
    print()

    print("Wendy Collection:")
    wendy = WendyReception("Wendy", tony)
    wendy.receive("Snow boots")


def Proxy():
    realObj = RealSubject('RealSubject')
    proxyObj = ProxySubject('ProxySubject', realObj)
    proxyObj.request()

def ReceiveParcel2():
    tony = TonyReception("Tony", "18512345678")
    print("Tony receives: ")
    tony.request("Snow boots")
    print()

    print("Wendy Collection:")
    wendy = WendyReception("Wendy", tony)
    wendy.request("Snow Boots")

# ReceiveParcel()
# Proxy()
ReceiveParcel2()

