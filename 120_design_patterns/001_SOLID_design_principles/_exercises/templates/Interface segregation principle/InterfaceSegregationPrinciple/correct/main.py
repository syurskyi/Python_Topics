# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

# Abstract Class

class SpeedControl(object):

    @abstractmethod
    def start_engine(self): raise NotImplementedError

    @abstractmethod
    def accelerate(self): raise NotImplementedError

    @abstractmethod
    def brake(self): raise NotImplementedError

    @abstractmethod
    def change_gear(self): raise NotImplementedError

class RadioCd(object):

    @abstractmethod
    def stop_radio(self): raise NotImplementedError

    @abstractmethod
    def eject_cd(self): raise NotImplementedError

# implements

class CarSpeedControl(SpeedControl):

    def start_engine(self):
        print('start engine')

    def accelerate(self):
        print('accelerate')

    def brake(self):
        print('brake')

    def change_gear(self):
        print('change gear')

class CarRadioCd(RadioCd):

    def stop_radio(self):
        print('stop radio')

    def eject_cd(self):
        print('eject cd')

# Decorator

def validate_type_hinting(func):
    def inner(*argv):
        if not issubclass(type(argv[1]), SpeedControl) : print("%s is a type %s, the function need a SpeedControl type" % (argv[1], type(argv[1]))); exit(0)
        if not issubclass(type(argv[2]), RadioCd) : print("%s is a type %s, the function need a RadioCd type" % (argv[2], type(argv[2]))); exit(0)
        return func(*argv)
    return inner

# Vehicle

class Car(object):

    @validate_type_hinting
    def __init__(self, speed_control, radio_cd):
        self.speed_control = speed_control
        self.radio_cd = radio_cd

if __name__ == '__main__':
    speed_control = CarSpeedControl()
    radio_cd = CarRadioCd()
    car = Car(speed_control, radio_cd)
    car.speed_control.start_engine()
    car.speed_control.accelerate()
