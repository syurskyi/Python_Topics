# -*- coding: utf-8 -*-
import re

p = re.compile(r"^.+$")       # Точка не соответствует \n
p.findall("str1\nstr2\nstr3") # Ничего не найдено
# []
p = re.compile(r"^.+$", re.S) # Теперь точка соответствует \n
p.findall("str1\nstr2\nstr3") # Строка полностью соответствует
# ['str1\nstr2\nstr3']
p = re.compile(r"^.+$", re.M) # Многострочный режим
p.findall("str1\nstr2\nstr3") # Получили каждую подстроку
# ['str1', 'str2', 'str3']