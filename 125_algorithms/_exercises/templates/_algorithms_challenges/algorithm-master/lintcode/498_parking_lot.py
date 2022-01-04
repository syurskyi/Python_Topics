VEHICLE_ID = {
    'MOTOCYCLE': 'MOTOCYCLE',
    'CAR': 'CAR',
    'BUS': 'BUS',
}


c_ Vehicle:
    ___ - ):
        t.. = ''
        costs = 0
        at_level = N..
        at_spots = N..

    ___ unpark
        __ n.. at_level:
            r..

        ___ x, y __ at_spots:
            at_level.spots[x, y] = N..

        at_level = N..
        at_spots = N..


c_ Motorcycle(Vehicle):
    ___ - ):
        t.. = VEHICLE_ID['MOTOCYCLE']
        costs = 1


c_ Car(Vehicle):
    ___ - ):
        t.. = VEHICLE_ID['CAR']
        costs = 1


c_ Bus(Vehicle):
    ___ - ):
        t.. = VEHICLE_ID['BUS']
        costs = 5


c_ Level:
    ___ - , id, m, n):
        id = id
        m = m
        n = n
        spots    # dict

    ___ get_range(self, vehicle_type):
        quarter = n // 4

        __ vehicle_type __ VEHICLE_ID['BUS']:
            r.. r..(quarter * 3, n)

        __ vehicle_type __ VEHICLE_ID['CAR']:
            r.. r..(quarter, n)

        r.. r..(n)

    ___ park_vehicle(self, vehicle):
        """
        :type vehicle: Vehicle
        :rtype: bool
        """
        RANGE = get_range(vehicle.t..)

        ___ x __ r..(m):
            gotcha = 0

            ___ y __ RANGE:
                __ spots.get((x, y)):
                    gotcha = 0
                    _____

                gotcha += 1

                __ gotcha __ vehicle.costs:
                    spots    # list

                    ___ i __ r..(y, y - gotcha, -1):
                        spots.a..((x, i))
                        spots[x, i] = vehicle

                    vehicle.at_level = self
                    vehicle.at_spots = spots
                    r.. T..

        r.. F..


c_ ParkingLot:
    ___ - , k, m, n):
        """
        :type k: int, number of levels
        :type m: int, each level has m rows of spots
        :type n: int, each row has n spots
        """
        levels = [Level(i, m, n) ___ i __ r..(k)]

    ___ park_vehicle(self, vehicle):
        """
        :type vehicle: Vehicle
        :rtype: bool
        """
        __ any(
            level.park_vehicle(vehicle)
            ___ level __ levels
        ):
            r.. T..

        r.. F..

    ___ unpark_vehicle(self, vehicle):
        """
        :type vehicle: Vehicle
        """
        vehicle.unpark()
