# -*- coding: utf-8 -*-

# Nested handlers
try:                                  # Обрабатываем исключения
    try:                              # Вложенный обработчик
        x = 1 / 0                     # Ошибка: деление на 0
    except NameError:
        print("Неопределенный идентификатор")
    except IndexError:
        print("Несуществующий индекс")
    print("Выражение после вложенного обработчика")
except ZeroDivisionError:
    print("Обработка деления на 0")
    x = 0
print(x)                              # Выведет: 0