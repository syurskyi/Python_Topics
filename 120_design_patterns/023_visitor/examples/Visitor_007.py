# Version 2.0
#=======================================================================================================================
# Code framework
#==============================
from abc import ABCMeta, abstractmethod
# Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods

class DataNode(metaclass=ABCMeta):
    """Data Structure Class"""

    def accept(self, visitor):
        """Accept visitors"""
        visitor.visit(self)

class Visitor(metaclass=ABCMeta):
    """Visitors"""

    @abstractmethod
    def visit(self, data):
        """Access operations on data objects"""
        pass


class ObjectStructure:
    """The management class of the data structure is also a container for the data object, which can traverse all the elements in the container"""

    def __init__(self):
        self.__datas = []

    def add(self, dataElement):
        self.__datas.append(dataElement)

    def action(self, visitor):
        """Operations for data access"""
        for data in self.__datas:
            data.accept(visitor)


# Framework-based implementation
#==============================
class DesignPatternBook(DataNode):
    """Interpreting Design Patterns from a Life Perspective"""

    def getName(self):
        return "Interpreting design patterns from a life perspective》"


class Engineer(Visitor):
    """engineer"""

    def visit(self, book):
        print("Technical dog's feeling after reading the book %s: Can grasp the core idea of the model, explain it in a simple way, very insightful!" % book.getName())


class ProductManager(Visitor):
    """Product manager"""

    def visit(self, book):
        print("Product manager's feelings after reading the book %s: The picture is very interesting, and the article is very layered!" % book.getName())


class OtherFriend(Visitor):
    """Friends outside the IT circle"""

    def visit(self, book):
        print("Friends outside the IT circle feel after reading the book %s: the content of technology is aggressive, but the story is very exciting, like watching a novel or a story collection!"
              % book.getName())


# Actual combat
# =======================================================================================================================
class Animal(DataNode):
    """Animal"""

    def __init__(self, name, isMale, age, weight):
        self.__name = name
        self.__isMale = isMale
        self.__age = age
        self.__weight = weight

    def getName(self):
        return self.__name

    def isMale(self):
        return self.__isMale

    def getAge(self):
        return self.__age

    def getWeight(self):
        return self.__weight

class Cat(Animal):
    """Cat"""

    def __init__(self, name, isMale, age, weight):
        super().__init__(name, isMale, age, weight)

    def speak(self):
        print("miao")


class Dog(Animal):
    """dog"""

    def __init__(self,  name, isMale, age, weight):
        super().__init__( name, isMale, age, weight)

    def speak(self):
        print("wang")


class GenderCounter(Visitor):
    """Sex statistics"""

    def __init__(self):
        self.__maleCat = 0
        self.__femaleCat = 0
        self.__maleDog = 0
        self.__femalDog = 0

    def visit(self, data):
        if isinstance(data, Cat):
            if data.isMale():
                self.__maleCat += 1
            else:
                self.__femaleCat += 1
        elif isinstance(data, Dog):
            if data.isMale():
                self.__maleDog += 1
            else:
                self.__femalDog += 1
        else:
            print("Not support this type")

    def getInfo(self):
        print("%d males, %d females, %d males, %d females."
              % (self.__maleCat, self.__femaleCat, self.__maleDog, self.__femalDog) )


class WeightCounter(Visitor):
    """Statistics of weight"""

    def __init__(self):
        self.__catNum = 0
        self.__catWeight = 0
        self.__dogNum = 0
        self.__dogWeight  = 0

    def visit(self, data):
        if isinstance(data, Cat):
            self.__catNum +=1
            self.__catWeight += data.getWeight()
        elif isinstance(data, Dog):
            self.__dogNum += 1
            self.__dogWeight += data.getWeight()
        else:
            print("Not support this type")

    def getInfo(self):
        print("The average weight of cats is: %0.2fkg, the average weight of dogs is: %0.2fkg " %
              ((self.__catWeight / self.__catNum),(self.__dogWeight / self.__dogNum)))


class AgeCounter(Visitor):
    """Age statistics"""

    def __init__(self):
        self.__catMaxAge = 0
        self.__dogMaxAge = 0

    def visit(self, data):
        if isinstance(data, Cat):
            if self.__catMaxAge < data.getAge():
                self.__catMaxAge = data.getAge()
        elif isinstance(data, Dog):
            if self.__dogMaxAge < data.getAge():
                self.__dogMaxAge = data.getAge()
        else:
            print("Not support this type")

    def getInfo(self):
        print("The maximum age of a cat is: %s, and the maximum age of a dog is: %s" % (self.__catMaxAge, self.__dogMaxAge) )

# Test
#=======================================================================================================================

def testBook():
    book = DesignPatternBook()
    fans = [Engineer(), ProductManager(), OtherFriend()];
    for fan in fans:
        fan.read(book)

def testVisitBook():
    book = DesignPatternBook()
    objMgr = ObjectStructure()
    objMgr.add(book)
    objMgr.action(Engineer())
    objMgr.action(ProductManager())
    objMgr.action(OtherFriend())


def testAnimal():
    animals = ObjectStructure()
    animals.add(Cat("Cat1", True, 1, 5))
    animals.add(Cat("Cat2", False, 0.5, 3))
    animals.add(Cat("Cat3", False, 1.2, 4.2))
    animals.add(Dog("Dog1", True, 0.5, 8))
    animals.add(Dog("Dog2", True, 3, 52))
    animals.add(Dog("Dog3", False, 1, 21))
    animals.add(Dog("Dog4", False, 2, 25))
    genderCounter = GenderCounter()
    animals.action(genderCounter)
    genderCounter.getInfo()
    print()

    weightCounter = WeightCounter()
    animals.action(weightCounter)
    weightCounter.getInfo()
    print()

    ageCounter = AgeCounter()
    animals.action(ageCounter)
    ageCounter.getInfo()


# testBook()
# testVisitBook()
testAnimal()