"""Пример использования файлового объекта io.StringIO"""

import io

# Создание потока
stream = io.StringIO()  # или io.StringIO('начальное значение')

# Запись данных в поток
stream.write('asdf in memory')

# Получение строки из объекта StringIO
print(stream.getvalue())

# Вывод текущей позиции
print('Current position:', stream.tell())

# Переход в начало потока
stream.seek(0)

# Запись данных в поток
stream.write('data')

# Вывод текущей позиции
print('Current position:', stream.tell())

# Чтение оставшихся данных в потоке
print(stream.read())

# Вывод текущей позиции
print('Current position:', stream.tell())

# Получение строки из объекта StringIO
print(stream.getvalue())
