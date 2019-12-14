# -*- coding: utf-8 -*-

print("0123".isalnum(), "123abc".isalnum(), "abc123".isalnum())
# (True, True, True)
print("строка".isalnum())
# True
print("".isalnum(), "123 abc".isalnum(), "abc, 123.".isalnum())
# (False, False, False)


print("string".isalpha(), "строка".isalpha(), "".isalpha())
# (True, True, False)
print("123abc".isalpha(), "str str".isalpha(), "st,st".isalpha())
# (False, False, False)


print("0123".isdigit(), "123abc".isdigit(), "abc123".isdigit())
# (True, False, False)


print("123".isdecimal(), "123стр".isdecimal())
# (True, False)


print("\u2155".isnumeric(), "\u2155".isdigit())
# (True, False)
print("\u2155") # Выведет символ "1/5"


print("STRING".isupper(), "СТРОКА".isupper(), "".isupper())
# (True, True, False)
print("STRING1".isupper(), "СТРОКА, 123".isupper(), "123".isupper())
# (True, True, False)
print("string".isupper(), "STRing".isupper())
# (False, False)


print("srting".islower(), "строка".islower(), "".islower())
# (True, True, False)
print("string1".islower(), "str, 123".islower(), "123".islower())
# (True, True, False)
print("STRING".islower(), "Строка".islower())
# (False, False)


print("Str Str".istitle(), "Стр Стр".istitle())
# (True, True)
print("Str Str 123".istitle(), "Стр Стр 123".istitle())
# (True, True)
print("Str str".istitle(), "Стр стр".istitle())
# (False, False)
print("".istitle(), "123".istitle())
# (False, False)


print("123".isprintable())
# True
print("PHP Python".isprintable())
# True
print("\n".isprintable())
# False


print("".isspace(), " \n\r\t".isspace(), "str str".isspace())
# (False, True, False)


print("s".isidentifier())
# True
print("func".isidentifier())
# True
print("123func".isidentifier())
# False

import keyword

print(keyword.iskeyword("else"))
# True
print(keyword.iskeyword("elsewhere"))
# False