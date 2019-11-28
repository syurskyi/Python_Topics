import io              # Подключаем модуль
f = io.StringIO("String1\n")
f.getvalue()           # Получаем содержимое файла
# 'String1\n'
f.close()              # Закрываем файл


f = io.StringIO("String1\n")
f.tell()        # Позиция указателя
# 0
f.seek(0, 2)    # Перемещаем указатель в конец файла
# 8
f.tell()        # Позиция указателя
# 8
f.seek(0)       # Перемещаем указатель в начало файла
# 0
f.tell()        # Позиция указателя
# 0
f.close()       # Закрываем файл


f = io.StringIO("String1\n")
f.seek(0, 2)         # Перемещаем указатель в конец файла
# 8
f.write("String2\n")  # Записываем строку в файл
# 8
f.getvalue()         # Получаем содержимое файла
# 'String1\nString2\n'
f.close()            # Закрываем файл


f = io.StringIO()
f.writelines(["String1\n", "String2\n"])
f.getvalue()         # Получаем содержимое файла
# 'String1\nString2\n'
f.close()            # Закрываем файл


f = io.StringIO("String1\nString2\n")
f.read()
# 'String1\nString2\n'
f.seek(0)  # Перемещаем указатель в начало файла
# 0
f.read(5), f.read(5), f.read(5), f.read(5), f.read(5)
# ('Strin', 'g1\nSt', 'ring2', '\n', '')
f.close()  # Закрываем файл


f = io.StringIO("String1\nString2")
f.readline(), f.readline(), f.readline()
# ('String1\n', 'String2', '')
f.close()  # Закрываем файл


f = io.StringIO("String1\nString2\nString3\n")
f.readline(5), f.readline(5)
# ('Strin', 'g1\n')
f.readline(100)  # Возвращается одна строка, а не 100 символов
# 'String2\n'
f.close()       # Закрываем файл


f = io.StringIO("String1\nString2\nString3")
f.readlines()
# ['String1\n', 'String2\n', 'String3']
f.close()  # Закрываем файл


f = io.StringIO("String1\nString2\nString3")
f.readlines(14)
# ['String1\n', 'String2\n']
f.seek(0)  # Перемещаем указатель в начало файла
# 0
f.readlines(17)
# ['String1\n', 'String2\n', 'String3']
f.close()  # Закрываем файл


f = io.StringIO("String1\nString2")
f.__next__(), f.__next__()
# ('String1\n', 'String2')
f.__next__()
# ... Фрагмент опущен ...
# StopIteration
f.close()  # Закрываем файл


f = io.StringIO("String1\nString2")
for line in f:
    print(line.rstrip())

# String1
# String2
f.close()  # Закрываем файл


f = io.StringIO("String1\nString2\nString3")
f.truncate(15)     # Обрезаем файл
# 15
f.getvalue()       # Получаем содержимое файла
# 'String1\nString2'
f.close()          # Закрываем файл


f = io.StringIO("String1\nString2\nString3")
f.seek(15)         # Перемещаем указатель
# 15
f.truncate()       # Обрезаем файл до указателя
# 15
f.getvalue()       # Получаем содержимое файла
# 'String1\nString2'
f.close()          # Закрываем файл


import io             # Подключаем модуль
f = io.BytesIO(b"String1\n")
f.seek(0, 2)          # Перемещаем указатель в конец файла
# 8
f.write(b"String2\n")  # Пишем в файл
# 8
f.getvalue()          # Получаем содержимое файла
# b'String1\nString2\n'
f.seek(0)             # Перемещаем указатель в начало файла
# 0
f.read()              # Считываем данные
# b'String1\nString2\n'
f.close()             # Закрываем файл


f = io.BytesIO(b"Python")
buf = f.getbuffer()
buf[0]                # Получаем значение по индексу
# b'P'
buf[0] = b"J"         # Изменяем значение по индексу
f.getvalue()          # Получаем содержимое
# b'Jython'
buf.tolist()          # Преобразуем в список чисел
# [74, 121, 116, 104, 111, 110]
buf.tobytes()         # Преобразуем в тип bytes
# b'Jython'
f.close()             # Закрываем файл
