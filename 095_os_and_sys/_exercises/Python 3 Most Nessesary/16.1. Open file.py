# "C:\\temp\\new\\file.txt"    # Правильно
# 'C:\\temp\\new\\file.txt'
# r"C:\temp\new\file.txt"      # Правильно
# 'C:\\temp\\new\\file.txt'
# "C:\temp\new\file.txt"       # Неправильно!!!
# 'C:\temp\new\x0cile.txt'


open("C:\temp\new\file.txt")
# Traceback (most recent call last):
#   File "<pyshell#0>", line 1, in <module>
#     open("C:\temp\new\file.txt")
# OSError: [Errno 22] Invalid argument: 'C:\temp\new\x0cile.txt'


import os.path # Подключаем модуль
# Файл в текущем рабочем каталоге (C:\book\)
os.path.abspath(r"file.txt")
# 'C:\\book\\file.txt'


# Открываемый файл в C:\book\folder1\
os.path.abspath(r"folder1/file.txt")
# 'C:\\book\\folder1\\file.txt'
# Открываемый файл в C:\book\folder1\folder2\
os.path.abspath(r"folder1/folder2/file.txt")
# 'C:\\book\\folder1\\folder2\\file.txt'


# Открываемый файл в C:\
os.path.abspath(r"../file.txt")
# 'C:\\file.txt'

# Открываемый файл в C:\book\folder1\
os.path.abspath(r"/book/folder1/file.txt")
# 'C:\\book\\folder1\\file.txt'
# Открываемый файл в C:\book\folder1\folder2\
os.path.abspath(r"/book/folder1/folder2/file.txt")
# 'C:\\book\\folder1\\folder2\\file.txt'


os.path.sep
# '\\'
os.path.abspath(r"C:/book/folder1/file.txt")
# 'C:\\book\\folder1\\file.txt'