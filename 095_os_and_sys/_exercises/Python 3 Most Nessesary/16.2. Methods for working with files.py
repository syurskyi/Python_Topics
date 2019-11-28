with open(r"file.txt", "w", encoding="cp1251") as f:
    f.write("Строка")  # Записываем строку в файл
# Здесь файл уже закрыт автоматически


# Текстовый режим
f = open(r"file.txt", "w", encoding="cp1251")
f.write("Строка1\nСтрока2")  # Записываем строку в файл
# 15
f.close()                   # Закрываем файл
# Бинарный режим
f = open(r"file.txt", "wb")
f.write(bytes("Строка1\nСтрока2", "cp1251"))
# 15
f.write(bytearray("\nСтрока3", "cp1251"))
# 8
f.close()


# Текстовый режим
f = open(r"file.txt", "w", encoding="cp1251")
f.writelines(["Строка1\n", "Строка2"])
f.close()
# Бинарный режим
f = open(r"file.txt", "wb")
arr = [bytes("Строка1\n", "cp1251"), bytes("Строка2", "cp1251")]
f.writelines(arr)
f.close()


f = open(r"file.txt", "r")        # Открываем файл для чтения
f.writable()
# False
f = open(r"file.txt", "w")        # Открываем файл для записи
f.writable()
# True


# Текстовый режим
with open(r"file.txt", "r", encoding="cp1251") as f:
    f.read()

'Строка1\nСтрока2'
# Бинарный режим
with open(r"file.txt", "rb") as f:
    f.read()

# b'\xd1\xf2\xf0\xee\xea\xe01\n\xd1\xf2\xf0\xee\xea\xe02'


# Текстовый режим
f = open(r"file.txt", "r", encoding="cp1251")
f.read(8)               # Считываем 8 символов
# 'Строка1\n'
f.read(8)               # Считываем 8 символов
# 'Строка2'
f.read(8)               # Достигнут конец файла
# ''
f.close()


# Текстовый режим
f = open(r"file.txt", "r", encoding="cp1251")
f.readline(), f.readline()
# ('Строка1\n', 'Строка2')
f.readline()            # Достигнут конец файла
''
f.close()
# Бинарный режим
f = open(r"file.txt", "rb")
f.readline(), f.readline()
# (b'\xd1\xf2\xf0\xee\xea\xe01\n', b'\xd1\xf2\xf0\xee\xea\xe02')
f.readline()            # Достигнут конец файла
# b''
f.close()


f = open(r"file.txt", "r", encoding="cp1251")
f.readline(2), f.readline(2)
# ('Ст', 'ро')
f.readline(100)  # Возвращается одна строка, а не 100 символов
# 'ка1\n'
f.close()


# Текстовый режим
with open(r"file.txt", "r", encoding="cp1251") as f:
    f.readlines()
# ['Строка1\n', 'Строка2']
# Бинарный режим
with open(r"file.txt", "rb") as f:
    f.readlines()

# [b'\xd1\xf2\xf0\xee\xea\xe01\n', b'\xd1\xf2\xf0\xee\xea\xe02']


# Текстовый режим
f = open(r"file.txt", "r", encoding="cp1251")
f.__next__(), f.__next__()
# ('Строка1\n', 'Строка2')
f.__next__()  # Достигнут конец файла
# Traceback (most recent call last):
#   File "<pyshell#26>", line 1, in <module>
#     f.__next__() # Достигнут конец файла
# StopIteration
f.close()


f = open(r"file.txt", "r", encoding="cp1251")
for line in f:
    print(line.rstrip("\n"), end=" ")

# Строка1 Строка2
f.close()


f = open(r"file.txt", "r", encoding="cp1251")
f.fileno()                    # Дескриптор файла
# 3
f.close()


f = open(r"file.txt", "r+", encoding="cp1251")
f.read()
# 'Строка1\nСтрока2'
f.truncate(5)
# 5
f.close()
with open(r"file.txt", "r", encoding="cp1251") as f:
    f.read()

# 'Строк'


with open(r"file.txt", "w", encoding="cp1251") as f:
        f.write("String1\nString2")

# 15
f = open(r"file.txt", "r", encoding="cp1251")
f.tell()      # Указатель расположен в начале файла
# 0
f.readline()  # Перемещаем указатель
# 'String1\n'
f.tell()      # Возвращает 9 (8 + '\r'), а не 8 !!!
# 9
f.close()


f = open(r"file.txt", "rb")
f.readline()  # Перемещаем указатель
# b'String1\r\n'
f.tell()      # Теперь значение соответствует
# 9
f.close()


import io
io.SEEK_SET, io.SEEK_CUR, io.SEEK_END
# (0, 1, 2)


import io
f = open(r"file.txt", "rb")
f.seek(9, io.SEEK_CUR)  # 9 байтов от указателя
# 9
f.tell()
# 9
f.seek(0, io.SEEK_SET)  # Перемещаем указатель в начало
# 0
f.tell()
# 0
f.seek(-9, io.SEEK_END)  # -9 байтов от конца файла
# 7
f.tell()
# 7
f.close()


f = open(r"C:\temp\new\file.txt", "r")
f.seekable()
# True


f = open(r"file.txt", "r+b")
f.name, f.mode, f.closed
# ('file.txt', 'rb+', False)
f.close()
f.closed
# True
#

f = open(r"file.txt", "a", encoding="cp1251")
f.encoding
# 'cp1251'
f.close()


import sys
sys.stdout.encoding
# 'cp1251'


f = open(r"file.txt", "w", encoding="cp1251")
f.buffer.write(bytes("Строка", "cp1251"))
# 6
f.close()