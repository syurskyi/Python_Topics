"""
Примеры других общих для изменяемых последовательностей методов.
"""


sequence = [1, 3, 5]
print(sequence)

# Добавление элемента в конец
sequence.append(3)  # sequence[len(sequence):] = [3]
print(sequence)

# Добавление в конец элементов из итерабельного объекта
sequence.extend(range(3))  # sequence[len(sequence):] = range(3)
print(sequence)

# Добавление элемента по индексу
sequence.insert(1, 8)  # sequence[1:1] = [8]
print(sequence)

# Удаление первого вхождения элемента
sequence.remove(3)  # del sequence[sequence.index(3)]
print(sequence)

# Удаление последнего элемента
sequence.pop()  # del sequence[-1]
print(sequence)

# Удаление элемента по индексу
sequence.pop(4)  # del sequence[4]
print(sequence)

# Удаление всех элементов
sequence.clear()  # del sequence[:]
print(sequence)
