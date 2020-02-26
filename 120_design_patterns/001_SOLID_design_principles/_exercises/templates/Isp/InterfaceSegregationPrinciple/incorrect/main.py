# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

# Abstract Class (Interface)
class Vehicle(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def start_engine(self): raise NotImplementedError

    @abstractmethod
    def accelerate(self): raise NotImplementedError

    @abstractmethod
    def brake(self): raise NotImplementedError

    @abstractmethod
    def lights_on(self): raise NotImplementedError

    @abstractmethod
    def signal_left(self): raise NotImplementedError

    @abstractmethod
    def signal_right(self): raise NotImplementedError

    @abstractmethod
    def change_gear(self): raise NotImplementedError

    @abstractmethod
    def stop_radio(self): raise NotImplementedError

    @abstractmethod
    def eject_cd(self): raise NotImplementedError


class Car(Vehicle):
    def start_engine(self):
        print('start engine')

    def accelerate(self):
        print('accelerate')

    def brake(self):
        print('brake')

    def lights_on(self):
        print('lights on')

    def signal_left(self):
        print('signal left')

    def signal_right(self):
        print('signal right')

    def change_gear(self):
        print('change gear')

    def stop_radio(self):
        print('stop radio')

    def eject_cd(self):
        print('eject cd')

if __name__ == '__main__':
    car = Car()
    car.start_engine()
    car.lights_on()
    car.accelerate()