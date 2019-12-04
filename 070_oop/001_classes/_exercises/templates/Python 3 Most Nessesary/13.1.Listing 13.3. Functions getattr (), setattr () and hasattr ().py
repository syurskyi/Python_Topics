# -*- coding: utf-8 -*-

class MyClass:
    def __init__(self):
        self.x = 10
    def get_x(self):
        return self.x
c = MyClass()                  # Создаем экземпляр класса
print(getattr(c, "x"))         # Выведет: 10
print(getattr(c, "get_x")())   # Выведет: 10
print(getattr(c, "y", 0))      # Выведет: 0, т. к. атрибут не найден
setattr(c, "y", 20)            # Создаем атрибут y
print(getattr(c, "y", 0))      # Выведет: 20
delattr(c, "y")                # Удаляем атрибут y
print(getattr(c, "y", 0))      # Выведет: 0, т. к. атрибут не найден
print(hasattr(c, "x"))         # Выведет: True
print(hasattr(c, "y"))         # Выведет: False