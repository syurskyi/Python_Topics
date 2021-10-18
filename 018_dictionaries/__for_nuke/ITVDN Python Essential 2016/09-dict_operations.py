"""Обзор операций со словарями"""

phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}

# len(d) – количество элементов.
print(len(phonebook), 'entries found')

print()

# d[key] – получение значения с ключом key. Если такой ключ не существует
# и отображение реализует специальный метод __missing__(self, key), то он
# вызывается. Если ключ не существует и метод __missing__ не определён,
# выбрасывается исключение KeyError.
try:
    print('Mary:', phonebook['Mary'])
    print('Lumberjack:', phonebook['Lumberjack'])
except KeyError as e:
    print('No entry for', *e.args)

print()

# d[key] = value – изменить значение или создать новую пару ключ-значение, если
# ключ не существует.
phonebook['Lumberjack'] = '000-777'

# key in d, key not in d – проверка наличия ключа в отображении.
for person in ('Guido', 'Mary', 'Ahmed'):
    if person in phonebook:
        print(person, 'is in the phonebook')
    else:
        print('No entry found for', person)

print()

# iter(d) – то же самое, что iter(d.keys()).
print('People in the phonebook:')
for person in phonebook:
    print(person)

print()

# copy() – создать неполную копию словаря.
phonebook_copy = phonebook.copy()
print('Phonebook:', phonebook)
print('Phonebook copy:', phonebook_copy)

print()

# clear() – удалить все элементы словаря.
phonebook_copy.clear()
print('Phonebook:', phonebook)
print('Phonebook copy:', phonebook_copy)

print()

# (метод класса) dict.fromkeys(sequence[, value]) – создаёт новый словарь с
# ключами из последовательности sequence и заданным значением (по умолчанию –
# None).
numbers_dict = dict.fromkeys(range(3), 42)
print(numbers_dict)

print()

# d.get(key[, default]) – безопасное получение значения по ключу (никогда не
# выбрасывает KeyError).  Если ключ не найден, возвращается значение default
# (по-умолчанию – None).
for key in range(5):
    print('{}:'.format(key), numbers_dict.get(key, 0))

print()

# d.items() – в Python 3 возвращает объект представления словаря,
# соответствующий парам (двухэлементным кортежам) вида (ключ, значение).  В
# Python 2 возвращает соответствующий список, а метод iteritems() возвращает
# итератор.  Аналогичный метод в Python 2.7 – viewitems().
print('Items:', phonebook.items())

# d.keys() – в Python 3 возвращает объект представления словаря,
# соответствующий ключам словаря.  В Python 2 возвращает соответствующий
# список, а метод iterkeys() возвращает итератор.  Аналогичный метод в Python
# 2.7 – viewkeys().
print('Keys:', phonebook.keys())

# d.values() – в Python 3 возвращает объект представления словаря,
# соответствующий значениям.  В Python 2 возвращает соответствующий список, а
# метод itervalues() возвращает итератор.  Аналогичный метод в Python 2.7 –
# viewvalues().
print('Values:', phonebook.values())

print()

# d.pop(key[, default]) – если ключ key существует, удаляет элемент из словаря
# и возвращает его значение.  Если ключ не существует и задано значение
# default, возвращается данное значение, иначе выбрасывается исключение
# KeyError.
number = phonebook.pop('Lumberjack')
print('Deleted Lumberjack (was ' + number + ')')
print(phonebook)

print()

# d.popitem() – удаляет произвольную пару ключ-значение и возвращает её.  Если
# словарь пустой, возникает исключение KeyError.  Метод полезен для алгоритмов,
# которые обходят словарь, удаляя уже обработанные значения (например,
# определённые алгоритмы, связанные с теорией графов).
person = phonebook.popitem()
print('Popped {} (phone: {})'.format(*person))

print()

# d.setdefault(key[, default]) – если ключ key существует, возвращает
# соответствующее значение.  Иначе создаёт элемент с ключом key и значением
# default.  default по умолчанию равен None.
for person in ('Jack', 'Liz'):
    phone = phonebook.setdefault(person, '000-000')
    print('{}: {}'.format(person, phone))

print(phonebook)

print()

# d.update(mapping) – принимает либо другой словарь или отображение, либо
# итерабельный объект, состоящий из итерабельных объектов – пар ключ-значение,
# либо именованные аргументы.  Добавляет соответствующие элементы в словарь,
# перезаписывая элементы с существующими ключами.
phonebook.update({'Alex': '832-438', 'Alice': '231-987'})
phonebook.update([('Joe', '217-531'), ('James', '783-428')])
phonebook.update(Carl='783-923', Victoria='386-486')
print(phonebook)
