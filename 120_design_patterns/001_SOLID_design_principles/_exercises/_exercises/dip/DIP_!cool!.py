# Dependence Inversion Principle, DIP for short

from abc import ABCMeta, abstractmethod
# Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods

class Animal(metaclass=ABCMeta):
    """animal"""

    def __init__(self, name):
        self._name = name

    def eat(self, food):
        if self.checkFood(food):
            print(self._name + " Eat " + food.getName())
        else:
            print(self._name + " Not eat " + food.getName())

    @abstractmethod
    def checkFood(self, food):
        """Check what foods you can eat"""
        pass


class Dog(Animal):
    """dog"""

    def __init__(self):
        super().__init__("dog")

    def checkFood(self, food):
        return food.category() == "meat"


class Swallow(Animal):
    """Swallow"""

    def __init__(self):
        super().__init__("Swallow")

    def checkFood(self, food):
        return food.category == "insect"


class Food(metaclass=ABCMeta):
    """food"""

    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    @abstractmethod
    def category(self):
        """Food category"""
        pass

    @abstractmethod
    def nutrient(self):
        """nutrient content"""
        pass


class Meat(Food):
    """meat"""

    def __init__(self):
        super().__init__("meat")

    def category(self):
        return "meat"

    def nutrient(self):
        return "Protein, fat"


class Worm(Food):
    """insect"""

    def __init__(self):
        super().__init__("insect")

    def category(self):
        return "insect"

    def nutrient(self):
        return "Protein and trace elements"


def food():
    dog = Dog()
    swallow = Swallow()
    meat = Meat()
    worm = Worm()
    dog.eat(meat)
    dog.eat(worm)
    swallow.eat(meat)
    swallow.eat(worm)


food()