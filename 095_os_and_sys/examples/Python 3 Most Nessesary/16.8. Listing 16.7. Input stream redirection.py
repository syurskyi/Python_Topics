# -*- coding: utf-8 -*-

import sys
tmp_in = sys.stdin          # Сохраняем ссылку на sys.stdin
f = open(r"file.txt", "r")  # Открываем файл на чтение
sys.stdin = f               # Перенаправляем ввод
while True:
    try:
        line = input()      # Считываем строку из файла
        print(line)         # Выводим строку
    except EOFError:        # Если достигнут конец файла,
        break               # выходим из цикла
sys.stdin = tmp_in          # Восстанавливаем стандартный ввод
f.close()                   # Закрываем файл
input()


tmp_in = sys.stdin           # Сохраняем ссылку на sys.stdin
f = open(r"file.txt", "r")
sys.stdin = f                # Перенаправляем ввод
sys.stdin.isatty()           # Не ссылается на терминал
# False
sys.stdin = tmp_in           # Восстанавливаем стандартный ввод
sys.stdin.isatty()           # Ссылается на терминал
# True
f.close()                    # Закрываем файл