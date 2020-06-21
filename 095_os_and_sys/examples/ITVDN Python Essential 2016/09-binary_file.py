"""Пример использования бинарного файла"""

from array import array
import os.path

prefix = os.path.join('data', 'ex09_')

# Создание списка чисел
numbers = list(range(300, 400))

# Запись в текстовый файл
with open(prefix + 'text.txt', 'w') as txt_file:
    print(numbers, file=txt_file)

# Создание массива, поддеживающего buffer protocol, из списка
numbers_array = array('i', numbers)

# Запись в бинарный файл
binary_filename = prefix + 'binary.bin'
with open(binary_filename, 'wb') as bin_file:
    bin_file.write(numbers_array)

# Подготовка массива
filesize = os.path.getsize(binary_filename)  # размер файла
int_len = array('i').itemsize  # размер одного элемента в байтах
read_array = array('i', (0 for _ in range(filesize // int_len)))

# Чтение из бинарного файла
with open(binary_filename, 'rb') as file:
    file.readinto(read_array)  # чтение в массив

# Вывод массива на экран
print(read_array)

# Проверка, что считанные данные соответствуют изначальным
print(read_array.tolist() == numbers)
