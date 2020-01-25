# # -*- coding: utf-8 -*-
#
# # Круглые скобки часто используются для группировки фрагментов внутри шаблона. В этом
# # случае не требуется, чтобы фрагмент запоминался и бьm доступен в результатах поиска.
# # Чтобы избежать захвата фрагмента, следует после открывающей круглой скобки разместить
# # символы ? :
#
# _______ __
#
# s _ "test text"
# p _ __.c..  _ a-z 1? st 2? xt __.3?   # 1.One or more occurrences | 2.Either or
#                                       # 3.Makes a period (dot) match any character, including a newline.
# ?.f.. ?
# # [('test', 'st', 'st', ''), ('text', 'xt', '', 'xt')]
# p _ __.c.. _ a-z 1? |_: |_:st 2? |_:xt||| __.3?    #  1.One or more occurrences   | 2.Either or
#                                                    #  3.Makes a period (dot) match any character, including a newline.
# ?.f.. ?
# # ['test', 'text']
