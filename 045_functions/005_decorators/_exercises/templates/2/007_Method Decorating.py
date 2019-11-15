# -*- coding: utf-8 -*-

# ___ a_decorator_passing_arbitrary_arguments function_to_decorate
#     # Данная "обёртка" принимает любые аргументы
# ___ a_wrapper_accepting_arbitrary_arguments 0a__ 00k__
#         print Передали ли мне что-нибудь?:
#         print a_
#         print k__
#         # Теперь мы распакуем *args и **kwargs
#         # Если вы не слишком хорошо знакомы с распаковкой, можете прочесть следующую статью:
#         # http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
#         function_to_decorate 0a__ 00k__
#
#     r_ a_w00_a00_a000_a000
#
#
# 0a_000
# ___ function_with_no_argument
#     print Python is cool, no argument here. # оставлено без перевода, хорошая игра слов:)
#
#
# f000_w00_n0
#
#
# # выведет:
# # Передали ли мне что-нибудь?:
# # ()
# # {}
# # Python is cool, no argument here.
#
# 0a_000
# ___ function_with_arguments a b c
#     print a b c
#
#
# f000_w00_ar000 1 2 3
#
#
# # выведет:
# # Передали ли мне что-нибудь?:
# # (1, 2, 3)
# # {}
# # 1 2 3
#
# 0a_00
# ___ function_with_named_arguments a b c platypus _ Почему нет?
#     print Любят ли /s, /s и /s утконосов? /s* / |a b c platypus||
#
#
# f000 Билл Линус Стив platypus_Определенно!
#
#
# # выведет:
# # Передали ли мне что-нибудь?:
# # ('Билл', 'Линус', 'Стив')
# # {'platypus': 'Определенно!'}
# # Любят ли Билл, Линус и Стив утконосов? Определенно!
#
# c___ Mary o___
#     ___ __i__ ____
#         ____.age _ 31
#
#     a_decorator_passing_arbitrary_arguments
#     ___ sayYourAge ____ lie_-3  # Теперь мы можем указать значение по умолчанию
#         print Мне /s, а ты бы сколько дал?* / |_____.age + lie||
#
#
# m = Mary||
# m.s00Y00A00||
# # выведет:
# # Передали ли мне что-нибудь?:
# # (<__main__ .Mary object at 0xb7d303ac>,)
# # {}
# # Мне 28, а ты бы сколько дал?