#=======================================================================================================================
class HouseInfo:
    """Listing Information"""

    def __init__(self, area, price, hasWindow, hasBathroom, hasKitchen, address, owner):
        self.__area = area
        self.__price = price
        self.__hasWindow = hasWindow
        self.__hasBathroom = hasBathroom
        self.__hasKitchen = hasKitchen
        self.__address = address
        self.__owner = owner

    def getAddress(self):
        return self.__address

    def getOwnerName(self):
        return self.__owner.getName()

    def showInfo(self, isShowOwner = True):
        print("Area: " + str(self.__area) + "square meter",
              "Price: " + str(self.__price) + "yuan",
              "Window: " + ("Yes" if self.__hasWindow else "No"),
              "Bathroom: " + self.__hasBathroom,
              "Kitchen:" + ("Yes" if self.__hasKitchen else "No"),
              "Address:" + self.__address,
              "Host:" + self.getOwnerName() if isShowOwner else "")


class HousingAgency:
    """Housing agency"""

    def __init__(self, name):
        self.__houseInfos = []
        self.__name = name

    def getName(self):
        return self.__name

    def addHouseInfo(self, houseInfo):
        self.__houseInfos.append(houseInfo)

    def removeHouseInfo(self, houseInfo):
        for info in self.__houseInfos:
            if(info == houseInfo):
                self.__houseInfos.remove(info)

    def getSearchCondition(self, description):
        """Here's a logic that turns user descriptions into search criteria
         (To save space, return to the description as it is)"""
        return description

    def getMatchInfos(self, searchCondition):
        """Find the best match based on the properties of the listing
         (To save space, the matching process is omitted here, all output)"""
        print(self.getName(), "Find the best fit for you:")
        for info in self.__houseInfos:
            info.showInfo(False)
        return  self.__houseInfos

    def signContract(self, houseInfo, period):
        """Sign an agreement with the landlord"""
        print(self.getName(), "With the host", houseInfo.getOwnerName(), "Sign", houseInfo.getAddress(),
              "Lease contract for house", period, "year. During the contract", self.getName(), "Right to use and sublet it!")

    def signContracts(self, period):
        for info in self.__houseInfos :
            self.signContract(info, period)


class HouseOwner:
    """landlord"""

    def __init__(self, name):
        self.__name = name
        self.__houseInfo = None

    def getName(self):
        return self.__name

    def setHouseInfo(self, address, area, price, hasWindow, bathroom, kitchen):
        self.__houseInfo = HouseInfo(area, price, hasWindow, bathroom, kitchen, address, self)

    def publishHouseInfo(self, agency):
        agency.addHouseInfo(self.__houseInfo)
        print(self.getName() + "in", agency.getName(), "Post Property Rental Information:")
        self.__houseInfo.showInfo()


class Customer:
    """Users, poor middle peasants renting houses"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def findHouse(self, description, agency):
        print("I am" + self.getName() + ", I want to find one\"" + description + "\"House of")
        print()
        return agency.getMatchInfos(agency.getSearchCondition(description))

    def seeHouse(self, houseInfos):
        """Go to the house and choose the most used house
         (The process of viewing a house is omitted here)"""
        size = len(houseInfos)
        return houseInfos[size-1]

    def signContract(self, houseInfo, agency, period):
        """Sign an agreement with an intermediary"""
        print(self.getName(), "Intermediary", agency.getName(), "Sign", houseInfo.getAddress(),
              "Lease contract for a house", period, "year. During the contract", self.__name, "Right to use it!")

# Version 2.0
#=======================================================================================================================
# Code framework
#==============================
class InteractiveObject:
    """Objects to interact with"""
    pass

class InteractiveObjectImplA:
    """Implementation class A"""
    pass

class InteractiveObjectImplB:
    """Implementation class B"""
    pass

class Meditor:
    """Intermediary"""

    def __init__(self):
        self.__interactiveObjA = InteractiveObjectImplA()
        self.__interactiveObjB = InteractiveObjectImplB()

    def interative(self):
        """Interactive operation"""
        # Complete the corresponding interactive operations through self .__ interactiveObjA and self .__ interactiveObjB
        pass


# Framework-based implementation
#==============================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法
from enum import Enum
# Enum enum syntax is supported after Python 3.4

class DeviceType(Enum):
    "Equipment type"
    TypeSpeaker = 1
    TypeMicrophone = 2
    TypeCamera = 3

class DeviceItem:
    """Equipment item"""

    def __init__(self, id, name, type, isDefault = False):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__isDefault = isDefault

    def __str__(self):
        return "type:" + str(self.__type) + " id:" + str(self.__id) \
               + " name:" + str(self.__name) + " isDefault:" + str(self.__isDefault)

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def isDefault(self):
        return self.__isDefault


class DeviceList:
    """Device List"""

    def __init__(self):
        self.__devices = []

    def add(self, deviceItem):
        self.__devices.append(deviceItem)

    def getCount(self):
        return len(self.__devices)

    def getByIdx(self, idx):
        if idx < 0 or idx >= self.getCount():
            return None
        return self.__devices[idx]

    def getById(self, id):
        for item in self.__devices:
            if( item.getId() == id):
                return item
        return None

class DeviceMgr(metaclass=ABCMeta):

    @abstractmethod
    def enumerate(self):
        """Enumerating the device list
         (When the program is initialized, the device list must be re-obtained when there is a device plug-in)"""
        pass

    @abstractmethod
    def active(self, deviceId):
        """Select the device you want to use"""
        pass

    @abstractmethod
    def getCurDeviceId(self):
        """Get the design ID currently in use"""
        pass


class SpeakerMgr(DeviceMgr):
    """Speaker device management class"""

    def __init__(self):
        self.__curDeviceId = None

    def enumerate(self):
        """Enumerating the device list
         (The real project should read the device information through the driver, here only the initialization is used to simulate)"""
        devices = DeviceList()
        devices.add(DeviceItem("369dd760-893b-4fe0-89b1-671eca0f0224", "Realtek High Definition Audio", DeviceType.TypeSpeaker))
        devices.add(DeviceItem("59357639-6a43-4b79-8184-f79aed9a0dfc", "NVIDIA High Definition Audio", DeviceType.TypeSpeaker, True))
        return devices

    def active(self, deviceId):
        """Activate the specified device as the current device"""
        self.__curDeviceId = deviceId

    def getCurDeviceId(self):
        return self.__curDeviceId


class DeviceUtil:
    """Equipment tools"""

    def __init__(self):
        self.__mgrs = {}
        self.__mgrs[DeviceType.TypeSpeaker] = SpeakerMgr()
        # 为节省篇幅，MicrophoneMgr和CameraMgr不再实现
        # self.__microphoneMgr = MicrophoneMgr()
        # self.__cameraMgr = CameraMgr

    def __getDeviceMgr(self, type):
        return self.__mgrs[type]

    def getDeviceList(self, type):
        return self.__getDeviceMgr(type).enumerate()

    def active(self, type, deviceId):
        self.__getDeviceMgr(type).active(deviceId)

    def getCurDeviceId(self, type):
        return self.__getDeviceMgr(type).getCurDeviceId()


# Test
#=======================================================================================================================

def Renting():
    myHome = HousingAgency("I love my home")
    zhangsan = HouseOwner("Zhang San");
    zhangsan.setHouseInfo("Upper Sicily", 20, 2500, 1, "individual washroom", 0)
    zhangsan.publishHouseInfo(myHome)
    lisi = HouseOwner("Li Si")
    lisi.setHouseInfo("Contemporary Urban Home", 16, 1800, 1, "Public toilet", 0)
    lisi.publishHouseInfo(myHome)
    wangwu = HouseOwner("Wang Wu")
    wangwu.setHouseInfo("Golden Beauty Garden", 18, 2600, 1, "独立卫生间", 1)
    wangwu.publishHouseInfo(myHome)
    print()

    myHome.signContracts(3)
    print()

    tony = Customer("Tony")
    houseInfos = tony.findHouse("About 18 square meters, you need to have independent guards and windows. It is best to face south. A kitchen is better! Price around 2000", myHome)
    print()
    print("Looking around, looking for the most suitable nest ...")
    print()
    AppropriateHouse = tony.seeHouse(houseInfos)
    tony.signContract(AppropriateHouse, myHome, 1)


def Devices():
    deviceUtil = DeviceUtil()
    deviceList = deviceUtil.getDeviceList(DeviceType.TypeSpeaker)
    print("Microphone device list：")
    if deviceList.getCount() > 0:
        # Set the first device to be used
        deviceUtil.active(DeviceType.TypeSpeaker, deviceList.getByIdx(0).getId())
    for idx in range(0, deviceList.getCount()):
        device = deviceList.getByIdx(idx)
        print(device)
    print("Equipment currently in use:"
          + deviceList.getById(deviceUtil.getCurDeviceId(DeviceType.TypeSpeaker)).getName())


# testRenting()
Devices()
