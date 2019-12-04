# -*- coding: utf-8 -*-

# Все члены класса в терминологии Python называются атрибутами


# Объявление класса MyClass с двумя атрибутами int_field
# и str_field. Атрибуты класса, являющиеся переменными,
# примерно соответствуют статическим полям класса в других
# языках программирования
class MyClass:
    int_field = 8
    str_field = 'a string'


# Обращение к атрибутам класса
print(MyClass.int_field)
print(MyClass.str_field)

# Создание двух экземпляров класса
object1 = MyClass()
object2 = MyClass()

# Обращение к атрибутам класса через его экземпляры
print(object1.int_field)
print(object2.str_field)

# Все вышеперечисленные обращения к атрибутам на самом деле относятся
# ко двум одним и тем же переменным

# Изменение значения атрибута класса
MyClass.int_field = 10
print(MyClass.int_field)
print(object1.int_field)
print(object2.int_field)

# Однако, аналогично глобальным и локальным переменным,
# присвоение значение атрибуту объекта не изменяет значение
# атрибута класса, а ведёт к созданию атрибута данных
# (нестатического поля)
object1.str_field = 'another string'
print(MyClass.str_field)
print(object1.str_field)
print(object2.str_field)