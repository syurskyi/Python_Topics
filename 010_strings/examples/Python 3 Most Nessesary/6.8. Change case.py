# -*- coding: utf-8 -*-

print("строка".upper())
# СТРОКА

print("СТРОКА".lower())
# строка

print("СТРОКА строка".swapcase())
# строка СТРОКА

print("строка строка".capitalize())
# Строка строка


s = "первая буква каждого слова станет прописной"
print(s.title())
# Первая Буква Каждого Слова Станет Прописной


print("Python".casefold() == "python".casefold())
# True
print("grosse".casefold() == "große".casefold())
# True
