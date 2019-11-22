# -*- coding: utf-8 -*-

# Generators and function application
# Normal positionals
#  Unpack range values: iterable in 3.X
#  Unpack generator expression values

def f(a, b, c): print('%s, %s, and %s' % (a, b, c))

f(0, 1, 2)  # Normal positionals

f(*range(3))  # Unpack range values: iterable in 3.X

f(*(i for i in range(3)))

# Generators and function application
# dict
# Normal keywords
# Unpack dict: key=value
# Unpack keys iterator
# Unpack view iterator: iterable in 3.X

D = dict(a='Bob', b='dev', c=40.5)

print(D)

f(a='Bob', b='dev', c=40.5)  # Normal keywords

f(**D)  # Unpack dict: key=value

f(*D)  # Unpack keys iterator

f(*D.values())

# Generators and function application
# for x in 'spam':

for x in 'spam': print(x.upper(), end=' ')
print()

list(print(x.upper(), end=' ') for x in 'spam')
print()

print(*(x.upper() for x in 'spam'))

# range-generator
def my_range(first, second=None, step=1):
    """Функция-генератор, работающая подобно стандартному классу range"""

    if second is None:
        current = 0
        end = first
    else:
        current = first
        end = second

    if step == 0:
        raise ValueError('step must not be zero')

    while (step > 0 and current < end) or (step < 0 and current > end):
        # yield выдаёт текущее значение и приостанавливает работу генератора.
        # При следующем вызове next выполнение продолжится с этого места.
        yield current
        current += step


# fibonacci-sequence
def fibonacci(max_count):
    """Генерация max_count чисел Фибоначчи"""
    count = 0
    first, second = 0, 1

    while count < max_count:
        count += 1
        yield second
        first, second = second, first + second


def main():
    # Вывод 15 первых чисел Фибоначчи
    for number in fibonacci(15):
        print(number)


if __name__ == '__main__':
    main()
