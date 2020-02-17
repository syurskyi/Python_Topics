#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 11/26/2017

# Version 1.0
#=======================================================================================================================
from abc import ABCMeta, abstractmethod
# Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods

class Person(metaclass=ABCMeta):
    """people"""

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def wear(self):
        print("Dress code")


class Engineer(Person):
    """engineer"""

    def __init__(self, name, skill):
        super().__init__(name)
        self.__skill = skill

    def getSkill(self):
        return self.__skill

    def wear(self):
        print("I'm " + self.getSkill() + "engineer " + self._name, end="， ")
        super().wear()

class Teacher(Person):
    "teacher"

    def __init__(self, name, title):
        super().__init__(name)
        self.__title = title

    def getTitle(self):
        return self.__title

    def wear(self):
        print("I'm " + self._name + self.getTitle(), end="， ")
        super().wear()

class ClothingDecorator(Person):
    """Base class for clothing decorators"""

    def __init__(self, person):
        self._decorated = person

    def wear(self):
        self._decorated.wear()
        self.decorate()

    @abstractmethod
    def decorate(self):
        pass


class CasualPantDecorator(ClothingDecorator):
    """Casual pants decorator"""

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("One pair of khaki slacks")


class BeltDecorator(ClothingDecorator):
    """Belt decorator"""

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("Black belt with a silver pin buckle")

class LeatherShoesDecorator(ClothingDecorator):
    """Leather shoe decorator"""

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("A pair of dark casual leather shoes")

class KnittedSweaterDecorator(ClothingDecorator):
    """Knitted sweater decorator"""

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("A fuchsia knitted sweater")


class WhiteShirtDecorator(ClothingDecorator):
    """White shirt decorator"""

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("A white shirt")


class GlassesDecorator(ClothingDecorator):
    """Glasses decorator"""

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("A pair of square black frame glasses")




# Test
#=======================================================================================================================
def mainDecorator():
    tony = Engineer("Tony", "Client")
    pant = CasualPantDecorator(tony)
    belt = BeltDecorator(pant)
    shoes = LeatherShoesDecorator(belt)
    shirt = WhiteShirtDecorator(shoes)
    sweater = KnittedSweaterDecorator(shirt)
    glasses = GlassesDecorator(sweater)
    glasses.wear()

    print()
    decorateTeacher = GlassesDecorator(WhiteShirtDecorator(LeatherShoesDecorator(Teacher("wells", "professor"))))
    decorateTeacher.wear()


def mainDecorator2():
    tony = Engineer("Tony", "Client")
    sweater = KnittedSweaterDecorator(tony)
    shirt = WhiteShirtDecorator(sweater)
    glasses = GlassesDecorator(shirt)
    glasses.wear()

mainDecorator()
print()
print('#' * 50)
mainDecorator2()