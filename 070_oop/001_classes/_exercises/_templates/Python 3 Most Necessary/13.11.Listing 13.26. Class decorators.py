# -*- coding: utf-8 -*-

def deco(C):                   # Принимает объект класса
    print("Внутри декоратора") # Производит какие-то действия
    return C                   # Возвращает объект класса

@deco
class MyClass:
    def __init__(self, value):
        self.v = value
c = MyClass(5)
print(c.v)