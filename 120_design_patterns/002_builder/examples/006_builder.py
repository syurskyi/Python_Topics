# Version 2.0
#=======================================================================================================================
from abc import ABCMeta, abstractmethod
# Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods

class Toy(metaclass=ABCMeta):
    """toy"""

    def __init__(self, name):
        self._name = name
        self.__components = []

    def getName(self):
        return self._name

    def addComponent(self, component, count = 1, unit = "个"):
        self.__components.append([component, count, unit])
        # print("%s increased %d %s%s" % (self._name, count, unit, component) );

    @abstractmethod
    def feature(self):
        pass


class Car(Toy):
    """Trolley"""

    def feature(self):
        print("I'm %s, I can run fast ..." % self._name)


class Manor(Toy):
    """manor"""

    def feature(self):
        print("I'm  %s, I can watch it, and I can also play!" % self._name)


class ToyBuilder(metaclass=ABCMeta):
    """Toy builder"""

    @abstractmethod
    def buildProduct(self):
        pass


class CarBuilder(ToyBuilder):
    """Construction class of car"""

    def buildProduct(self):
        car = Car("Mini car")
        print("Building %s ....." % car.getName())
        car.addComponent("wheel", 4)
        car.addComponent("Bodywork", 1)
        car.addComponent("engine", 1)
        car.addComponent("steering wheel")
        return car


class ManorBuilder(ToyBuilder):
    """庄园的构建类"""

    def buildProduct(self):
        manor = Manor("Taotao Small Manor")
        print("Building %s ...." % manor.getName())
        manor.addComponent('living room', 1, "between")
        manor.addComponent('bedroom', 2, "between")
        manor.addComponent("study", 1, "between")
        manor.addComponent("kitchen", 1, "between")
        manor.addComponent("garden", 1, "Each")
        manor.addComponent("Fence", 1, "Blocking")
        return manor

class BuilderMgr:
    """Construction Management"""

    def __init__(self):
        self.__carBuilder = CarBuilder()
        self.__manorBuilder = ManorBuilder()

    def buildCar(self, num):
        count = 0
        products = []
        while(count < num):
            car = self.__carBuilder.buildProduct()
            products.append(car)
            count +=1
            print("Construction completed %d Car %s" % (count, car.getName()) )
        return products

    def buildManor(self, num):
        count = 0
        products = []
        while (count < num):
            manor = self.__manorBuilder.buildProduct()
            products.append(manor)
            count += 1
            print("Construction completed %d Each %s" % (count, manor.getName()))
        return products


# Test
# ==============================
def testAdvancedBuilder():
    builderMgr = BuilderMgr()
    builderMgr.buildManor(2)
    print()
    builderMgr.buildCar(4)


# testBuilder()
testAdvancedBuilder()
