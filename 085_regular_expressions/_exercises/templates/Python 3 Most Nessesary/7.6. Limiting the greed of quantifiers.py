# # -*- coding: utf-8 -*-
#
# # Вместо желаемого результата мы получили полностью строку. Чтобы ограничить «жадность», необходимо после квантификатора
# # указать символ ?
# _______ __
#
# s _ "<b>Text1</b>Text2<b>Text3</b>"
# p _ __.c.. _ <b>. 1?2_ </b>" __.3?   # 1.Zero or more occurrences |
#                                      # 2.ограничить жадность -  zero or one occurrence Causes the resulting RE to match 0 or 1 repetitions of the preceding RE. ab? will match either ‘a’ or ‘ab’.
#                                      # 3. Makes a period (dot) match any character, including a newline.
# ?.f.. ?
# # ['<b>Text1</b>', '<b>Text3</b>']
