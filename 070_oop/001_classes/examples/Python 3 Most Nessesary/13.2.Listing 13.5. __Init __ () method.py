# -*- coding: utf-8 -*-

class MyClass:
    def __init__(self, value1, value2): # Конструктор
        self.x = value1
        self.y = value2
c = MyClass(100, 300)                   # Создаем экземпляр класса
print(c.x, c.y)                         # Выведет: 100 300