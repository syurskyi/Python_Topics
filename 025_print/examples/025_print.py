# -*- coding: utf-8 -*-

# Строка-разделитель выводиться не будет
x = 'spam'
y = 99
z = ['eggs']
print(x, y, z, sep='')

# Нестандартная строка-разделитель
x = 'spam'
y = 99
z = ['eggs']
print(x, y, z, sep=', ')

# Подавление вывода символа конца строки
x = 'spam'
y = 99
z = ['eggs']
print(x, y, z, end='')

# Вывод двух строк в одной строке
x = 'spam'
y = 99 z = ['eggs']
print(x, y, z, end='')
print(x, y, z)

# Нестандартный разделитель строк
x = 'spam'
y = 99
z = ['eggs']
print(x, y, z, end='...\n')

# Несколько именованных аргументов
x = 'spam'
y = 99
z = ['eggs']
print(x, y, z, sep='...', end='!\n')

# Порядок не имеет значения
x = 'spam'
y = 99
z = ['eggs']
print(x, y, z, end='!\n', sep='...')

# Вывод в файл
x = 'spam'
y = 99
z = ['eggs']
print(x, y, z, sep='...', file=open('data.txt', 'w'))

# Вывод содержимого текстового файла
x = 'spam'
y = 99
z = ['eggs']
print(open('data.txt').read())

# Сохранить для последующего восстановления Перенаправить вывод в файл Выведет в файл, а не на экран Вытолкнуть буферы
# на диск Восстановить первоначальный поток Результаты более ранних обращений
import sys
x = 'spam'
y = 99
z = ['eggs']
temp = sys.stdout
sys.stdout = open('log.txt', 'a')
print('spam')
print(1, 2, 3)
sys.stdout.close()
sys.stdout = temp
print('back here')
print(open('log.txt').read())

# В версии 3.0 именованный аргумент file позволяет перенаправить в файл вывод единственного вызова функции print,
# не прибегая к переустановке значения sys.stdout.
import sys
x = 'spam'
y = 99
z = ['eggs']
log = open(‘log.txt’, ‘a’)
# 3.0 print(x, y, z, file=log) # Вывести в объект, напоминающий файл print(a, b, c) Вывести в оригинальный поток вывода


# Эти способы перенаправления удобно использовать, когда в одной и той же программе необходимо организовать вывод
# и в файл, и в стандартный поток вывода. Однако если вы собираетесь использовать эти формы вывода, вам потребуется
# создать объект-файл (или объект, который имеет метод write, как и объект файла) и передавать инструкции этот объект,
# а не строку с именем файла:

import sys
x = 'spam'
y = 99
z = ['eggs']
log = open('log.txt', 'w')
print(1, 2, 3, file=log)
# В 2.6: print >> log, 1, 2, 3 print(4, 5, 6, file=log) log.close() print(7, 8, 9) # В 2.6: print 7, 8, 9 print(open('log.txt').read())

# Эти расширенные формы инструкции print нередко используются для вывода сообщений об ошибках в стандартный поток ошибок,
# sys.stderr. Вы можете либо использовать его метод write и форматировать выводимые строки вручную, либо использовать
# синтаксис перенаправления:

import sys
sys.stderr.write(('Bad!' * 8) + '\n')
# Bad!Bad!Bad!Bad!Bad!Bad!Bad!Bad! print('Bad!' * 8, file=sys.stderr) # В 2.6: print >> sys.stderr, ‘Bad’ * 8 # Bad!Bad!Bad!Bad!Bad!Bad!Bad!Bad!

# я вывод текста обоими способами в версии 3.0, перенаправление вывода во внешний файл и выполняется проверка содержимого
# екстовых файлов:
X = 1; Y = 2 print(X, Y)
# Вывод: простой способ # 1 2 import sys # Вывод: сложный способ sys.stdout.write(str(X) + ' ' + str(Y) + '\n') print(X, Y, file=open('temp1', 'w')) # Перенаправление в файл open('temp2', 'w').write(str(X) + ' ' + str(Y) + '\n') # Запись в файл print(open('temp1', 'rb').read()) # Двоичный режим print(open('temp2', 'rb').read())
