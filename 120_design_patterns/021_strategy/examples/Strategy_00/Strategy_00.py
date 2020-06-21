#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 5/1/2018

# Version 1.0
#=======================================================================================================================
from abc import ABCMeta, abstractmethod
#  Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods


class IVehicle(metaclass=ABCMeta):
    """Abstract Classes of Transport"""

    @abstractmethod
    def running(self):
        pass


class SharedBicycle(IVehicle):
    """Bicycle sharing"""

    def running(self):
        print("Riding a shared bike (light and convenient", end='')


class ExpressBus(IVehicle):
    """BRT"""

    def running(self):
        print("By BRT (Economic Green", end='')

class Express(IVehicle):
    """express train"""

    def running(self):
        print("Express (quick and easy)", end='')


class Subway(IVehicle):
    """subway"""

    def running(self):
        print("By subway (efficient and safe)", end='')


class Classmate:
    """Classmates attending dinner"""

    def __init__(self, name, vechicle):
        self.__name = name
        self.__vechicle = vechicle

    def attendTheDinner(self):
        print(self.__name + " ", end='')
        self.__vechicle.running()
        print("Come for a dinner!")


# Version 2.0
#=======================================================================================================================
# Code framework
#==============================
from abc import ABCMeta, abstractmethod
# Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods

class Person:
    """Humanity"""

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def showMysef(self):
        print("%s age: %dyear old，body weight：%0.2fkg，height：%0.2fm" % (self.name, self.age, self.weight, self.height) )


class ICompare(metaclass=ABCMeta):
    """Comparison algorithm"""

    @abstractmethod
    def comparable(self, person1, person2):
        "person1 > person2 return value>0，person1 == person2 return0， person1 < person2 The return value is less than 0"
        pass


class CompareByAge(ICompare):
    """Sort by age"""

    def comparable(self, person1, person2):
        return person1.age - person2.age


class CompareByHeight(ICompare):
    """Sort by height"""

    def comparable(self, person1, person2):
        return person1.height - person2.height


class CompareByHeightAndWeight(ICompare):
    """Sort by height and weight (Weights for height and weight are 0.6 and 0.4, respectively) """

    def comparable(self, person1, person2):
        value1 = person1.height * 0.6 + person1.weight * 0.4
        value2 = person2.height * 0.6 + person2.weight * 0.4
        return value1 - value2


class SortPerson:
    "Person Sorting class"

    def __init__(self, compare):
        self.__compare = compare

    def sort(self, personList):
        """Sorting Algorithm Here is the simplest bubble sort"""
        n = len(personList)
        for i in range(0, n-1):
            for j in range(0, n-i-1):
                if(self.__compare.comparable(personList[j], personList[j+1]) > 0):
                    tmp = personList[j]
                    personList[j] = personList[j+1]
                    personList[j+1] = tmp
            j += 1
        i += 1


# Framework-based implementation
#==============================


# Test
#=======================================================================================================================

def TheDinner():
    sharedBicycle = SharedBicycle()
    joe = Classmate("Joe", sharedBicycle)
    joe.attendTheDinner()
    helen = Classmate("Helen", Subway())
    helen.attendTheDinner()
    henry = Classmate("Henry", ExpressBus())
    henry.attendTheDinner()
    ruby = Classmate("Ruby", Express())
    ruby.attendTheDinner()



def SortPerson():
    personList = [
        Person("Tony", 2, 54.5, 0.82),
        Person("Jack", 31, 74.5, 1.80),
        Person("Nick", 54, 44.5, 1.59),
        Person("Eric", 23, 62.0, 1.78),
        Person("Helen", 16, 45.7, 1.60)
    ]
    ageSorter = SortPerson(CompareByAge())
    ageSorter.sort(personList)
    print("Results sorted by age: ")
    for person in personList:
        person.showMysef()
    print()

    heightSorter = SortPerson(CompareByHeight())
    heightSorter.sort(personList)
    print("Results sorted by height: ")
    for person in personList:
        person.showMysef()
    print()

    heightWeightSorter = SortPerson(CompareByHeightAndWeight())
    heightWeightSorter.sort(personList)
    print("Results sorted by height and weight:")
    for person in personList:
        person.showMysef()



from operator import itemgetter,attrgetter

def PersonListInPython():
    "Sorting Persons in Python"

    personList = [
        Person("Tony", 2, 54.5, 0.82),
        Person("Jack", 31, 74.5, 1.80),
        Person("Nick", 54, 44.5, 1.59),
        Person("Eric", 23, 62.0, 1.78),
        Person("Helen", 16, 45.7, 1.60)
    ]

    # Sort by age and height using the operator module
    sortedPerons = sorted(personList, key = attrgetter('age'))
    sortedPerons1 = sorted(personList, key=attrgetter('height'))

    print("Results sorted by age")
    for person in sortedPerons:
        person.showMysef()
    print()
    print("Results sorted by height:")
    for person in sortedPerons1:
        person.showMysef()


    # print("Sort according to the combination of height and weight:")
    # sortedPerons1 = sorted(personList, key=attrgetter("height" + "weight"))
    # for person in sortedPerons1:
    #     person.showMysef()



TheDinner()
print()
SortPerson()
PersonListInPython()
#
#
# # testArray()