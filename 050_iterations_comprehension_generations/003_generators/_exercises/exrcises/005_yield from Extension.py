# # -*- coding: utf-8 -*-

# В Python 3 существуют так называемые подгенераторы (subgenerators).
# Если в функции-генераторе встречается пара ключевых слов yield from,
# после которых следует объект-генератор, то данный генератор делегирует
# доступ к подгенератору, пока он не завершится (не закончатся его значения),
# после чего продолжает своё исполнение.

# # The Python 3.3  yield from Extension
# # def both (N )

# i, x
def both(N):
    for i in range(N):   yield  i
    for i in (x ** 2 for x in range(N)):   yield i


print(both(5))
print(list(both(5)))


def both(N):
     yield from range(N)
     yield from (x ** 2 for x in range(N))

print()
print()

print(list(both(5)))

# i
print(' : '.join(str(i) for i in both(5)))
