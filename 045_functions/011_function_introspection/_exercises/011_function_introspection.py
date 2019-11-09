# An example of using function generators

# ___ func x y
#     f_ i i_ r_ 1 x+1
#         y_ i ** y
# f_ n i_ f_ 10 2
#     print n e_=" "    # Выведет: 1 4 9 16 25 36 49 64 81 100
# print()                  # Вставляем пустую строку
# f_ n i_ f_ 10 3
#     print n e_=" "    # Выведет: 1 8 27 64 125 216 343 512 729 1000
#
# print()
# ######################################################################################################################
#  Using the __next __ () parameter

# ___ func x y
#     ___ i i_ r_ 1 x + 1
#         y_ i ** y
#
# i = f_ 3 3
# print(i.__n_  # Выведет: 1 (1 ** 3)
# print(i.__n_  # Выведет: 8 (2 ** 3)
# print(i.__n_  # Выведет: 27 (3 ** 3)
# print(i.__n_  # Исключение StopIteration
#
# print()
# ######################################################################################################################
#  Calling one generator function fro… (simple case)

# ___ gen l
#     ___ e __ l
#         y_ f_ r_ 1 e + 1
#
# l = [5, 10]
# ___ i __ g_([5, 10]): print i e_ - " ")
#
# print()
# ######################################################################################################################
# Calling one function generator fro…er (hard case)

# ___ gen2 n
#     ___ e __ r_ 1 n + 1
#         y_ e * 2
#
# ___ gen l
#     ___ e __ l
#         y_ f_ gen2(e)
#
# l = [5, 10]
# ___ i __ g_([5, 10]): print i e_ - " "
#
# print()