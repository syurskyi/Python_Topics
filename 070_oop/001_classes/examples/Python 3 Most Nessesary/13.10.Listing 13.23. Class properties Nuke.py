# -*- coding: utf-8 -*-

class MyClass:
    def __init__(self, value):
        self.__var = value
    def get_var(self):        # Чтение
        return self.__var
    def set_var(self, value): # Запись
        self.__var = value
    def del_var(self):        # Удаление
        del self.__var
    v = property(get_var, set_var, del_var, "Строка документирования")
c = MyClass(5)
c.v = 35                    # Вызывается метод set_var()
print(c.v)                  # Вызывается метод get_var()
del c.v                     # Вызывается метод del_var()