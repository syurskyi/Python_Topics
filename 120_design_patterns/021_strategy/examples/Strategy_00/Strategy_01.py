#=======================================================================================================================
from abc import ABCMeta, abstractmethod


class IVehicle(metaclass=ABCMeta):

    @abstractmethod
    def running(self):
        pass


class SharedBicycle(IVehicle):

    def running(self):
        print("aaaa", end='')


class ExpressBus(IVehicle):

    def running(self):
        print("nbbb", end='')

class Express(IVehicle):


    def running(self):
        print("nnnn", end='')


class Subway(IVehicle):

    def running(self):
        print("mmmm)", end='')


class Classmate:

    def __init__(self, name, vechicle):
        self.__name = name
        self.__vechicle = vechicle

    def attendTheDinner(self):
        print(self.__name + " ", end='')
        self.__vechicle.running()
        print(" gggg")

