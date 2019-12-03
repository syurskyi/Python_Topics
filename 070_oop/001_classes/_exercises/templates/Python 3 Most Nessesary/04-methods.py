# -*- coding: utf-8 -*-

# Атрибутами класса могут быть и функции


# Класс, описывающий человека
class Person:
    # Первый аргумент, который указывает на текущий экземпляр класса,
    # принято называть self
    def print_info(self):
        print(self.name, 'is', self.age)


# Создание экземпляров класса

alex = Person()
alex.name = 'Alex'
alex.age = 18

john = Person()
john.name = 'John'
john.age = 20

# Проверим, чем является атрибут print_info класса Person
print(type(Person.print_info))  # функция (<class 'function'>)

# Вызовем её для объектов alex и john
Person.print_info(alex)
Person.print_info(john)

# Метод -- это функция, привязанная к объекту. Все атрибуты класса,
# являющиеся функциями, описывают соответствующие методы экземпляров
# данного класса.

print(type(alex.print_info))  # метод (<class 'method'>)

# Вызов метода print_info
alex.print_info()
john.print_info()