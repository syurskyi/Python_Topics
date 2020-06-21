# # -*- coding: utf-8 -*-
#
# #  Этот код вывел то, что мы искали. Если необходимо получить содержимое без тегов, то
# # нужный фрагмент внутри шаблона следует разместить внутри круглых скобок
# _______ __
#
# s _ "<b>Text1</b>Text2<b>Text3</b>"
# p _ __.c.. _ <b> .1?2_ </b> __.3?  # 1.Zero or more occurrences | 2.ограничить жадность -  zero or one occurrence
#                                    # 3.Makes a period (dot) match any character, including a newline.
# ?.f.. ?
# # ['Text1', 'Text3']
