class Employee:

    def __init__(self, name, age, address, number, vehicle=None):
        self.name = name
        self._age = age
        self._address = address
        self.__number = number
        self.__vehicle = vehicle
