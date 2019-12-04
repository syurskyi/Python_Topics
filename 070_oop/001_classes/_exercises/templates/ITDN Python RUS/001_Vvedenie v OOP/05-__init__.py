# -*- coding: utf-8 -*-

# Начальное состояние объекта следует создавать в
# специальном методе-конструкторе __init__, который
# вызывается автоматически после создания экземпляра
# класса. Его параметры указываются при создании
# объекта.


# Класс, описывающий человека
class Person:
    # Конструктор
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Метод из прошлого примера
    def print_info(self):
        print(self.name, 'is', self.age)


# Создание экземпляров класса
alex = Person('Alex', 18)
john = Person('John', 20)

# Вызов метода print_info
alex.print_info()
john.print_info()