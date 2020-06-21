"""
Большинство последовательностей поддерживают операции
проверки вхождения элемента in и not in.

Для поддержки данной операции необходимо реализовать
специальный метод __contains__
"""

# Список
my_list = [1, 3, 5, 7]
print(3 in my_list)
print(9 in my_list)
print(18 not in my_list)

print()


# Диапазон
my_range = range(2, 10)
print(3 in my_range)
print(5 not in my_range)

print()


# Для строк эта операция проверяет вхождение подстроки
print('ips' in 'Lorem ipsum dolor sit amet.')

print()


# Реализация поддержки операции
class Container(object):
    def __contains__(self, element):
        return element == 3


container = Container()
print(3 in container)
print(5 in container)
