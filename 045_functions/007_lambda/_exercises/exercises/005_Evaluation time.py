# -*- coding: utf-8 -*-

def wrap(n):
    def f():
        print(n)
    return f

numbers = 'one', 'two', 'three'
funcs = []    # list
for n in numbers:
    funcs.append(wrap(n))

for f in funcs:
    f()

# one
# two
# three

# В нормальной функции n вычисляется во время определения, в строке 9, когда функция добавляется в список:
# funcs.append (wrap (n)).
#
# Теперь, при реализации той же логики с лямбда-функцией, наблюдаем неожиданное поведение:

numbers = 'one', 'two', 'three'
funcs = []  # list
for n in numbers:
    funcs.append(lambda: print(n))

for f in funcs:
    f()

# three
# three
# three

# Неожиданный результат возникает из-за того, что свободная переменная n, как она реализована,
# связана во время выполнения лямбда-выражения. Лямбда-функция Python в строке 4 является замыканием,
# которое захватывает n, свободную переменную, ограниченную во время выполнения.
# Во время выполнения при вызове функции f из строки 7 значение n равно three.
#
# Чтобы решить эту проблему, вы можете назначить свободную переменную во время определения следующим образом:

numbers = 'one', 'two', 'three'
funcs = []   # list
for n in numbers:
    funcs.append(lambda n=n: print(n))

for f in funcs:
    f()

# one
# two
# three

# Лямбда ведет себя как нормальная функция в отношении аргументов.
# Следовательно, лямбда-параметр может быть инициализирован значением по умолчанию:
# параметр n принимает значение n по умолчанию для внешнего n. Лямбда может бы быть записана как lambda x=n: print(x)
# и вернуть такой же результат.
#
# Лямбда вызывается без аргумента в строке 7 и использует значение по умолчанию n, установленное во время определения.

