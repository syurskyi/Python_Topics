VEHICLE_ID = {
    'MOTOCYCLE': 'MOTOCYCLE',
    'CAR': 'CAR',
    'BUS': 'BUS',
}


class Vehicle:
    ___ __init__(self):
        self.type = ''
        self.costs = 0
        self.at_level = N..
        self.at_spots = N..

    ___ unpark(self):
        __ n.. self.at_level:
            r..

        ___ x, y __ self.at_spots:
            self.at_level.spots[x, y] = N..

        self.at_level = N..
        self.at_spots = N..


class Motorcycle(Vehicle):
    ___ __init__(self):
        self.type = VEHICLE_ID['MOTOCYCLE']
        self.costs = 1


class Car(Vehicle):
    ___ __init__(self):
        self.type = VEHICLE_ID['CAR']
        self.costs = 1


class Bus(Vehicle):
    ___ __init__(self):
        self.type = VEHICLE_ID['BUS']
        self.costs = 5


class Level:
    ___ __init__(self, id, m, n):
        self.id = id
        self.m = m
        self.n = n
        self.spots = {}

    ___ get_range(self, vehicle_type):
        quarter = self.n // 4

        __ vehicle_type __ VEHICLE_ID['BUS']:
            r.. r..(quarter * 3, self.n)

        __ vehicle_type __ VEHICLE_ID['CAR']:
            r.. r..(quarter, self.n)

        r.. r..(self.n)

    ___ park_vehicle(self, vehicle):
        """
        :type vehicle: Vehicle
        :rtype: bool
        """
        RANGE = self.get_range(vehicle.type)

        ___ x __ r..(self.m):
            gotcha = 0

            ___ y __ RANGE:
                __ self.spots.get((x, y)):
                    gotcha = 0
                    continue

                gotcha += 1

                __ gotcha __ vehicle.costs:
                    spots    # list

                    ___ i __ r..(y, y - gotcha, -1):
                        spots.a..((x, i))
                        self.spots[x, i] = vehicle

                    vehicle.at_level = self
                    vehicle.at_spots = spots
                    r.. True

        r.. False


class ParkingLot:
    ___ __init__(self, k, m, n):
        """
        :type k: int, number of levels
        :type m: int, each level has m rows of spots
        :type n: int, each row has n spots
        """
        self.levels = [Level(i, m, n) ___ i __ r..(k)]

    ___ park_vehicle(self, vehicle):
        """
        :type vehicle: Vehicle
        :rtype: bool
        """
        __ any(
            level.park_vehicle(vehicle)
            ___ level __ self.levels
        ):
            r.. True

        r.. False

    ___ unpark_vehicle(self, vehicle):
        """
        :type vehicle: Vehicle
        """
        vehicle.unpark()
