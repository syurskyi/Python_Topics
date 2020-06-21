
# Базовые операции
#  Длина: число элементов
print()
# Базовые операции
# Конкатенация: новая строка
print()
# Базовые операции
# Повторение
print()
#  Индексация от начала или от конца
S = 'spam'
print()
# Операция индексирования (S[i])
S = 'spam'
# S[l...(S)...])


# Операция извлечения подстроки (S[i:j])
S = '123456789'
# # # # извлечь элементы со смещениями от 1 до 3
print()
# # # # извлечь элементы, начиная со смещения 1 и до конца
print()
# # # # извлечь элементы, начиная со смещения 0 и до 3
print()
# # # # извлечь  элементы, начиная со смещения 0 и до последнего это эффективный способ создать
# # # # поверхностную копию последовательности S
print()

# Расширенная операция извлечения подстроки:
# третий предел
S = '123456789'
print()
print()
# Расширенная операция извлечения подстроки:
# третий предел
# отрицательное значение шага.
S = 'hello'
print()
# Инструменты преобразования строк
# # # # # Преобразование из/в строки
print()
print()
# # # # # # Преобразование в строку, как если бы она была  литералом в программном коде
print()
# Преобразование кодов символов

# Изменение строк
S = 'spam'


# Строковые методы:
# replace
# заменить буквы  'mm' на 'xx'
S = 'spammy'

print()
# заменить символ '$' на 'SPAM'
S = 'aacc$dd'

print()
# Заменить все найденные подстроки  (‘SPAM’ на ‘EGGS’
S = 'xxxxSPAMxxxxSPAMxxxx'

print()
# Заменить одну подстроку ‘SPAM’ на ‘EGGS
S = 'xxxxSPAMxxxxSPAMxxxx'

print()
# Строковые методы:
# find
S = 'xxxxSPAMxxxxSPAMxxxx'

print()

print()
# Строковые методы:
# list
S = 'spammy'
print()
# Строковые методы:
# join
S = 'spammy'
L = None
print()
# change index 3

# change index 4

print()

S = None
print()
# Строковые методы:
# split
line = 'bob,hacker,40'
print()
line = 'i’mSPAMaSPAMlumberjack'
print()
# Строковые методы:
# rstrip()
# strip()
line = "The knights who say Ni!\n"
print()
txt = "     banana     "
print()
x = None
print('of all fruits', 'is my favorite')
# Строковые методы:
# upper()
line = "The knights who say Ni!\n"
print()
# Строковые методы:
# isalpha()
line1 = "The knights who say Ni!\n"
line2 = "TheknightswhosayNi"
print()
# Строковые методы:
# endswith()
line = "The knights who say Ni!\n"
print()
# Строковые методы:
# startswith()
line = "The knights who say Ni!\n"


# Check String
# in
txt = "The rain in Spain stays mainly in the plain"
x = None
print()
txt = "The rain in Spain stays mainly in the plain"
x = None
print
# Форматирование строк
# Выражения форматирования строк
print()  # one element
print()  # three element
# Форматирование строк
# Выражения форматирования строк
# <Ключ=>
print('(...) - (...)')
# Formatting Method Basics
# By position
template = None
print()
# Formatting Method Basics
# By keyword
template = None
print()
# Formatting Method Basics
# By position and keyword
template = None
print()
# Formatting Method Basics
# By relative position
template = None
print()
# Formatting Method Basics
# Parameters hardcoded
# print('{.....}'.f.....(1/3.0))

# Formatting Method Basics
# Take value from arguments
# print('{.....}'.f.....(1/3.0, .....))

# Formatting Method Basics
# String method
# print('{.....}'.f.....(1.23456789))

# Formatting Method Basics
# Built-in function

# Flexible reference syntax Extra complexity and functional overlap

# # # # print('{n...} {j...} {n..}'.f...(n...='Bob', j..='dev'))

# # # # print('..(n...)... %(j...)... %(n....)...' % d...(n...='Bob', j...='dev'))

# # # # D = d...(n...='Bob', j...='dev')

# # # # print('{0[n]...} {0[j...]} {0[n...]}'.f......(D))
# # # # Method, key references


# # # # print('{n....} {j...} {n...}'.f.....(**D))
# # # # Method, dict-to-args

# # # # print('%(n....)s %(j...)s %(n....)s' % D)
# # # # Expression, key references


# Format () method - Индексы

# # # # print("{...} — {....} — {...}".f....(10, 12.3, "string"))

# # # # arr = [10, 12.3, "string"]

# # # # print("{....} — {....} — {....}".format(....))

# # # # arr = [10, [12.3, "string"]]

# # # # print("{...[...]} — {....[....][...]} — {...[...][...]}".f.....(....))

# # # # print("{...[...]} — {...[...][...]}".f.....(....=....))

# # # # Format () method - Ключи

# # # #  print("{m....} — {c....}".f.....(c....="red", m....="BMW"))

# # # # d = {"c....": "red", "m.....": "BMW"}
# # # # print("{m....} — {c....}".f....(.....))                   # Ключи


# Format () method -Индексы и Ключи
# # # # print("{c....} — {.....}".f.....(2015, c.....="red"))


# Параметр <Функция> задает функцию, с помощью которой обрабатываются данные перед вставкой в строку.

# # # # print("{....}".f....("строка"))
# # # # # # str()

# # # # print("{....}".f.....("строка"))
# # # # # # repr()

# # # # print("{...}".f....("строка"))
# # # # # # ascii()

# strip( [<Символы>])
s1, s2 = "     str\n\r\v\t"

# lstrip ( [ <Символы> ])
s1, s2 = "     str     ", "strstrstrokstrstrstr"

# rstrip ( [<Символы>] )
s1, s2 = "     str     ", "strstrstrokstrstrstr"

# splitlines ( [True ] )
w = "word1\nword2\nword3"

# partition (<Разделитель>)
string = "Python is fun"

string = "Python is fun, isn't it"

# join()

# Изменение регистра символов
# upper ()

# Изменение регистра символов
# lower ()

# Изменение регистра символов
# swapcase ()

# Изменение регистра символов
# capitalize ()

# Изменение регистра символов
# title ()
s = "the first letter of each words will be capitilize"

# Поиск и замена в строке
# find()
s = 'exapmle example Example'

# Поиск и замена в строке
# index ( )
s = 'exapmle example Example Example'

# Поиск и замена в строке
# count ()
s = 'exapmle example Example Example'

# Поиск и замена в строке
# startswith ( )
s = 'exapmle example Example Example'

s = 'exapmle example Example Example'

# Поиск и замена в строке
# endswith ()
s = 'substring SUBSTRING'

s = 'substring SUBSTRING'

# Поиск и замена в строке
# replace( )
s = 'Hi Maksym!'

s = "strstrstrstrstr"

# Проверка типа содержимого строки
# isalnum()


# Проверка типа содержимого строк
# isalpha ()

# Проверка типа содержимого строк
# isdigit ( )

# Проверка типа содержимого строк
# isdecimal ()

# Проверка типа содержимого строк
# isnumeric ()

# Проверка типа содержимого строк
# isupper ()

# Проверка типа содержимого строк
# islower ()

# Проверка типа содержимого строк
# istitie ()


# Проверка типа содержимого строк
# isprintable()

# Проверка типа содержимого строк
# isidentifier ()


# Проверка типа содержимого строк
# isspace()


# Тип данных bytes
# b = ....('....', 'cp1251')
b = None  # b...

# # # #  Обращение по индексу

# # # #  Получение среза

# # # #  Конкатенация

# # # #  Повторение

# Как видно из примера, при выводе объекта целиком, а также при извлечении среза,
# производится попытка отображения символов. Однако доступ по индексу возвращ ает целое число, а не символ.
# Если преобразовать объект в список, то мы получим последовательность целых чисел:
# l...(b...('....', 'cp1251'))

# При использовании методов следует учитывать, что в параметрах нужно указывать объекты типа bytes, а не строки:

b = bytes("string", "cp1251")
# b.r....(...'s', b'S'))

# Создать объект типа bytearray можно


# Создать объект типа bytearray можно с помощью функции bytearray (<После.nовательность>),
# которая преобразует последовательность
# целых чисел от о до 255 в объект типа bytearтa'/. Если число не попадает в диапазон, то возбуждается
# исключение ValueError.
b = bytearray([225, 226, 224, 174, 170, 160])

# Создать объект типа bytearray можно с помощью функции bytearray (<Число>),
# которая задает количество элементов в последовательности. Каждый элемент будет содержать нулевой символ:

# The syntax is similar to the one you used with str.format() but less verbose.
# It would also be valid to use a capital letter F:
name = "Eric"
age = 74

# Arbitrary Expressions
# Because f-strings are evaluated at runtime, you can put any and all valid Python expressions in them.

# Arbitrary Expressions
# you could also call functions.
#


def to_lowercase():
    pass

name = "Eric idle"


# You also have the option of calling a method directly:
name = "Eric Idle"


# Multiline f-strings
name = "Eric"
profession = "comedian"
affiliation = "Monty Python"

message = None

# Speaking of quotation marks, watch out when you are working with dictionaries.
# If you are going to use single quotation marks for the keys of the dictionary,
# then remember to make sure you’re using double quotation marks for the f-strings containing the keys.
comedian = {'name': 'Eric Idle', 'age': 74}

# Imagine you had the following greet() function that contains an f-string:

def greet():
    return