#!/usr/bin/env python
# Written by: DGC

import abc

#==============================================================================
class Vehicle(object):

    def __init__(self, type_name):
        self.type = type_name
        self.wheels = None
        self.doors = None
        self.seats = None

    def view(self):
        print(
            "This vehicle is a " +
            self.type +
            " with; " +
            str(self.wheels) +
            " wheels, " +
            str(self.doors) +
            " doors, and " +
            str(self.seats) +
            " seats."
            )

#==============================================================================
class VehicleBuilder(object):
    """
    An abstract builder class, for concrete builders to be derived from.
    """
    __metadata__ = abc.ABCMeta

    @abc.abstractmethod
    def make_wheels(self):
        raise NotImplemented

    @abc.abstractmethod
    def make_doors(self):
        raise NotImplemented


    @abc.abstractmethod
    def make_seats(self):
        raise NotImplemented
#==============================================================================
class CarBuilder(VehicleBuilder):

    def __init__(self):
        self.vehicle = Vehicle("Car ")

    def make_wheels(self):
        self.vehicle.wheels = 4

    def make_doors(self):
        self.vehicle.doors = 3

    def make_seats(self):
        self.vehicle.seats = 5

#==============================================================================
class BikeBuilder(Vehicle):

    def __init__(self):
        self.vehicle = Vehicle("Bike")

    def make_wheels(self):
        self.vehicle.wheels = 2

    def make_doors(self):
        self.vehicle.doors = 0

    def make_seats(self):
        self.vehicle.seats = 2

#==============================================================================
class VehicleManufacturer(object):
    """
    The director class, this will keep a concrete builder.
    """

    def __init__(self):
        self.builder = None

    def create(self):
        """
        Creates and returns a Vehicle using ____.builder
        Precondition: not ____.builder is N..
        """
        assert not self.builder is None, "No defined builder"
        self.builder.make_wheels()
        self.builder.make_doors()
        self.builder.make_seats()
        return self.builder.vehicle

#==============================================================================
if (__name__ == '__main__'):
    manufacture = VehicleManufacturer()

    manufacture.builder = CarBuilder()
    car = manufacture.create()
    car.view()

    manufacture.builder = BikeBuilder()
    bike = manufacture.create()
    bike.view()
