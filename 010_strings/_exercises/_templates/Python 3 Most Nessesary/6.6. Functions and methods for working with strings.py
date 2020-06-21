# # -*- coding: utf-8 -*-
#
# print( s.. ,  s.. 1, 2,  s.. 3, 4,  s.. x 1
# # ('', '[1, 2]', '(3, 4)', "{'x': 1}")
# print("строка1\nстрока2")
# # строка1
# # строка2
#
#
# print(r.. Строка", r.. 1, 2, 3, r.. x 5
# # ("'Строка'", '[1, 2, 3]', "{'x': 5}")
# print(r.. строка1\nстрока2
# # "'строка1\\nстрока2'"
#
#
# print(as.. 1, 2, 3, as.. "x" 5
# # ('[1, 2, 3]', "{'x': 5}")
# print(as.. строка
# # "'\\u0441\\u0442\\u0440\\u043e\\u043a\\u0430'"
#
#
# print(le. Python, le. "\r\n\t" le. _"\r\n\t"
# # (6, 3, 6)
# print(le. строка
# # 6
#
#
# s1, s2 = "     str\n\r\v\t", "strstrstrokstrstrstr"
# print("'__' — '__'"  _1.st.., _2.st.."tsr"
# # "'str' — 'ok'"
#
#
# s1, s2 = "     str     ", "strstrstrokstrstrstr"
# print("'__' — '__'"  _1.ls.. _2.ls.."tsr"
# # "'str     ' — 'okstrstrstr'"
#
# s1, s2 = "     str     ", "strstrstrokstrstrstr"
# print("'__' — '__'"  _1.rs.., _2.rs.."tsr"
# # "'     str' — 'strstrstrok'"
#
#
# s = "word1 word2 word3"
# print ?.sp..  ?.sp.. N.. 1
# # (['word1', 'word2', 'word3'], ['word1', 'word2 word3'])
# s = "word1\nword2\nword3"
# print ?.sp.. "\n"
# # ['word1', 'word2', 'word3']
#
#
# s = "word1           word2 word3     "
# print ?.sp..
# # ['word1', 'word2', 'word3']
#
#
# s = ",,word1,,word2,,word3,,"
# print(?.sp.. !
# # ['', '', 'word1', '', 'word2', '', 'word3', '', '']
# print "1,,2,,3".sp.. !
# # ['1', '', '2', '', '3']
#
#
# print("word1 word2 word3".sp.. \n
# # ['word1 word2 word3']
#
#
# s = "word1 word2 word3"
# print ?.rs.. ?.rs.. N.. 1
# # (['word1', 'word2', 'word3'], ['word1 word2', 'word3'])
# print("word1\nword2\nword3".rs.. \n
# # ['word1', 'word2', 'word3']
#
#
# print("word1\nword2\nword3".s.l.
# # ['word1', 'word2', 'word3']
# print("word1\nword2\nword3".s.l. T..
# # ['word1\n', 'word2\n', 'word3']
# print("word1\nword2\nword3".s.l. F..
# # ['word1', 'word2', 'word3']
# print("word1 word2 word3".s.l.
# # ['word1 word2 word3']
#
#
# print("word1 word2 word3".pa.." "
# # ('word1', ' ', 'word2 word3')
# print("word1 word2 word3".pa.. "\n"
# # ('word1 word2 word3', '', '')
#
#
# print("word1 word2 word3".rpa.. " "
# # ('word1 word2', ' ', 'word3')
# print("word1 word2 word3".rpa.."\n"
# # ('', '', 'word1 word2 word3')
#
#
# print(" => ".j.. "word1" "word2" "word3"
# # 'word1 => word2 => word3'
# print(" ".j.. "word1" "word2" "word3"
# # 'word1 word2 word3'
#
#
# # " ".join(("word1", "word2", 5
# # Traceback (most recent call last):
# #   File "<pyshell#48>", line 1, in <module>
# #     " ".join(("word1", "word2", 5))
# # TypeError: sequence item 2: expected str instance, int found
#
#
# s = "Python"
# arr = li.. ?; print ?        # Преобразуем строку в список
# # ['P', 'y', 't', 'h', 'o', 'n']
# ? 0 = "J"; print ?       # Изменяем элемент по индексу
# # ['J', 'y', 't', 'h', 'o', 'n']
# s = "".j.. ?; print ?       # Преобразуем список в строку
# # 'Jython'
#
#
# s = "Python"
# b = b.a. ?  cp1251 ; print ?
# # bytearray(b'Python')
# ? 0 = o.. "J"; print ?
# # bytearray(b'Jython')
# s = ?.de..  cp1251 ; print ?
# # 'Jython'
