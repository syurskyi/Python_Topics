# -*- coding: utf-8 -*-

# # Во время отладки, в трассировочную информацию выводится __name__ функции.
# ___ foo
#     print foo
#
#
# print f00.__n__
#
# # выведет: foo
#
# # Однако, декораторы мешают нормальному ходу дел:
# ___ bar func
#     ___ wrapper
#         print  bar
#         r_ f00
#
#     r_ w000
#
#
# _b__
# ___ foo
#     print foo
#
#
# print f00.__n__
# # выведет: wrapper
#
# # "functools" может нам с этим помочь
#
# _____ fun__
#
#
# ___ bar func
#     # Объявляем "wrapper" оборачивающим "func"
#     # и запускаем магию:
#     _f00.w00 func
#     ___ wrapper
#         print bar
#         r__ f00
#
#     r_ w00
#
#
# _b00
# ___ foo
#     print foo
#
#
# print f00.__n__
# # выведет: foo