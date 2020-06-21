# -*- coding: utf-8 -*-
# Реализация с помощью именованных функций:
def make_adder(x):
    def adder(n):
        return x + n # захват переменной "x" из внешнего контекста
    return adder

# То же самое, но через безымянные функции:
make_adder = lambda x: (lambda n: x + n)

f = make_adder(10)
print(f(5)) # 15
print(f(-1)) # 9


def multiplier(n):  # multiplier возвращает функцию умножения на n
    def mul(k):
        return n * k

    return mul


mul3 = multiplier(3)  # mul3 - функция, умножающая на 3
print(mul3(3), mul3(5))

n = 3


def mult(k, mul=n):
    return mul * k


n = 7
print(mult(3))
n = 13
print(mult(5))

n = 10
mult = lambda k, mul=n: mul * k
print(mult(3))


def outer_func(x):
    def inner_func(y):
        # inner_func замкнуло в себе х
        return y + x
    return inner_func