# Создаем пустой кортеж

# Преобразуем строку в кортеж

# Преобразуем список в кортеж

# Создаем пустой кортеж

# Создаем кортеж из одного элемента

# Кортеж из трех элементов

# Получаем значение первого элемента кортежа
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Изменяем порядок следования элементов
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Получаем срез
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Проверка на вхождение
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Повторение

# Конкатенация

# Изменить элемент по индексу нельзя!
t = (1, 2, 3)

# Получаем количество элементов
t = (1, 2, 3)

# Ищем элементы в кортеже
t = (1, 2, 1, 2, 1)

# Make a list from a tuple's items
T = ('cc', 'aa', 'dd', 'bb')

# Sort the list
T = ('cc', 'aa', 'dd', 'bb')

# Make a tuple from the list's items
T = ('cc', 'aa', 'dd', 'bb')

# Create tuple
# But the parentheses are not what indicate a tuple - it is the commas:

#  'extend' tuples
# creating a new tuple
a = 1, 2, 3

# represent a city using a tuple
# We can even have a list of these tuples:
# We can obtain a list of all the cities in the list using a simple list comprehension
# We could even calculate the total population of all these cities.
london = 'London', 'UK', 8_780_000
new_york = 'New York', 'USA', 8_500_000
beijing = 'Beijing', 'China', 21_000_000

cities = london, new_york, beijing

city_names = None
total = 0

# unpacking to extract values from the tuple:
new_york = 'New York', 'USA', 8_500_000
city, country, population = None

# create a Point named tuple that will contain an x-coordinate and a y-coordinate.
from collections import namedtuple

Point2D = None
Pt =None

# There are a number of ways we can specify the field names for the named tuple:
#
# we can provide a sequence of strings containing each property name
# we can provide a single string with property names separated by whitespace or a comma

Circle = None
circle_1 = None
circle_2 = None

# Second option

City = None
new_york = None

# Accessing Items in a Named Tuple
Point2D = None
Pt = None

# We can also choose to let the namedtuple function replace invalid field names automatically for us,
# by using the keyword argument rename

Person = None
eric = None

# Named Tuples - Application - Returning Multiple Values

from random import randint, random

def random_color():
    pass

print(random_color())
red, green, blue, alpha = None
print()

# ## But it might be nicer to use a named tuple: ###

from collections import namedtuple
Color = None

def random_color():
    return None

color = None

