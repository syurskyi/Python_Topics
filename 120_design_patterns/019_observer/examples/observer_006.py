##!/usr/bin/python

# Version 1.0
########################################################################################################################
# from abc import ABCMeta, abstractmethod
# # Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods
#
# class WaterHeater:
#     """Water heater: a good weapon to overcome the winter"""
#
#     def __init__(self):
#         self.__observers = []
#         self.__temperature = 25
#
#     def getTemperature(self):
#         return self.__temperature
#
#     def setTemperature(self, temperature):
#         self.__temperature = temperature
#         print("The current temperature is：" + str(self.__temperature) + "C")
#         self.notifies()
#
#     def addObserver(self, observer):
#         self.__observers.append(observer)
#
#     def notifies(self):
#         for o in self.__observers:
#             o.update(self)
#
#
# class Observer(metaclass=ABCMeta):
#     "Parents in bath mode and drinking mode"
#
#     @abstractmethod
#     def update(self, waterHeater):
#         pass
#
#
# class WashingMode(Observer):
#     """This mode is used for bathing"""
#
#     def update(self, waterHeater):
#         if waterHeater.getTemperature() >= 50 and waterHeater.getTemperature() < 70:
#             print("The water is burned! The temperature is just right and it can be used for bathing.")
#
#
# class DrinkingMode(Observer):
#     """This mode is used for drinking"""
#
#     def update(self, waterHeater):
#         if waterHeater.getTemperature() >= 100:
#             print(The water has boiled! Ready to drink.")


# Version 2.0
########################################################################################################################
from abc import ABCMeta, abstractmethod
# Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods


class Observer(metaclass=ABCMeta):
    """Observer base class"""

    @abstractmethod
    def update(self, observable, object):
        pass


class Observable:
    """Observed base class"""

    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, object=0):
        for o in self.__observers:
            o.update(self, object)


class WaterHeater(Observable):
    """Water heater: a good weapon to overcome the winter"""

    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("The current temperature is: " + str(self.__temperature) + "C")
        self.notifyObservers()


class WashingMode(Observer):
    """This mode is used for bathing"""

    def update(self, observable, object):
        if isinstance(observable, WaterHeater) \
                and observable.getTemperature() >= 50 and observable.getTemperature() < 70:
            print("The water is burned! The temperature is just right and it can be used for bathing.")


class DrinkingMode(Observer):
    "This mode is used for drinking"

    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 100:
            print("The water has boiled! Ready to drink.")


import time
# Import time processing module


class Account(Observable):
    """User Account"""

    def __init__(self):
        super().__init__()
        self.__latestIp = {}
        self.__latestRegion = {}

    def login(self, name, ip, time):
        region = self.__getRegion(ip)
        if self.__isLongDistance(name, region):
            self.notifyObservers({"name": name, "ip": ip, "region": region, "time": time})
        self.__latestRegion[name] = region
        self.__latestIp[name] = ip

    def __getRegion(self, ip):
        # Obtain area information by IP address. This is just a simulation.
        # The IP address resolution service should be called in a real project.
        ipRegions = {
            "101.47.18.9": "Hangzhou, Zhejiang",
            "67.218.147.69":"Los Angeles, USA"
        }
        region = ipRegions.get(ip)
        return "" if region is None else region

    def __isLongDistance(self, name, region):
        # Calculate the regional difference between this login and the last login.
        # Here is just to use string matching to simulate, in a real project, you should call geographic information
        # related services
        latestRegion = self.__latestRegion.get(name)
        return latestRegion is not None and latestRegion != region;


class SmsSender(Observer):
    """SMS sender"""

    def update(self, observable, object):
        print("[send a text message] " + object["name"] + "Hello! It is detected that your account may be logged in abnormally. Last login information:\n"
              + "Registration area:" + object["region"] + "  Login ip: " + object["ip"] + "  Log in time: "
              + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))


class MailSender(Observer):
    """Mail sender"""

    def update(self, observable, object):
        print("[Send by mail] " + object["name"] + "Hello! It is detected that your account may be logged in abnormally. Last login information:\n"
              + "Registration area:" + object["region"] + "  log inip：" + object["ip"] + "  Log in time: "
              + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))


def testWaterHeater():
    heater = WaterHeater()
    washingObser = WashingMode()
    drinkingObser = DrinkingMode()
    heater.addObserver(washingObser)
    heater.addObserver(drinkingObser)
    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(100)


def testLogin():
    accout = Account()
    accout.addObserver(SmsSender())
    accout.addObserver(MailSender())
    accout.login("Tony", "101.47.18.9", time.time())
    accout.login("Tony", "67.218.147.69", time.time())



def testTime():
    print(time.time())
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))
    print(strTime)

# testWaterHeater()
testLogin()
# testTime()

# ipRegion = {
#             "101.47.18.9": "Hangzhou, Zhejiang",
#             "67.218.147.69":"Los Angeles, USA"
#         }
#
# print(ipRegion["101.47.18.90"])
