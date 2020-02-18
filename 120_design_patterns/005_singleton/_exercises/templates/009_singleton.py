##!/usr/bin/python

# Version 1.0
########################################################################################################################

class MyBeautifulGril(object):
    """My pretty goddess"""
    __instance = None
    __isFirstInit = False

    def __new__(cls, name):
        if not cls.__instance:
            MyBeautifulGril.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__isFirstInit:
            self.__name = name
            print("meet" + name + "，I fell in love at first sight！")
            MyBeautifulGril.__isFirstInit = True
        else:
            print("meet" + name + ", I turned a deaf ear")

    def showMyHeart(self):
        print(self.__name + "The only one in my heart！")



#========================================================================================
def singletonDecorator(cls, *args, **kwargs):
    """Define a singleton decorator"""
    instance = {}

    def wrapperSingleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapperSingleton


@singletonDecorator
class Singleton3:
    """Decorate a class with a singleton decorator"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name


# tony = Singleton3("Tony")
# karry = Singleton3("Karry")
# print(tony.getName(), karry.getName())
# print("id(tony):", id(tony), "id(karry):", id(karry))
# print("tony == karry:", tony == karry)


# Version 2.0
########################################################################################################################
@singletonDecorator
class MyBeautifulGril(object):
    """My pretty goddess"""

    def __init__(self, name):
        self.__name = name
        if self.__name == name:
            print("meet" + name + "，I fell in love at first sight！")
        else:
            print("meet" + name + ", I turned a deaf ear")

    def showMyHeart(self):
        print(self.__name + "The only one in my heart! ")


# Test
########################################################################################################################
def TestLove():
    jenny = MyBeautifulGril("Jenny")
    jenny.showMyHeart()
    kimi = MyBeautifulGril("Kimi")
    kimi.showMyHeart()
    print("id(jenny):", id(jenny), " id(kimi):", id(kimi))


TestLove()

