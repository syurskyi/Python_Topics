# Dependence Inversion Principle, DIP for short

from abc import ABCMeta, abstractmethod
# Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods

class Animal(metaclass=ABCMeta):
    """animal"""

    def __init__(self, name):
        self._name = name

    def eat(self, food):
        if self.checkFood(food):
            print(self._name + "Eat" + food.getName())
        else:
            print(self._name + "Not eat" + food.getName())

    @abstractmethod
    def checkFood(self, food):
        """Check what foods you can eat"""
        pass


class Dog(Animal):
    """dog"""

    def __init__(self):
        super().__init__("dog")

    def checkFood(self, food):
        return food.category() == "me


class Swallow(Animal):
    """Swallow"""

    def __init__(self):
        s__. -("Sw..

    def checkFood(self, food):
        r_ f___.ca.. __ "in..


class Food(metaclass=ABCMeta):
    """food"""

    def __init__(self, name):
        _?  ?

    def getName
        r_ _n..

    @abstractmethod
    def category
        """Food category"""
        pass

    @abstractmethod
    def nutrient()
        """nutrient content"""
        pass


class Meat(Food):
    """meat"""

    def __init__(self):
        s__. - "m..

    def category(self):
        r_ "m..

    def nutrient(self):
        r_ "Protein, fat"


class Worm(Food):
    """insect"""

    def  __init__(self):
        s__. - "i..

    def category(self):
        r_ "i..

    def nutrient(self):
        r_ "Protein and trace elements"


def Food():
    dog = D..
    swallow = S..
    meat = M..
    worm = W..
    d__.e.. m..
    d__.e.. w..
    s__.e.. m..
    s__.e.. w..


Food()