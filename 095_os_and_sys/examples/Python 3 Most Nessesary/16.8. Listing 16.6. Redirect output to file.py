# -*- coding: utf-8 -*-

import sys                  # Подключаем модуль sys
tmp_out = sys.stdout        # Сохраняем ссылку на sys.stdout
f = open(r"file.txt", "a")  # Открываем файл на дозапись
sys.stdout = f              # Перенаправляем вывод в файл
print("Пишем строку в файл")
sys.stdout = tmp_out        # Восстанавливаем стандартный вывод
print("Пишем строку в стандартный вывод")
# Пишем строку в стандартный вывод
f.close()                   # Закрываем файл


f = open(r"file.txt", "a")
print("Пишем строку в файл", file=f)
f.close()


f = open(r"file.txt", "a")
print("Пишем строку в файл", file = f, flush = True)
print("Пишем другую строку в файл", file = f, flush = True)
f.close()
