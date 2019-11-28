import os
os.name               # Значение в ОС Windows 8
# 'nt'
import os                # Подключаем модуль


mode = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
f = os.open(r"file.txt", mode)
os.write(f, b"String1\n")  # Записываем данные
# 8
os.close(f)               # Закрываем файл


mode = os.O_WRONLY | os.O_CREAT | os.O_APPEND
f = os.open(r"file.txt", mode)
os.write(f, b"String2\n") # Записываем данные
# 8
os.close(f)               # Закрываем файл


f = os.open(r"file.txt", os.O_RDONLY)
os.read(f, 50)            # Читаем 50 байт
# b'String1\nString2\n'
os.close(f)               # Закрываем файл


f = os.open(r"file.txt", os.O_RDONLY | os.O_BINARY)
os.read(f, 50)            # Читаем 50 байт
# b'String1\r\nString2\r\n'
os.close(f)               # Закрываем файл


f = os.open(r"file.txt", os.O_RDONLY)
os.read(f, 5), os.read(f, 5), os.read(f, 5), os.read(f, 5)
# (b'Strin', b'g1\nS', b'tring', b'2\n')
os.read(f, 5)             # Достигнут конец файла
# b''
os.close(f)               # Закрываем файл


f = os.open(r"file.txt", os.O_RDONLY | os.O_BINARY)
os.lseek(f, 0, os.SEEK_END)  # Перемещение в конец файла
# 18
os.lseek(f, 0, os.SEEK_SET)  # Перемещение в начало файла
# 0
os.lseek(f, 9, os.SEEK_CUR)  # Относительно указателя
# 9
os.lseek(f, 0, os.SEEK_CUR)  # Текущее положение указателя
# 9
os.close(f)                 # Закрываем файл


fd = os.open(r"file.txt", os.O_RDONLY)
fd
# 3
f = os.fdopen(fd, "r")
f.fileno()  # Объект имеет тот же дескриптор
# 3
f.read()
'String1\nString2\n'
f.close()