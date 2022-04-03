# # -*- coding: utf-8 -*-

# Поскольку мы указали режим w, то если файл не существует, он будет создан, а если существует,
# то будет перезаписан.
# Текстовый режим
# Открываем файл на запись
# Записываем строку в файл
# Закрываем файл
# В параметре errors можно указать уровень обработки ошибок. Возможные значения:
# "strict" (при ошибке возбуждается исключение ValueError - значение по умолчанию),
# "replace" (неизвестный символ заменяется символом вопроса или символом с кодом
# \ufffd), "ignore" (неизвестные символы игнорируются), "xmlcharrefreplace" (неизвестный
# символ заменяется последовательностью &#хххх;) и "backslashreplace" (неизвестный символ
# заменяется последовательностью \ uxxxx).

with open(r"file.txt", "w", encoding="cp1251") as f:
    f.write("Строка")  # Записываем строку в файл
# Здесь файл уже закрыт автоматически

# Методы для работы с файлами
# close ()
#
# закрывает файл. Так как интерпретатор автоматически удаляет объект, когда
# на него отсутствуют ссылки, в небольших программах можно явно не закрывать файл.
# Тем не менее, явное закрытие файла является признаком хорошего стиля программирования.
# Кроме того, при наличии незакрытого файла генерируется предупреждающее сообщение:
# "ResourceWarning: unclosed file".

# write (<данные>)
#
# записывает строку или последовательность байтов в файл. Если
# в качестве параметра указана строка, то файл должен быть открыт в текстовом режиме.
# Для записи последовательности байтов необходимо открыть файл в бинарном режиме.
# Помните, что нельзя записывать строку в бинарном режиме и последовательность байтов
# в текстовом режиме. Метод возвращает количество записанных символов или байтов.

# Текстовый режим
f = open(r"file.txt", "w", encoding="cp1251")
f.write("Строка1\nСтрока2")  # Записываем строку в файл
# 15
f.close()                   # Закрываем файл
# ######################################################################################################################

# Бинарный режим
f = open(r"file.txt", "wb")
f.write(bytes("Строка1\nСтрока2", "cp1251"))
# 15
# ######################################################################################################################

f.write(bytearray("\nСтрока3", "cp1251"))
# ######################################################################################################################
# 8
f.close()

# При использовании текстового режима (задается по умолчанию) при чтении производится
# попытка преобразовать данные в кодировку Unicode, а при записи выполняется обратная
# операция - строка преобразуется в последовательность байтов в определенной кодировке.
# По умолчаншо назначается кодировка, применяемая в системе. Если преобразование невозможно,
# то возбуждается исключение. Указать кодировку, которая будет использоваться при
# записи и чтении файла, позволяет параметр encoding.

# writelines (<Последовательность>)
#
# записывает последовательность в файл. Если все
# элементы последовательности являются строками, то файл должен быть открыт в текстовом
# режиме. Если все элементы являются последовательностями байтов, то файл
# должен быть открыт в бинарном режиме.

# Текстовый режим
f = open(r"file.txt", "w", encoding="cp1251")
f.writelines(["Строка1\n", "Строка2"])
f.close()
# Бинарный режим
f = open(r"file.txt", "wb")
arr = [bytes("Строка1\n", "cp1251"), bytes("Строка2", "cp1251")]
f.writelines(arr)
f.close()

# writable ()
# - возвращает True, если файл поддерживает запись, и False - в противном случае:

f = open(r"file.txt", "r")        # Открываем файл для чтения
f.writable()
# False
# ######################################################################################################################

f = open(r"file.txt", "w")        # Открываем файл для записи
f.writable()
# True
# ######################################################################################################################

# read ( [<Количество>] ) -
#
#  считывает данные из файла. Если файл открыт в текстовом
# режиме, то возвращается строка, а если в бинарном - последовательность байтов. Если
# параметр не указан, возвращает ся содержимое файла от текущей позиции указателя до
# конца файла:
# Если в качестве параметра указать число, то за каждый вызо в будет возвращаться указанное
# количество символов или байт ов. Когда достигается конец файла, метод возв ращает
# пустую строку

# Текстовый режим
with open(r"file.txt", "r", encoding="cp1251") as f:
    f.read()

'Строка1\nСтрока2'
# Бинарный режим
with open(r"file.txt", "rb") as f:
    f.read()
# b'\xd1\xf2\xf0\xee\xea\xe01\n\xd1\xf2\xf0\xee\xea\xe02'
# ######################################################################################################################

# Текстовый режим
f = open(r"file.txt", "r", encoding="cp1251")
f.read(8)               # Считываем 8 символов
# 'Строка1\n'
f.read(8)               # Считываем 8 символов
# 'Строка2'
f.read(8)               # Достигнут конец файла
# ''
f.close()
# ######################################################################################################################

# readline ( [ <Количество> J )
#
# считывает из файла одну строку при каждом вызове. Если
# файл открыт в текстовом режиме, то возвращается строка, а если в бинарном - последовательность
# байтов. Возвращаемая строка включает символ перевода строки. Исключением
# является последняя строка - если она не завершается символом перевода строки,
# то таковой добавлен не будет. При достижении конца файла возвращается пустая строка.
#
# Если в необязательном параметре указано число, то считывание будет выполняться до
# тех пор, пока не встретится символ новой строки {\n), символ конца файла или из файла
# не будет прочитано указанное количество символов. Иными словами, если количество
# символов в строке меньше значения параметра, то будет считана одна строка, а не указанное
# количество символов, а если количество символов в строке больше, то возвращается
# указанное количество символов.

# Текстовый режим
f = open(r"file.txt", "r", encoding="cp1251")
f.readline(), f.readline()
# ('Строка1\n', 'Строка2')
# ######################################################################################################################
# readline ( [ <Количество> J )
#
# считывает из файла одну строку при каждом вызове. Если
# файл открыт в текстовом режиме, то возвращается строка, а если в бинарном - последовательность
# байтов. Возвращаемая строка включает символ перевода строки. Исключением
# является последняя строка - если она не завершается символом перевода строки,
# то таковой добавлен не будет. При достижении конца файла возвращается пустая строка.
#
# Если в необязательном параметре указано число, то считывание будет выполняться до
# тех пор, пока не встретится символ новой строки {\n), символ конца файла или из файла
# не будет прочитано указанное количество символов. Иными словами, если количество
# символов в строке меньше значения параметра, то будет считана одна строка, а не указанное
# количество символов, а если количество символов в строке больше, то возвращается
# указанное количество символов.

f.readline()            # Достигнут конец файла
''
f.close()
# Бинарный режим
f = open(r"file.txt", "rb")
f.readline(), f.readline()
# (b'\xd1\xf2\xf0\xee\xea\xe01\n', b'\xd1\xf2\xf0\xee\xea\xe02')
# ######################################################################################################################

f.readline()            # Достигнут конец файла
# b''
# ######################################################################################################################
f.close()


f = open(r"file.txt", "r", encoding="cp1251")
f.readline(2), f.readline(2)
# ('Ст', 'ро')
# ######################################################################################################################

f.readline(100)  # Возвращается одна строка, а не 100 символов
# 'ка1\n'
f.close()
# ######################################################################################################################
# readlines ( ) -
#
# считывает все содержимое файла в список. Каждый элемент списка будет
# содержать одну строку, включая символ перевода строки. Исключением является
# последняя строка. Если она не завершается символом перевода строки, то символ перевода
# строки добавлен не будет. Если файл открыт в текстовом режиме, то возвращается
# список строк, а если в бинарном - список объектов типа bytes.

# Текстовый режим
with open(r"file.txt", "r", encoding="cp1251") as f:
    f.r..
# ['Строка1\n', 'Строка2']
# ######################################################################################################################

# Бинарный режим
with open(r"file.txt", "rb") as f:
    f.r..

# [b'\xd1\xf2\xf0\xee\xea\xe01\n', b'\xd1\xf2\xf0\xee\xea\xe02']
# ######################################################################################################################
# _next_ ()
#
# считывает одну строку при каждом вызове. Если файл открыт в текстовом
# режиме, возвращается строка, а если в бинарном - последовательность байтов. При
# достижении конца файла возбуждается исключение stopiteration.
#
# Благодаря методу _next_ ( ) мы можем перебирать файл построчно с помощью цикла
# for. Цикл for на каждой итерации будет автоматически вызывать метод _next_(). Для
# примера выведем все строки, предварительно удалив символ перевода строки:

# Текстовый режим
f = open(r"file.txt", "r", encoding="cp1251")
f.__next__(), f.__next__()
# ('Строка1\n', 'Строка2')
# ######################################################################################################################

f.__next__()  # Достигнут конец файла
# Traceback (most recent call last):
#   File "<pyshell#26>", line 1, in <module>
#     f.__next__() # Достигнут конец файла
# StopIteration
f.close()
# ######################################################################################################################

f = open(r"file.txt", "r", encoding="cp1251")
for line in f:
    print(line.rstrip("\n"), end=" ")
# Строка1 Строка2
f.close()
# ######################################################################################################################

# flush () - принудительно записывает данные из буфера на диск;
# fileno () - возвращает целочисленный дескриптор файла. Возвращаемое значение всегда будет больше числа 2, т . к.
# число О закреплено за стандартным вводом stdin, l - за стандартным выводом stdout, а 2 - за стандартным выводом
# сообщений об ошибках stderr.

f = open(r"file.txt", "r", encoding="cp1251")
f.fileno()                    # Дескриптор файла
# 3
f.close()
# ######################################################################################################################

f = open(r"file.txt", "r+", encoding="cp1251")
f.read()
# 'Строка1\nСтрока2'
# ######################################################################################################################
# truncate ([<Количество>])
#
# обрезает файл до указанного количества символов (если задан текстовый режим) или байтов (в случае бинарного режима).
# Метод возвращает новый размер файла.

f.truncate(5)
# 5
f.close()
# ######################################################################################################################

with open(r"file.txt", "r", encoding="cp1251") as f:
    f.read()
# 'Строк'
# ######################################################################################################################

with open(r"file.txt", "w", encoding="cp1251") as f:
        f.write("String1\nString2")

# 15
# ######################################################################################################################
# tell() - возвращает позицию указателя относительно начала файла в виде целого числа.
# Обратите внимание на то, что в Windows метод tell () считает символ \r как дополнительный
# байт, хотя этот символ удаляется при открытии файла в текстовом режиме.

f = open(r"file.txt", "r", encoding="cp1251")
f.tell()      # Указатель расположен в начале файла
# 0
# ######################################################################################################################

f.readline()  # Перемещаем указатель
# 'String1\n'
# ######################################################################################################################

f.tell()      # Возвращает 9 (8 + '\r'), а не 8 !!!
# 9
# ######################################################################################################################
f.close()


f = open(r"file.txt", "rb")
f.readline()  # Перемещаем указатель
# b'String1\r\n'
# ######################################################################################################################

f.tell()      # Теперь значение соответствует
# 9
f.close()
# ######################################################################################################################
# seek ( <Смещение> [, <Позиция>] )
#
# устанавливает указатель в позицию, имеющую смещение
# <Смещение> относительно позиции <Позиция>. В параметре <Позиция> мoryr быть
# указаны следующие атрибуты из модуля io или соответствующие им значения:
# • io.SEEK_SET или о- начало файла (значение по умолчанию);
# • io. SEEK _ cuR или 1 - текущая позиция указателя. Положительное значение смещения
# вызывает перемещение к концу файла, отрицательное - к его началу;
# • io. SEEK _ END или 2 - конец файла.
# Выведем значения этих атрибутов:

import io
io.SEEK_SET, io.SEEK_CUR, io.SEEK_END
# (0, 1, 2)
# ######################################################################################################################

import io
f = open(r"file.txt", "rb")
f.seek(9, io.SEEK_CUR)  # 9 байтов от указателя
# 9
# ######################################################################################################################

f.tell()
# 9
# ######################################################################################################################
f.seek(0, io.SEEK_SET)  # Перемещаем указатель в начало
# 0
# ######################################################################################################################
f.tell()
# 0
# ######################################################################################################################
f.seek(-9, io.SEEK_END)  # -9 байтов от конца файла
# 7
# ######################################################################################################################
f.tell()
# 7
# ######################################################################################################################
f.close()

# seekabe ()
#
# возвращает True, если указатель файла можно сдвинуть в друrую позицmо,
# и False - в противном случае:

f = open(r"C:\temp\new\file.txt", "r")
f.seekable()
# True
# ######################################################################################################################
# Помимо методов, объекты файлов поддерживают несколько атрибутов:
# + name - имя файла;
# + mode - режим, в котором был открыт файл;
# + closed - возвращает True, если файл был закрыт, и False - в противном случае.

f = open(r"file.txt", "r+b")
f.name, f.mode, f.closed
# ('file.txt', 'rb+', False)
# ######################################################################################################################
f.close()
f.closed
# True
#
# ######################################################################################################################
# encoding -
# название кодировки, которая будет использоваться для преобразования строк перед записью в файл или при чтении.
# Атрибут доступен только в текстовом режиме.
# Обратите также внимание на то, что изменить значение атрибута нельзя, поскольку он доступен только для чтения.
#
# Стандартный вывод stdout также является файловым объектом. Атрибут encoding этого объекта всегда содержит кодировку
# устройства вывода, поэтому строка преобразуется
# в последовательность байтов в правильной кодировке. Например , при запуске с помощью двойного щелчка на значке файла
# атрибут encoding будет иметь значение "ср866", а при запуске в окне Python Shell редактора IDLE - значение " ср1251 ".

f = open(r"file.txt", "a", encoding="cp1251")
f.encoding
# 'cp1251'
# ######################################################################################################################
f.close()

import sys
sys.stdout.encoding
# 'cp1251'
# ######################################################################################################################
# buffer -
# позволяет получить доступ к буферу. Атрибут доступен только в текстовом
# режиме. С помощью этого объекта можно записать последовательность байтов в текстовый
# поток.

f = open(r"file.txt", "w", encoding="cp1251")
f.buffer.write(bytes("Строка", "cp1251"))
# 6
f.close()