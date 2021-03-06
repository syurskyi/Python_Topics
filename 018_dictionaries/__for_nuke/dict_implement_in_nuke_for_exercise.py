# Генераторы словарей

# ===== Python Example ================================================================================

keys = ["a", "b"]  # Список с ключами
values = [1, 2] # Список со значениями
print({k: v for (k, v) in zip(keys, values)})
#  {'a': 1, 'b': 2}
# ======================================================================================================
# ===== Nuke Example ===================================================================================
transformNode = nuke.createNode('Transform', '{} {}'.format(keys[1], values[1]))


print({k: 0 for k in keys})
#  {'a': 0, 'b': 0}
d = {"a": 1, "b": 2, "c": 3, "d": 4 }
print({k: v for (k, v) in d.items() if v % 2 == 0})
# # {'b': 2, 'd': 4}

# Zip together keys and values
print(list(zip(['a', 'b', 'c'], [1, 2, 3])))

# Make a dict from zip result
D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))

# dict keyword argument form
print(dict(name='mel', age=45))

# dict key/value tuples form
print(dict([('name', 'mel'), ('age', 45)]))

# Zip together keys and values
print(list(zip(['a', 'b', 'c'], [1, 2, 3])))

# Make a dict from zip result
D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))

# dict comprehension
D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)

# dict comprehension
D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)

# dict comprehension
# Or: range(1, 5)
D = {x: x ** 2 for x in [1, 2, 3, 4]}
print(D)

# dict comprehension
# Loop over any iterable
D = {c: c * 4 for c in 'SPAM'}
print(D)

D = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
print(D)

# Initialize dict from keys
# with a comprehension
D = dict.fromkeys(['a', 'b', 'c'], 0)
# Initialize dict from keys
print(D)
D = {k:0 for k in ['a', 'b', 'c']}
# Same, but with a comprehension
print(D)

# d.get key[, default]
# безопасное получение значения по ключу  никогда не  выбрасывает KeyError .
# Если ключ не найден, возвращается значение default   по-умолчанию – None .
# #
numbers_dict = dict.fromkeys(range(3, 42))
print(numbers_dict)

for key in range(5):
    print('{}:'.format(key), numbers_dict.get(key, 0))

d = {'x': 1, 'y': 2, 'z': 3}
for key in d.keys():          # Использование метода keys()
    print("({0} => {1})".format(key, d[key],  end=" "))
# Выведет: (y => 2) (x => 1) (z => 3)
print()                       # Вставляем символ перевода строки
for key in d:                 # Словари также поддерживают итерации
    print("({0} => {1})".format(key, d[key], end=" "))
# Выведет: (y => 2) (x => 1) (z => 3)


d = {"x": 1, "y": 2, "z": 3}
k = list(d.keys())           # Получаем список ключей
k.sort()                     # Сортируем список ключей
for key in k:
    print("({0} => {1})".format(key,  d[key]), end=" ")
# Выведет: (x => 1) (y => 2) (z => 3)
print()

d = {'x': 1, 'y': 2, 'z': 3}
for key in sorted(d.keys()):
    print("({0} => {1})".format(key, d[key]), end=" ")
# Выведет: (x => 1) (y => 2) (z => 3)
print()

d = {'x': 1, 'y': 2, 'z': 3}
for key in sorted(d):
    print("({0} => {1})".format(key, d[key]), end=" ")
# Выведет: (x => 1) (y => 2) (z => 3)


# d.items
#  в Python 3 возвращает объект представления словаря, соответствующий парам  двухэлементным кортежам
#  вида  ключ, значение .  В  Python 2 возвращает соответствующий список, а метод iteritems   возвращает итератор.
# Аналогичный метод в Python 2.7 – viewitems  .
#
phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}

print('Items:', phonebook.items())

# d.keys
# в Python 3 возвращает объект представления словаря, соответствующий ключам словаря.  В Python 2 возвращает соответствующий
# список, а метод iterkeys   возвращает итератор.  Аналогичный метод в Python
# 2.7 – viewkeys  .
#
phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}

print('Keys:', phonebook.keys())

phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}

print('Values:', phonebook.values())

# # d.popitem
# # удаляет произвольную пару ключ-значение и возвращает её.  Если словарь пустой, возникает исключение KeyError.
# # Метод полезен для алгоритмов, которые обходят словарь, удаляя уже обработанные значения  например,
# # определённые алгоритмы, связанные с теорией графов .
# #
phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}

person = phonebook.popitem()
print('Popped {}  phone: {} '.format(*person))

# d.setdefault key[, default]
#  если ключ key существует, возвращает
# соответствующее значение.  Иначе создаёт элемент с ключом key и значением default.  default по умолчанию равен None.
#
phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}

for person in ('Jack', 'Liz'):
    phone = phonebook.setdefault(person, '000-000')
    print('{}: {}'.format(person, phonebook))
print(phonebook)

# d.update(mapping)
# принимает либо другой словарь или отображение, либо итерабельный объект, состоящий из итерабельных объектов –
# пар ключ-значение, либо именованные аргументы.  Добавляет соответствующие элементы в словарь,
# перезаписывая элементы с существующими ключами.
#
phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}

phonebook.update({'Alex': '832-438', 'Alice': '231-987'})
phonebook.update([('Joe', '217-531'), ('James', '783-428')])
phonebook.update(Carl='783-923', Victoria='386-486')
print(phonebook)

# d[key]
# получение значения с ключом key. Если такой ключ не существует
# # и отображение реализует специальный метод __missing__(self, key), то он
# # вызывается. Если ключ не существует и метод __missing__ не определён,
# # выбрасывается исключение KeyError.
#

phonebook ={
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}

try:
    print('Mary:', phonebook['Mary'])
    print('Lumberjack:', phonebook['Lumberjack'])
except KeyError as e:
    print('No entry for', *e.args)

# how many times each character occurred ib a st___:
text = 'Some long text'
counts = dict()
for c in text:
    key = c.lower().strip()
    if key:
        counts[key] = counts.get(key, 0)  + 1
print(counts)

# how many times each character occurred in a string:
#
# Suppose now that we just want a dictionary to track the uppercase, lowercase, and other characters in the string
# (i.e. kind of grouping the data by uppercase, lowercase, other) - again ignoring spaces:
import string

print(string.ascii_lowercase)
print(string.ascii_uppercase)

text = 'Some long text'

categories = {}
for c in text:
    if c != ' ':
        if c in string.ascii_lowercase:
            key = 'lower'
        elif c in string.ascii_uppercase:
            key = 'upper'
        else:
            key = 'other'
        if key not in categories:
            categories[key] = set()  # set we'll insert the value into

        categories[key].add(c)
for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))

# how many times each character occurred in a string:
# We can simplify this a bit using setdefault:
text = 'Some long text'

categories = {}
for c in text:
    if c != ' ':
        if c in string.ascii_lowercase:
            key = 'lower'
        elif c in string.ascii_uppercase:
            key = 'upper'
        else:
            key = 'other'
        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))

categories = {}
for c in text:
    if c != ' ':
        if c in string.ascii_lowercase:
            key = 'lower'
        elif c in string.ascii_uppercase:
            key = 'upper'
        else:
            key = 'other'
        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))

# how many times each character occurred in a string:
#
# Just to clean things up a but more, let's create a small utility function that will return the category key:
text = 'Some long text'

def cat_key(c):
    if c == ' ':
        return None
    elif c in string.ascii_lowercase:
        return 'lower'
    elif c in string.ascii_uppercase:
        return 'upper'
    else:
        return 'other'

categories = {}
for c in text:
    key = cat_key(c)
    if key:
        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))

# how many times each character occurred in a string:
#
# If you are not a fan of using if...elif... in the cat_key function we could do it this way as well
text = 'Some long text'

def cat_key(c):
    categories = {' ': None,
                 string.ascii_lowercase: 'lower',
                 string.ascii_uppercase: 'upper'}
    for key in categories:
        if c in key:
            return categories[key]
    else:
        return 'other'

cat_key('a'), cat_key('A'), cat_key('!'), cat_key(' ')

categories = {}
for c in text:
    key = cat_key(c)
    if key:
        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))


# In this example we have some dictionaries we use to configure our application. One dictionary specifies
# some configuration defaults for every configuration parameter our application will need.
# Another dictionary is used to configure some global configuration, and another set of dictionaries is used
# to define environment specific configurations, maybe dev and prod.
conf_defaults = dict.fromkeys(('host', 'port', 'user', 'pwd', 'database'), None)
print(conf_defaults)

conf_global = {
    'port': 5432,
    'database': 'deepdive'}

conf_dev = {
    'host': 'localhost',
    'user': 'test',
    'pwd': 'test'}


conf_prod = {
    'host': 'prodpg.deepdive.com',
    'user': '$prod_user',
    'pwd': '$prod_pwd',
    'database': 'deepdive_prod'}


# Now we can generate a full configuration for our dev environment this way:

config_dev = {**conf_defaults, **conf_global, **conf_dev}
print(conf_dev)

# and a config for our prod environment:

config_prod = {**conf_defaults, **conf_global, **conf_prod}
print(config_prod)

# defaultdict
# The defaultdict is a specialized dictionary found i_ the collections module. (It is a subclass of the dict type).

# Write a Python function that will create and r_ a dictionary from another dictionary, but sorted by value.
# You can assume the values are all comparable and have a natural sort order.
#
# composers _ {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}
#
#  instead of using a dictionary comprehension, we can simply use the dict()
#  function to create a dictionary from the sorted tuples!

composers = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}

def sort_dict_by_value(d):
    d = {k: v for k, v in sorted(d.items(), key = lambda el: el[1])}
    return d

print(sort_dict_by_value(composers))

def sort_dict_by_value(d):
    return dict(sorted(d.items(), key = lambda el: el[1]))

print(sort_dict_by_value(composers))