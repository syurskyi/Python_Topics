# # -*- coding: utf-8 -*-
#
# _______ __
#
# # Чтобы внутри шаблона обратиться к именованным фрагментам, используется следующий
# # синтаксис: (?P=name).
#
# s _ "<b>Text1</b>Text2<I>Text3</I>"
# p _ __.c.. _ < 1_? tag a-z ? > .2? _ </ 1_? _ ?|> __.3? 4? __.5?    # 1. обратиться к именованным фрагментам | 2. One or more occurrences |
#                                                                     # 3. Makes a period (dot) match any character, including a newline. |
#                                                                     # 4. Either or |5. Performs case-insensitive matching.
# ?.f.. ?
# # [('b', 'Text1'), ('I', 'Text3')]
#
# # Кроме того, внугри круглых скобок могут быть расположены следующие конструкции:
# # + (?aiLmsux) - позволяет установить опции регулярного выражения. Буквы а, i, L, rn, s, и
# # и х имеют такое же назначение, что и одноименные модификаторы в функции
# # compile ();
# # {?# ... ) - комментарий. Текст внутри круглых скобок игнорируется;
# # + (?= ... ) - положительный просмотр вперед. Выведем все слова, после которых расположена запятая:
#
# s _ "text1, text2, text3 text4"
# p _ __.c.. _ 1? 2?  |3? , )", __.4? 5? __.6?  # 1. Matches word characters. | 2. One or more occurrences |
#                                               # 3. Matches if ... matches next, but doesn’t consume any of the string. This is called a lookahead assertion.
#                                               # 4. Makes a period (dot) match any character, including a newline. | 5. Either or |6. Performs case-insensitive matching.
# ?.f.. >
# # ['text1', 'text2']
#
# # {?! ... ) - отрицательный просмотр вперед. Выведем все слова, после которых нет запятой:
#
# s _ "text1, text2, text3 text4"
# p _ __.c.. _ a-z 1? 0-9 2? , )", __.3? 4? __.5?    # 1. One or more occurrences
#                                                    # 2. Matches if ... doesn’t match next. This is a negative lookahead assertion.
#                                                    # 3. Makes a period (dot) match any character, including a newline. | 4. Either or |5. Performs case-insensitive matching.
# ?.f.. ?
# # ['text3', 'text4']
#
# # (?<= ...) - положительный просмотр назад. Выведем все слова, перед которыми расположена запятая с пробелом:
#
# s _ "text1, text2, text3 text4"
# p _ __.c.. _ |1? , | | a-z 2? 0-9 __.3? 4? __.5?      # 1. Matches if the current position in the string is preceded by a match for ... that ends at the current position. This is called a positive lookbehind assertion
#                                                       # 2. 2. One or more occurrences
#                                                       # 3. Makes a period (dot) match any character, including a newline. |
#                                                       # 4. Either or |5. Performs case-insensitive matching.
# ?.f..
# # ['text2', 'text3']
#
# # { ?< ! ... ) - отрицательный просмотр назад. Выведем все слова, перед которыми расположен пробел, но перед пробелом нет запятой:
#
# s _ "text1, text2, text3 text4"
# p _ __.c.. _ |1? , a-z 2? 0-9 __.3? 4? __.5?         # 1. Matches if the current position in the string is preceded by a match for ... that ends at the current position. This is called a positive lookbehind assertion.
#                                                      # 2. One or more occurrences
#                                                      # 3. Makes a period (dot) match any character, including a newline. |
#                                                      # 4. Either or |5. Performs case-insensitive matching.
# ?.f.. ?
# # ['text4']
#
# # (? ( id или name) шаблон! 1 шаблон2 J - если группа с номером или названием найдена, то
# # должно выполняться условие из параметра шаблонl, в противном случае должно выполняться условие из параметра шаблон2.
# # Выведем все слова. которые расположены внутри
# # апострофов. Если перед словом нет апострофа, то в конце слова должна быть запятая:
#
# s _ "text1 'text2' 'text3 text4, text5"
# p _ __.c.. _ |' 1_ | a-z 2? 0-9 |1_|1| '3?,)", __.4? 3? __.5?        # 1. Will try to match with yes-pattern if the group with given id or name exist
#                                                                      # 2. One or more occurrences
#                                                                      # 3.  Either or
#                                                                      # 4. Makes a period (dot) match any character, including a newline.
#                                                                      # 5. Performs case-insensitive matching.
# ?.f.. ?
# # [("'", 'text2'), ('', 'text4')]
#
# # Рассмотрим небольшой пример. Предположим, необходимо получить все слова, расположенные после дефиса,
# # причем перед дефисом и после слов должны следовать пробельные символы:
#
# s _ "-word1 -word2 -word3 -word4 -word5"
# __.f.. _ \s\-([a-z0-9]+)\s", s, __.? ? __.?
# # ['word2', 'word4']
#
# # Как видно из примера, мы ПОЛyчили только два слова вместо пяти. Первое и последнее слова не попали в результат.
# # т. к. расположены в начале и в конце строки. Чтобы эти слова попали в результат. необхо.!IИ.\10 .::юбавить
# # альтернативный выбор (, 1 \s: - для начала строки и ( \s 1 $ J - ШIЯ конца строки. Чтобы найденные выражения внутри
# # круглых скобок не попали в результат. следует лобавить символы ? : после открываюшей скобки:
#
# __.f.. _ |?:^|\s)\-([a-z0-9]+)(?:\s|$)", s, __.? ? __.?
# # ['word1', 'word3', 'word5']
#
# # Первое и последнее слова успешно попали в результат. Почему же слова word2 и word4 не
# # попали в список совпадений - ведь перед дефисом есть пробел и после слова есть пробел?
# # Чтобы понять причину, рассмотрим поиск по шагам. Первое слово успешно попадает в результат, т. к. перед дефисом
# # расположено начало строки, и после слова есть пробел. После
# # поиска указатель перемещается, и строка для дальнейшего поиска примет следующий вид:
# # "-wordl <Указатель>-wоrd2 -wordЗ -word4 -word5"
# # Обратите внимание на то, что перед фрагментом -word2 больше нет пробела, и дефис не
# # расположен в начале строки. Поэтому следующим совпадением будет слово wordЗ, и указатель снова будет перемещен:
# # "-wordl -word2 -wordЗ <Указатель>-wоrd4 -word5"
# # Опять перед фрагментом -word4 нет пробела, и дефис не расположен в начале строки. Поэтому следующим совпадением будет
# # слово word5, и поиск будет завершен. Таким образом,
# # слова word2 и word4 не попадают в результат, поскольку пробел до фрагмента уже был использован в предыдущем поиске.
# # Чтобы этого избежать, следует воспользоваться положительным просмотром вперед ( ?= •.. ) :
#
# __.f.. _ |?:^|\s)\-([a-z0-9]+)(?_\s|$)", s, __.? ? __.?
# # ['word1', 'word2', 'word3', 'word4', 'word5']
