# # -*- coding: utf-8 -*-

# # Во время отладки, в трассировочную информацию выводится __name__ функции.
# ___ foo
#     print foo
#
#
# print ?. -n
#
# # выведет: foo
#
# # Однако, декораторы мешают нормальному ходу дел:
# ___ bar func
#     ___ wrapper
#         print  bar
#         r_ ?
#
#     r_ ?
#
#
# ??
# ___ foo
#     print foo
#
#
# print ?. -n
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
#     ??.? ?
#     ___ wrapper
#         print bar
#         r__ ?
#
#     r_ ?
#
#
# ??
# ___ foo
#     print ?
#
#
# print ?. -n
# # выведет: foo
