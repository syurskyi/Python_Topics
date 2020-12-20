import abc
from abc import abstractmethod

class AbstractClass(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self):
        pass

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    def template_method(self):
        print("Defining the Algorithm. Operation1 follows Operation2")
        self.operation2()
        self.operation1()


class ConcreteClass(AbstractClass):

    def operation1(self):
        print("My Concrete Operation1")
        g = nuke.createNode('Grade', inpanel=False)
    def operation2(self):
        print("Operation 2 remains same")
        b = nuke.createNode('Blur', inpanel=False)


class Client:
    def main(self):
        self.concreate = ConcreteClass()
        self.concreate.template_method()

client = Client()
client.main()