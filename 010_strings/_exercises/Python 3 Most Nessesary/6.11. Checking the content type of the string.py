# # -*- coding: utf-8 -*-
#
# print("0123".i_n_ "123abc".i_n_ "abc123".i_n_
# # (True, True, True)
# print("строка".isalnum())
# # True
# print("".i_n_ "123 abc".i_n_ "abc, 123.".i_n_
# # (False, False, False)
#
#
# print("string".i_a_ "строка".i_a_ "".i_a_
# # (True, True, False)
# print("123abc".i_a_ "str str".i_a_ "st,st".i_a_
# # (False, False, False)
#
#
# print("0123".i_d_ "123abc".i_d_ "abc123".i_d_
# # (True, False, False)
#
#
# print("123".i_d_ "123стр".i_d_
# # (True, False)
#
#
# print("\u2155".i_n_ "\u2155".i_d_
# # (True, False)
# print("\u2155") # Выведет символ "1/5"
#
#
# print("STRING".isu.. "СТРОКА".isu.. "".isu..
# # (True, True, False)
# print("STRING1".isu.. "СТРОКА, 123".isu.. "123".isu..
# # (True, True, False)
# print("string".isu.. "STRing".isu..
# # (False, False)
#
#
# print("srting".isl.. "строка".isl.. "".isl..
# # (True, True, False)
# print("string1".isl.. "str, 123".isl.. "123".isl..
# # (True, True, False)
# print("STRING".isl.. "Строка".isl..
# # (False, False)
#
#
# print("Str Str".ist.. "Стр Стр".ist..
# # (True, True)
# print("Str Str 123".ist.. "Стр Стр 123".ist..
# # (True, True)
# print("Str str".ist.. "Стр стр".ist..
# # (False, False)
# print("".ist.. "123".ist..
# # (False, False)
#
#
# print("123".isp..
# # True
# print("PHP Python".isp..
# # True
# print("\n".isp..
# # False
#
#
# print("".iss.. " \n\r\t".iss.. "str str".iss..
# # (False, True, False)
#
#
# print("s".isi..
# # True
# print("func".isi..
# # True
# print("123func".isi..
# # False
#
# ______ key____
#
# print(?.isk..("else"
# # True
# print(?.isk..("elsewhere"
# # False