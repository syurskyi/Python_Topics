# -*- coding: utf-8 -*-

# ___ a_decorator_passing_arbitrary_arguments function_to_decorate
#     # Данная "обёртка" принимает любые аргументы
# ___ a_wrapper_accepting_arbitrary_arguments $ $$
#         print Передали ли мне что-нибудь?:
#         print a_
#         print k__
#         # Теперь мы распакуем *args и **kwargs
#         # Если вы не слишком хорошо знакомы с распаковкой, можете прочесть следующую статью:
#         # http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
#         ? $ $$
#
#     r_ ?
#
#
# ??
# ___ function_with_no_argument
#     print Python is cool, no argument here. # оставлено без перевода, хорошая игра слов:)
#
#
# ?
#
#
# # выведет:
# # Передали ли мне что-нибудь?:
# # ()
# # {}
# # Python is cool, no argument here.
#
# ??
# ___ function_with_arguments a b c
#     print a b c
#
#
# ? 1 2 3
#
#
# # выведет:
# # Передали ли мне что-нибудь?:
# # (1, 2, 3)
# # {}
# # 1 2 3
#
# ??
# ___ function_with_named_arguments a b c platypus _ Почему нет?
#     print Любят ли @, @ и @ утконосов? @*  |a b c pl....   # string
#
#
# ? Билл Линус Стив platypus_Определенно!
#
#
# # выведет:
# # Передали ли мне что-нибудь?:
# # ('Билл', 'Линус', 'Стив')
# # {'platypus': 'Определенно!'}
# # Любят ли Билл, Линус и Стив утконосов? Определенно!
#
# c___ Mary o___
#     ___ - ____
#         ____.age _ 31
#
#     ??
#     ___ sayYourAge ____ lie_-3  # Теперь мы можем указать значение по умолчанию
#         print Мне @, а ты бы сколько дал?* |_____.a.. + lie    # stirng
#
#
# m = ?
# m.s..
# # выведет:
# # Передали ли мне что-нибудь?:
# # (<__main__ .Mary object at 0xb7d303ac>,)
# # {}
# # Мне 28, а ты бы сколько дал?
