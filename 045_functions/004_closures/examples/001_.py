# -*- coding: utf-8 -*-

# В питоне циклы не создают область видимости, что делает создание замыканий несколько нетривиальным.
#
# Простой пример: в массив multipliers мы размещаем функции, которые умножают аргумент на 0, 1, 2, 3, 4

multipliers = []

for m in range(5):
    multipliers.append(lambda x: x * m)

print([multipliers[i](5) for i in range(5)])

# На самом деле, все функции будут умножать аргумент на 4, на выходе мы получим [20, 20, 20, 20, 20].
# Чтобы получить правильные замыкания, гайды рекомендуют делать так:

multipliers = []

for m in range(5):
    multipliers.append(lambda x, real_m=m: x * real_m)

print([multipliers[i](5) for i in range(5)])

# В этом случае m биндится сразу, т. к. находится не в теле функции. Если вам кажется, что это похоже на хак,
# то вы правы. Такой подход ломает интерфейс функции, оставляя возможность указывать real_m снаружи,
# что достаточно криво. Но все становится еще хуже, если вы хотите вместо x использовать *args.

multipliers = []

for m in range(5):
    multipliers.append(lambda *args: [x * m for x in args])

print([multipliers[i](1, 2, 3) for i in range(5)])

# это синтаксически неверно,
# нельзя ставить параметр после *args
# multipliers.append(lambda *args, real_m=m: [x * real_m for x in args])

# Как еще можно решить эту проблему, не прибегая к хаку с дефолтным значением аргумента? Нужно сделать так,
# чтобы значение m рельно использовалось в цикле, а не просто прокидывалось в тело функции.
# Для этого используем его в качестве аргумента промежуточной функции:
# partial создает функцию-обертку, позволяя задать заранее некоторые дефолтные значения параметров.
# Правда, с partial конкретно в моем случае возникла неожиданная проблема:
# она возвращает вызываемый functools.partial object, но не обычную функцию, что почему-то не устраивает библиотеку,
# с который я работаю.

multipliers = []

for m in range(5):
    def _closure(m):
        return lambda *args: [x * m for x in args]


    multipliers.append(_closure(m))

print([multipliers[i](1, 2, 3) for i in range(5)])

# Более того, функция подобная _closure уже есть в стандартной библиотеке:
from functools import partial

multipliers = []


def mult_array(m, *args):
    return [x*m for x in args]

for m in range(5):
    multipliers.append(partial(mult_array, m))

print([multipliers[i](1, 2, 3) for i in range(5)])