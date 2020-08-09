VEHICLE_ID = {
    'MOTOCYCLE': 'MOTOCYCLE',
    'CAR': 'CAR',
    'BUS': 'BUS',
}


class Vehicle:
    ___ __init__(self
        self.type = ''
        self.costs = 0
        self.at_level = None
        self.at_spots = None

    ___ unpark(self
        __ not self.at_level:
            r_

        for x, y in self.at_spots:
            self.at_level.spots[x, y] = None

        self.at_level = None
        self.at_spots = None


class Motorcycle(Vehicle
    ___ __init__(self
        self.type = VEHICLE_ID['MOTOCYCLE']
        self.costs = 1


class Car(Vehicle
    ___ __init__(self
        self.type = VEHICLE_ID['CAR']
        self.costs = 1


class Bus(Vehicle
    ___ __init__(self
        self.type = VEHICLE_ID['BUS']
        self.costs = 5


class Level:
    ___ __init__(self, id, m, n
        self.id = id
        self.m = m
        self.n = n
        self.spots = {}

    ___ get_range(self, vehicle_type
        quarter = self.n // 4

        __ vehicle_type __ VEHICLE_ID['BUS']:
            r_ range(quarter * 3, self.n)

        __ vehicle_type __ VEHICLE_ID['CAR']:
            r_ range(quarter, self.n)

        r_ range(self.n)

    ___ park_vehicle(self, vehicle
        """
        :type vehicle: Vehicle
        :rtype: bool
        """
        RANGE = self.get_range(vehicle.type)

        for x in range(self.m
            gotcha = 0

            for y in RANGE:
                __ self.spots.get((x, y)):
                    gotcha = 0
                    continue

                gotcha += 1

                __ gotcha __ vehicle.costs:
                    spots = []

                    for i in range(y, y - gotcha, -1
                        spots.append((x, i))
                        self.spots[x, i] = vehicle

                    vehicle.at_level = self
                    vehicle.at_spots = spots
                    r_ True

        r_ False


class ParkingLot:
    ___ __init__(self, k, m, n
        """
        :type k: int, number of levels
        :type m: int, each level has m rows of spots
        :type n: int, each row has n spots
        """
        self.levels = [Level(i, m, n) for i in range(k)]

    ___ park_vehicle(self, vehicle
        """
        :type vehicle: Vehicle
        :rtype: bool
        """
        __ any(
            level.park_vehicle(vehicle)
            for level in self.levels

            r_ True

        r_ False

    ___ unpark_vehicle(self, vehicle
        """
        :type vehicle: Vehicle
        """
        vehicle.unpark()
