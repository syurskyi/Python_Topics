# -*- coding: utf-8 -*-

# Примеры некоторых стандартных итерабельных объектов.
# список

my_list = [1, 2, 5, 7, 32, 148]

# Обход списка
for element in my_list:
    print(element)


# Функция enumerate возвращает итерабельный объект, который возвращает пары индекс-значение
for index, element in enumerate(my_list):
    print('my_list[{}] = {}'.format(index, element))


# Примеры некоторых стандартных итерабельных объектов.
# строка

string = 'A string'
# Обход строки посимвольно
for char in string:
    print(char)

# Create my function ,my_for



def my_for(iterable, callback):
    it = iter(iterable)
    while True:
        try:
            value = next(it)
            callback(value)
        except StopIteration:
            break

def loop_body(value):
    print('Next value received:', value)

my_for(range(10), loop_body)

# Примеры некоторых стандартных итерабельных объектов.
#  диапазон

# В Python 3 range -- это итерабельный объект, который задаёт диапазон.
# В Python 2 для этого служит xrange, а range является функцией,
# которая возвращает список.

my_range = range(2, 17, 2)

for counter in my_range:
    print(counter)

# iterable_with_getitem

# Итерабельные объекты должны реализовывать как минимум один из двух методов:
# -  __iter__(self)
# -  __getitem__(self, key)
#
# Метод __iter__ возвращает объект - итератор(будет рассмотрен далее).
# Метод __getitem__ возвращает элемент контейнера по ключу или индексу.
# Встроенная фукнция iter(автоматически вызывается циклом for ) вызывает метод __iter__, если он существует.Иначе, если
# существует метод __getitem__, то автоматически создаётся итератор, который вызывает метод __getitem__ с
# возрастающими индексами, начиная от нуля, до возникновения исключения IndexError.Если объект не реализовавает ни один из
# этих методов, то данный объект не является итерабельным и выбрасывается исключение TypeError.


class SimpleIterable(object):
    """Класс итерабельного объекта с методом __getitem__"""

    def __getitem__(self, index):
        if 0 <= index < 5:
            return index * 2
        else:
            raise IndexError('iterable index out of range')


# Создание объекта
iterable = SimpleIterable()


# Вывод некоторых значений
print('iterable[0] =', iterable[0])
print('iterable[3] =', i)

# list_iterator
# Функция обхода итерабельного объекта

# Итератор (iterator) – это объект, который представляет поток данных.
# Повторяемые вызовы метода __next__() (next() в Python 2) итератора
# или передача его встроенной функции next() возвращает последующие
# элементы потока.
#
# Если больше не осталось данных, выбрасывается исключение StopIteration.
# После этого итератор исчерпан и любые последующие вызовы его метода __next__()
# снова генерируют исключение StopIteration.
#
# Итераторы обязаны иметь метод __iter__, который возвращает сам объект итератора.
# Таким образом, любой итератор сам по себе также является итерабельным объектом.


def traverse(iterable):
    print('Traversing {}:'.format(type(iterable).__name__))
    for element in iterable:
        print(element)
    print()


# Объявление списка
my_list = [1, 2, 3, 5, 8]

# Получение его итератора
list_iterator = iter(my_list)

# Обход списка
traverse(my_list)

# Обход итератора списка
traverse(list_iterator)

# Очередной обход списка -- работает корректно, так как создаётся
# новый объект-итератор
traverse(my_list)

# Очередной обход итератора -- не выводится ничего, так как
# эле
