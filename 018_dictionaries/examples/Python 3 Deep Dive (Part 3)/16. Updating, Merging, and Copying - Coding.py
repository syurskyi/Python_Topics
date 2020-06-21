print('#' * 52 + ' Updating an existing keys value in a dictionary is straightforward: ')

d = {'a': 1, 'b': 2, 'c': 3}
d['b'] = 200
print(d)

print('#' * 52 + '  ')
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d1.update(d2)
print(d1)

print('#' * 52 + ' Note how the key order is maintained and based on the order in which the dictionaries were'
                 ' create/updated. ')

d1 = {'a': 1, 'b': 2}
d1.update(b=20, c=30)
print(d1)

print('#' * 52 + ' Again notice how the key order reflects the order in which the parameters were'
                 ' specified when calling the `update` method.  ')

d1 = {'a': 1, 'b': 2}
d1.update([('c', 2), ('d', 3)])
print(d1)

print('#' * 52 + ' Of course we can use more complex iterables. For example we could use a generator expression: ')
d = {'a': 1, 'b': 2}
d.update((k, ord(k)) for k in 'python')
print(d)

print('#' * 52 + '  ')
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 200, 'd': 4}
d1.update(d2)
print(d1)

print('#' * 52 + ' #### Unpacking dictionaries  ')

l1 = [1, 2, 3]
l2 = 'abc'
l = (*l1, *l2)
print(l)

print('#' * 52 + ' We can do something similar with dictionaries: ')

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d = {**d1, **d2}
print(d)

print('#' * 52 + ' Again note how order is preserved. What happens when there are conflicting keys in the unpacking? ')
d1 = {'a': 1, 'b': 2}
d2 = {'b': 200, 'c': 3}
d = {**d1, **d2}
print(d)

print('#' * 52 + '  ')
conf_defaults = dict.fromkeys(('host', 'port', 'user', 'pwd', 'database'), None)
print(conf_defaults)

print('#' * 52 + '  ')

conf_global = {
    'port': 5432,
    'database': 'deepdive'}

conf_dev = {
    'host': 'localhost',
    'user': 'test',
    'pwd': 'test'
}

conf_prod = {
    'host': 'prodpg.deepdive.com',
    'user': '$prod_user',
    'pwd': '$prod_pwd',
    'database': 'deepdive_prod'
}

config_dev = {**conf_defaults, **conf_global, **conf_dev}
print(config_dev)
config_prod = {**conf_defaults, **conf_global, **conf_prod}
print(config_prod)

print('#' * 52 + ' Another way dictionary unpacking can be really useful,'
                 ' is for passing keyword arguments to a function:  ')

def my_func(*, kw1, kw2, kw3):
    print(kw1, kw2, kw3)

d = {'kw2': 20, 'kw3': 30, 'kw1': 10}

print('#' * 52 + ' In this case, we dont really care about the order of the elements, since we will be'
                 ' unpacking keyword arguments: ')

print(my_func(**d))

print('#' * 52 + ' Of course we can even use it this way, but here the dictionary order does matter,'
                 ' as it will be reflected in the order in which those arguments are passed to the function: ')

def my_func(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

print(my_func(**d))

print('#' * 52 + ' #### Copying Dictionaries  ')
d = {'a': [1, 2], 'b': [3, 4]}
d1 = d.copy()
print(d)
print(d1)

print(id(d), id(d1), d is d1)

print('#' * 52 + '  ')
del d['a']
print(d)
print(d1)
d['b'] = 100
print(d)
print(d1)

print('#' * 52 + ' But lets see what happens if we mutate the value of one dictionary:  ')

d = {'a': [1, 2], 'b': [3, 4]}
d1 = d.copy()
print(d)
print(d1)

d['a'].append(100)
print(d)
print(d1)
print(d['a'] is d1['a'])

print('#' * 52 + ' So if we have nested dictionaries for example, as is often the case with JSON documents,'
                 ' we have to be careful when creating shallow copies. ')

d = {'id': 123445,
    'person': {
        'name': 'John',
        'age': 78},
     'posts': [100, 105, 200]
    }

d1 = d.copy()
d1['person']['name'] = 'John Cleese'
d1['posts'].append(300)
print(d1)
print(d)

print('#' * 52 + ' If we want to avoid this issue, we have to create a **deep** copy. '
                 ' We can easily do this ourselves using recursion, but the `copy` module implements such'
                 ' a function for us: ')

from copy import deepcopy
d = {'id': 123445,
    'person': {
        'name': 'John',
        'age': 78},
     'posts': [100, 105, 200]
    }

d1 = deepcopy(d)
d1['person']['name'] = 'John Cleese'
d1['posts'].append(300)
print(d1)
print(d)

print('#' * 52 + ' We saw earlier that we can also copy a dictionary by essentially unpacking the keys of one,'
                 ' or more dictionaries, into another.This also creates a **shallow** copy: ')

d1 = {'a': [1, 2], 'b':[3, 4]}
d = {**d1}
print(d)
d1['a'].append(100)
print(d1)
print(d)

print('#' * 52 + '  ')
from random import randint

big_d = {k: randint(1, 100) for k in range(1_000_000)}


def copy_unpacking(d):
    d1 = {**d}


def copy_copy(d):
    d1 = d.copy()


def copy_create(d):
    d1 = dict(d)


def copy_comprehension(d):
    d1 = {k: v for k, v in d.items()}

print('#' * 52 + '  ')
from timeit import timeit

print(timeit('copy_unpacking(big_d)', globals=globals(), number=100))
print(timeit('copy_copy(big_d)', globals=globals(), number=100))
print(timeit('copy_create(big_d)', globals=globals(), number=100))
print(timeit('copy_comprehension(big_d)', globals=globals(), number=100))