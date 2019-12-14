# Создание списка чисел
my_list = [5, 1, 5, 7, 8, 1, 0, -23]

# Вывод списка
print(my_list)

# Получение длины списка
length = len(my_list)

# Ввод индекса
index = length
while not -length <= index < length:
    index = int(input('Введите индекс элемента списка (от %d до %d): '
                      % (-length, length - 1)))

# Ввод нового значения
value = int(input('Введите новое значение заданного элемента: '))

# Изменение элемента списка
my_list[index] = value

# Вывод списка на экран
print(my_list)