# # -*- coding: utf-8 -*-
#
# # Фрагментам внутри круглых скобок можно дать имена. Для этого после открывающей
# # круглой скобки следует указать комбинацию символов ?P<name>
# _______ __
#
# email _ "test@mail.ru"
# p _ __.c.. _""" 1_? ? a-z0-9_.-| 2? |  #  1.Название ящика - Group names | 2.One or more occurrences
#         @                                     # Символ "@"
#         1_? 2?host? _: a-z0-9-| 3? 4?. 5? a-z 6?2,6 #  1.Group names | 2.Домен |3.One or more occurrences
#                                                     #  4.ekranirovat' . | 5.One or more occurrences
#                                                     #  6.Causes the resulting RE to match from m to n repetitions of the preceding RE
#         """, __.? ? __.V..
# r _ ?.s.. e..
# ?.g..  ?                          # Название ящика
# # 'test'
# ?.g.. ?                           # Домен
# # 'mail.ru'
