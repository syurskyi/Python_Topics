# # -*- coding: utf-8 -*-
#
# r = ra..(1, 10)
# ___ i __ r
#     print ? e.. _ " "
# # 1 2 3 4 5 6 7 8 9
# r = ra..(10, 110, 10)
# ___ i __ r
#     print ? e.. _ " "
# # 10 20 30 40 50 60 70 80 90 100
# r = ra..10, 1, -1
# ___ i __ r
#     print ? e.. _ " "
# # 10 9 8 7 6 5 4 3 2
#
#
# print(li.. ra.. 1, 10           # Преобразуем в список
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(tu.. ra.. 1, 10           # Преобразуем в кортеж
# # (1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(se. ra.. 1, 10            # Преобразуем в множество
# # {1, 2, 3, 4, 5, 6, 7, 8, 9}
#
#
# r = ra.. 1, 10
# print ? 2 ? -1
# # (3, 9)
# print ? 2 4
# # range(3, 5)
# print(2 __ r, 12 __ r)
# # (True, False)
# print(3 not __ r, 13 not __ r)
# # (False, True)
# print(len(r), min(r), max(r))
# # (9, 1, 9)
# print(r.index(4), r.count(4))
# # (3, 1)
#
# print(ra..(1, 10) == ra..(1, 10, 1))
# # True
# print(ra..(1, 10, 2) == ra..(1, 11, 2))
# # True
# print(ra..(1, 10, 2) == ra..(1, 12, 2))
# # False
#
#
# print(ra..(1, 10, 2) != ra..(1, 12, 2))
# # True
# print(ra..(1, 10) != ra..(1, 10, 1))
# # False
#
# r = ra..(1, 10)
# print(r.start, r.stop, r.step)
# (1, 10, 1)