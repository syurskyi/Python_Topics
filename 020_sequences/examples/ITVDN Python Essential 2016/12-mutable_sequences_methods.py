"""
Примеры других общих для изменяемых последовательностей методов.
"""


sequence = list(range(10))
print(sequence)

# Неполное копирование
copy = sequence.copy()  # copy = sequence[:]
print(copy)

# Разворот в обратном порядке
sequence.reverse()
print(sequence)
