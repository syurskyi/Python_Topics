# -*- coding: utf-8 -*-

print(str(), str([1, 2]), str((3, 4)), str({"x": 1}))
# ('', '[1, 2]', '(3, 4)', "{'x': 1}")
print("строка1\nстрока2")
# строка1
# строка2


print(repr("Строка"), repr([1, 2, 3]), repr({"x": 5}))
# ("'Строка'", '[1, 2, 3]', "{'x': 5}")
print(repr("строка1\nстрока2"))
# "'строка1\\nстрока2'"


print(ascii([1, 2, 3]), ascii({"x": 5}))
# ('[1, 2, 3]', "{'x': 5}")
print(ascii("строка"))
# "'\\u0441\\u0442\\u0440\\u043e\\u043a\\u0430'"


print(len("Python"), len("\r\n\t"), len(r"\r\n\t"))
# (6, 3, 6)
print(len("строка"))
# 6


s1, s2 = "     str\n\r\v\t", "strstrstrokstrstrstr"
print("'%s' — '%s'" % (s1.strip(), s2.strip("tsr")))
# "'str' — 'ok'"


s1, s2 = "     str     ", "strstrstrokstrstrstr"
print("'%s' — '%s'" % (s1.lstrip(), s2.lstrip("tsr")))
# "'str     ' — 'okstrstrstr'"

s1, s2 = "     str     ", "strstrstrokstrstrstr"
print("'%s' — '%s'" % (s1.rstrip(), s2.rstrip("tsr")))
# "'     str' — 'strstrstrok'"


s = "word1 word2 word3"
print(s.split(), s.split(None, 1))
# (['word1', 'word2', 'word3'], ['word1', 'word2 word3'])
s = "word1\nword2\nword3"
print(s.split("\n"))
# ['word1', 'word2', 'word3']


s = "word1           word2 word3     "
print(s.split())
# ['word1', 'word2', 'word3']


s = ",,word1,,word2,,word3,,"
print(s.split(","))
# ['', '', 'word1', '', 'word2', '', 'word3', '', '']
print("1,,2,,3".split(","))
# ['1', '', '2', '', '3']


print("word1 word2 word3".split("\n"))
# ['word1 word2 word3']


s = "word1 word2 word3"
print(s.rsplit(), s.rsplit(None, 1))
# (['word1', 'word2', 'word3'], ['word1 word2', 'word3'])
print("word1\nword2\nword3".rsplit("\n"))
# ['word1', 'word2', 'word3']


print("word1\nword2\nword3".splitlines())
# ['word1', 'word2', 'word3']
print("word1\nword2\nword3".splitlines(True))
# ['word1\n', 'word2\n', 'word3']
print("word1\nword2\nword3".splitlines(False))
# ['word1', 'word2', 'word3']
print("word1 word2 word3".splitlines())
# ['word1 word2 word3']


print("word1 word2 word3".partition(" "))
# ('word1', ' ', 'word2 word3')
print("word1 word2 word3".partition("\n"))
# ('word1 word2 word3', '', '')


print("word1 word2 word3".rpartition(" "))
# ('word1 word2', ' ', 'word3')
print("word1 word2 word3".rpartition("\n"))
# ('', '', 'word1 word2 word3')


print(" => ".join(["word1", "word2", "word3"]))
# 'word1 => word2 => word3'
print(" ".join(("word1", "word2", "word3")))
# 'word1 word2 word3'


" ".join(("word1", "word2", 5))
# Traceback (most recent call last):
#   File "<pyshell#48>", line 1, in <module>
#     " ".join(("word1", "word2", 5))
# TypeError: sequence item 2: expected str instance, int found


s = "Python"
arr = list(s); arr        # Преобразуем строку в список
# ['P', 'y', 't', 'h', 'o', 'n']
arr[0] = "J"; arr         # Изменяем элемент по индексу
# ['J', 'y', 't', 'h', 'o', 'n']
s = "".join(arr); s       # Преобразуем список в строку
# 'Jython'


s = "Python"
b = bytearray(s, "cp1251"); b
# bytearray(b'Python')
b[0] = ord("J"); b
# bytearray(b'Jython')
s = b.decode("cp1251"); s
# 'Jython'