# -*- coding: utf-8 -*-

class MyClass:
    def __init__(self, x):
        self.__privateVar = x
    def set_var(self, x):         # Изменение значения
        self.__privateVar = x
    def get_var(self):            # Получение значения
        return self.__privateVar
c = MyClass(10)                   # Создаем экземпляр класса
print(c.get_var())                # Выведет: 10
c.set_var(20)                     # Изменяем значение
print(c.get_var())                # Выведет: 20
try:                              # Перехватываем ошибки
    print(c.__privateVar)         # Ошибка!!!
except AttributeError as msg:
    print(msg)                    # Выведет: 'MyClass' object has
                                  # no attribute '__privateVar'
c._MyClass__privateVar = 50       # Значение псевдочастных атрибутов
                                  # все равно можно изменить
print(c.get_var())                # Выведет: 50
