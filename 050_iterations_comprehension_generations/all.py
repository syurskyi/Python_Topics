# List Comprehensions A First Detailed Look

L = [1, 2, 3, 4, 5]

for i in range(len(L)):          # how to use range to change a list as we step across it
    L[i] += 10

print(L)

L = [x + 10 for x in L]          #list comprehension expression
print(L)


# List Comprehension Basics

L = [1, 2, 3, 4, 5]

L = [x + 10 for x in L]   #  list comprehension simply looks like a backward for loop.
print(L)


res = []
for x in L:
    res.append(x + 10)

print(res)

# Using List Comprehensions on Files

f = open('script1.py')
lines = f.readlines()
print(lines)

lines = [line.rstrip() for line in lines]
print(lines)


lines = [line.rstrip() for line in open('script1.py')]
print(lines)

print([line.upper() for line in open('script1.py')])

print([line.rstrip().upper() for line in open('script1.py')])

print([line.split() for line in open('script2.py')])

print([line.replace(' ', '!') for line in open('script2.py')])

print([('sys' in line, line[0]) for line in open('script1.py')])

# Extended List Comprehension Syntax

lines = [line.rstrip() for line in open('script2.py') if line[0] == 'p']
print(lines)

res = []
for line in open('script2.py'):
    if line[0] == 'p':
        res.append(line.rstrip())
print(res)


print([x + y for x in 'abc' for y in 'lmn'])

res = []
for x in 'abc':
    for y in 'lmn':
        res.append(x + y)
print(res)


# Iteration Contexts
# Use file iterators

for line in open('script2.py'):
    print(line.upper(), end='')

# Iteration Contexts
# Use List Comprehension

uppers = [line.upper() for line in open('script2.py')]
print(uppers)

# Iteration Contexts
# Use Map

print(map(str.upper, open('script1.py')))

# Iteration Contexts
# Use List and Map

print(list(map(str.upper, open('script2.py'))))

# Iteration Contexts
# Use Sorted

print(sorted(open('script2.py')))

# Iteration Contexts
# Use Zip

print(list(zip(open('script2.py'), open('script2.py'))))

# Iteration Contexts
# Use Enumerate

print(list(enumerate(open('script2.py'))))

# Iteration Contexts
# Use Filter

print(list(filter(bool, open('script2.py'))))

# Iteration Contexts
# Use Reduce

print(functools.reduce(operator.add, open('script2.py')))

# Iteration Contexts
# Use Sum

print(sum([3, 2, 4, 1, 5, 0]))

# Iteration Contexts
# Use Any

print(any(['spam', '', 'ni']))

# Iteration Contexts
# Use All

print(all(['spam', '', 'ni']))

# Iteration Contexts
# Use Max

print(max([3, 2, 5, 1, 4]))

# Iteration Contexts
# Use Min

print(min([3, 2, 5, 1, 4]))

# Iteration Contexts
# Use Max for file

print(max(open('script2.py')))

# Iteration Contexts
# Use Min for file

print(min(open('script2.py')))

# Iteration Contexts
# Use List for file
print(list(open('script2.py')))

# Iteration Contexts
# Use Tuple for file
print(tuple(open('script2.py')))

# Iteration Contexts
# Slice assignment
L = [11, 22, 33, 44]
L[1:3] = open('script2.py')
print(L)

# Iteration Contexts
# list.extend method
L = [11]
L.extend(open('script2.py'))
print(L)

# The range Iterable
R = range(10)
# range returns an iterator, not a list
print(R)
I = iter(R)
# Make an iterator from the range
print(next(I))  # Advance to next result
print(next(I))
print(next(I))
print(list(range(10)))  # To force a list if required

print(len(R))  # range also does len and indexing, but no others
print(R[0])
print(R[-1])

print(next(I))  # Continue taking from iterator, where left off
print(I.__next__())  # .next() becomes .__next__(), but use new next()

# The map  Iterable
M = map(abs, (-1, 0, 1))  # map returns an iterator, not a list
print(M)

print(next(M))  # Use iterator manually: exhausts results. hese do not support len() or indexing

print(next(M))

print(next(M))

# print(next(M))

for x in M: print(x)  # map iterator is now empty: one pass only

M = map(abs, (-1, 0, 1))  # Make a new iterator to scan again

for x in M: print(x)  # Iteration contexts auto call next()

print(list(map(abs, (-1, 0, 1))))  # Can force a real list if needed

# The zip Iterables
Z = zip((1, 2, 3), (10, 20, 30))  # zip is the same: a one-pass iterator

print(Z)

print(list(Z))

for pair in Z: print(pair)  # Exhausted after one pass

Z = zip((1, 2, 3), (10, 20, 30))

for pair in Z: print(pair)  # Iterator used automatically or manually

Z = zip((1, 2, 3), (10, 20, 30))
print(next(Z))
print(next(Z))

# The filter Iterables
print(filter(bool, ['spam', '', 'ni']))
print(list(filter(bool, ['spam', '', 'ni'])))

# Multiple Versus Single Pass Iterators
# Range

R = range(3)  # range allows multiple iterators

# print(next(R))                       # TypeError: range object is not an iterator

I1 = iter(R)
print(next(I1))
print(next(I1))

I2 = iter(R)  # Two iterators on one range
print(next(I2))

print(next(I1))  # I1 is at a different spot than I2

R = range(3)  # But range allows many iterators
I1, I2 = iter(R), iter(R)
print([next(I1), next(I1), next(I1)])

print(next(I2))  # Multiple active scans, like 2.X lists

# Multiple Versus Single Pass Iterators
# Zip

Z = zip((1, 2, 3), (10, 11, 12))

I1 = iter(Z)
I2 = iter(Z)  # Two iterators on one zip

print(next(I1))
print(next(I1))

print(next(I2))  # I2 is at same spot as I1!

# Multiple Versus Single Pass Iterators
# Map

M = map(abs, (-1, 0, 1))  # Ditto for map (and filter)
I1 = iter(M);
I2 = iter(M)
print(next(I1), next(I1), next(I1))

# next(I2)                              # (3.X) Single scan is exhausted! StopIteration

# Dictionary View Iterables

D = dict(a=1, b=2, c=3)
print(D)
K = D.keys()  # Views are not iterators themselves. TypeError: 'dict_keys' object is not an iterator
print(K)

# Dictionary View Iterables
# Views have an iterator
# which can be used manually
#  but does not support len(), index
# All iteration contexts use auto

from __future__ import print_function
D = dict(a=1, b=2, c=3)
K = D.keys()

I = iter(K)
print(next(I))
print(next(I))

for k in D.keys(): print(k, end=' ')

# Dictionary View Iterables
# Ditto for values() and items() views
#
#  Dictionaries still have own iterator, # Returns next key on each iteration
#
# Still no need to call keys() to iterate. But keys is an iterator in 3.0 too!

from __future__ import print_function
D = dict(a=1, b=2, c=3)
K = D.keys()
V = D.values()
print(V)
print(list(V))
print(list(D.items())
for (k, v) in D.items(): print(k, v, end=' ')
print()
print(D)

I = iter(D)
print(next(I))
print(next(I))

for key in D: print(key, end=' ')

# Dictionary View Iterables
# sorted


from __future__ import print_function

D = dict(a=1, b=2, c=3)
K = D.keys()
V = D.values()

for k in sorted(D.keys()): print(k, D[k], end=' ')
print()

print(D)

for k in sorted(D): print(k, D[k], end=' ')

# List Comprehensions Versus map

res = []
for x in 'spam':
    res.append(ord(x))  # Manual results collection

print(res)

res = list(map(ord, 'spam'))  # Apply function to sequence
print(res)

res = [ord(x) for x in 'spam']  # Apply expression to sequence
print(res)

print([x ** 2 for x in range(10)])

print(list(map((lambda x: x ** 2), range(10))))

# Adding Tests and Nested Loops - filter
# range(5)

print([x for x in range(5) if x % 2 == 0])

print(list(filter((lambda x: x % 2 == 0), range(5))))

res = []
for x in range(5):
    if
x % 2 == 0:
res.append(x)
print(res)

# Adding Tests and Nested Loops - filter
# range(10)

print([x ** 2 for x in range(10) if x % 2 == 0])

print(list(map((lambda x: x ** 2), filter((lambda x: x % 2 == 0), range(10)))))

# Adding Tests and Nested Loops - filter
#  for x in

res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
print(res)

res = []
for x in [0, 1, 2]:
    for
y in [100, 200, 300]:
res.append(x + y)
print(res)

print([x + y for x in 'spam' for y in 'SPAM'])

# Adding Tests and Nested Loops - filter
# for x in range(5)

print([(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1])

res = []
for x in range(5):
    if
x % 2 == 0:
for y in range(5):
    if
y % 2 == 1:
res.append((x, y))
print(res)

# Why You Will Care List Comprehensions and map
print(open('myfile').readlines())

print([line.rstrip() for line in open('myfile').readlines()])

print([line.rstrip() for line in open('myfile')])

print(list(map((lambda line: line.rstrip()), open('myfile'))))

listoftuple = [('bob', 35, 'mgr'), ('mel', 40, 'dev')]

print([age for (name, age, job) in listoftuple])

print(list(map((lambda row: row[1]), listoftuple)))

# Generator Functions and Expressions


def gensquares(N):
    for i in range(N):
        yield i ** 2  # Resume here later


for i in gensquares(5):  # Resume the function
    print(i, end=' : ')  # # Print last yielded value

print()
x = gensquares(4)
print(x)

print(next(x))  # Same as x.__next__() in 3.0

print(next(x))  # Use x.next() or next() in 2.6
print(next(x))
print(next(x))

# Generator Functions and Expressions
#  Returns a generator which is its own iterator
def gensquares(N):
    for i in range(N):
        yield i ** 2


y = gensquares(5)  # Returns a generator which is its own iterator

print(iter(y) is y)  # iter() is not required: a no-op here

print(next(y))  # Can run next()immediately

# Generator Functions and Expressions
# def buildsquares(n):

def buildsquares(n):
    res = []
    for i in range(n): res.append(i ** 2)
    return res


for x in buildsquares(5): print(x, end=' : ')
print()

for x in [n ** 2 for n in range(5)]: print(x, end=' : ')

print()

for x in map((lambda n: n ** 2), range(5)): print(x, end=" : ")

# Generator Functions and Expressions
# def  ups()
def ups(line):
    for sub in line.split(','):  # Substring generator
        yield sub.upper()


print(tuple(ups('aaa,bbb,ccc')))  # All iteration contexts)

print({i: s for (i, s) in enumerate(ups('aaa,bbb,ccc'))})

# Generator expressions versus map
#  Map function on tuple
#  Generator expression
#  Nonfunction case
# Simpler as generator?

print(list(map(abs, (-1, -2, 3, 4))))  # Map function on tuple

print(list(abs(x) for x in (-1, -2, 3, 4)))  # Generator expression

print(list(map(lambda x: x * 2, (1, 2, 3, 4))))  # Nonfunction case

print(list(x * 2 for x in (1, 2, 3, 4)))  # Simpler as generator?


# Generator expressions versus map
# using (''.join
#  Makes a pointless list
#  Generates results
# Generates results
# impler as generator?

line = 'aaa,bbb,ccc'

print(''.join([x.upper() for x in line.split(',')]))  # Makes a pointless list

print(''.join(x.upper() for x in line.split(',')))  # Generates results

print(''.join(map(str.upper, line.split(','))))  # Generates results

print(''.join(x * 2 for x in line.split(',')))  # Simpler as generator?

print(''.join(map(lambda x: x * 2, line.split(','))))

# Generator expressions versus map
# [x * 2 for x in [abs(x)
#  Nested comprehensions
# Nested maps
# Nested generators
# Nested combinations

print([x * 2 for x in [abs(x) for x in (-1, -2, 3, 4)]])  # Nested comprehensions

print(list(map(lambda x: x * 2, map(abs, (-1, -2, 3, 4)))))  # Nested maps

print(list(x * 2 for x in (abs(x) for x in (-1, -2, 3, 4))))  # Nested generators

import math

print(list(map(math.sqrt, (x ** 2 for x in range(4)))))  # Nested combinations

# Generator expressions versus filter
# (''.join(x for x in line.split()
#  Generator with 'if'
#  Similar to filter using lambda


line = 'aa bbb c'

print(''.join(x for x in line.split() if len(x) > 1))  # Generator with 'if'

print(''.join(filter(lambda x: len(x) > 1, line.split())))  # Similar to filter

print(''.join(x.upper() for x in line.split() if len(x) > 1))

print(''.join(map(str.upper, filter(lambda x: len(x) > 1, line.split()))))

print(''.join(x.upper() for x in line.split() if len(x) > 1))

print()

res = ''
for x in line.split():
    if len(x) > 1:
        res += x.upper()
print(res)

# Generator Functions Versus Generator Expressions
# Generator expression
# Force generator to produce all results
# Generator function
# Iterate automatically
# Iterate manually


G = (c * 4 for c in 'SPAM')  # Generator expression

print(list(G))  # Force generator to produce all results


def timesfour(S):  # Generator function
    for c in S:
        yield c * 4


G = timesfour('spam')
print(list(G))  # Iterate automatically

G = (c * 4 for c in 'SPAM')
I = iter(G)  # Iterate manually
print(next(I))
print(next(I))

G = timesfour('spam')
I = iter(G)
print(next(I))
print(next(I))

# Generator Functions Versus Generator Expressions
# Function def gensub(line): or
# (''.join(x.upper()  Expression

line = 'aa bbb c'
print(''.join(x.upper() for x in line.split() if len(x) > 1))  # Expression


def gensub(line):  # Function
    for x in line.split():
        if len(x) > 1:
            yield x.upper()


print(''.join(gensub(line)))  # But why generate?

# Generators Are Single-Iteration Objects
# My iterator is myself: G has __next__
# Iterate manually
# Second iterator at same position!
# Collect the rest of I1's items
# Other iterators exhausted too StopIteration
# Ditto for new iterators
# New generator to start over

G = (c * 4 for c in 'SPAM')
print(iter(G) is G)  # My iterator is myself: G has __next__
True

G = (c * 4 for c in 'SPAM')  # Make a new generator
I1 = iter(G)  # Iterate manually
print(next(I1))
print(next(I1))

I2 = iter(G)  # Second iterator at same position!
print(next(I2))

print(list(I1))  # Collect the rest of I1's items
# print(next(I2))                            # Other iterators exhausted too StopIteration

I3 = iter(G)  # Ditto for new iterators
# print(next(I3))                          # StopIteration

I3 = iter(c * 4 for c in 'SPAM')  # New generator to start over
print(next(I3))

# Generators Are Single-Iteration Objects
# Generator functions work the same way
# like generator expression

def timesfour(S):
    for c in S:
        yield c * 4


G = timesfour('spam')  # Generator functions work the same way

print(iter(G) is G)

I1, I2 = iter(G), iter(G)

print(next(I1))
print(next(I1))
print(next(I2))  # I2 at same position as I1

# Generators Are Single-Iteration Objects
# Lists support multiple iterators
#  Changes reflected in iterators

L = [1, 2, 3, 4]

I1, I2 = iter(L), iter(L)

print(next(I1))
print(next(I1))  # Lists support multiple iterators
print(next(I2))

del L[2:]  # Changes reflected in iterators

# print(next(I1))                     # StopIteration

# The Python 3.3 yield from Extension
# def both(N)

def both(N):
    for i in range(N): yield i
    for i in (x ** 2 for x in range(N)): yield i


print(both(5))
print(list(both(5)))


def both(N):
    yield from range(N)
    yield from (x ** 2 for x in range(N))


print(list(both(5)))

print(' : '.join(str(i) for i in both(5)))

# Generators and function application
# Normal positionals
#  Unpack range values: iterable in 3.X
#  Unpack generator expression values

def f(a, b, c): print('%s, %s, and %s' % (a, b, c))


f(0, 1, 2)  # Normal positionals

f(*range(3))  # Unpack range values: iterable in 3.X

f(*(i for i in range(3)))

# Generators and function application
# dict
# Normal keywords
# Unpack dict: key=value
# Unpack keys iterator
# Unpack view iterator: iterable in 3.X

D = dict(a='Bob', b='dev', c=40.5)

print(D)

f(a='Bob', b='dev', c=40.5)  # Normal keywords

f(**D)  # Unpack dict: key=value

f(*D)  # Unpack keys iterator

f(*D.values())

# Generators and function application
# for x in 'spam':

for x in 'spam': print(x.upper(), end=' ')
print()

list(print(x.upper(), end=' ') for x in 'spam')
print()

print(*(x.upper() for x in 'spam'))

# Comprehension Syntax Summary
# List comprehension: builds list

print([x * x for x in range(10)])

# Comprehension Syntax Summary
# Generator expression: produces items
# Parens are often optional

print((x * x for x in range(10)))

# Comprehension Syntax Summary
# Set comprehension, new in 3.0, {x, y} is a set in 3.0 too

print({x * x for x in range(10)} )

# Comprehension Syntax Summary
# Dictionary comprehension

print({x: x * x for x in range(10)})

# Comprehending Set and Dictionary Comprehensions
# Comprehension
# Generator and type name
#  Set comprehension equivalent
# Dict comprehension equivalent

print({x * x for x in range(10)})
set(x * x for x in range(10))
print({x: x * x for x in range(10)})
print(dict((x, x * x) for x in range(10)))

res = set()
for x in range(10):
    res.add(x * x)
print(res)

res = {}
for x in range(10):
    res[x] = x * x

print(res)

# Notice that although both forms accept iterators, they have no notion of generating
# results on demand—both forms build objects all at once. If you mean to produce keys
# and values upon request, a generator expression is more appropriate:

G = ((x, x * x) for x in range(10))
print(next(G))

print(next(G))

# Extended Comprehension Syntax for Sets and Dictionaries
# Lists are ordered
# But sets are not
# Neither are dict keys
# Lists keep duplicates
#  But sets do not
# Neither do dict keys

print([x * x for x in range(10) if x % 2 == 0])
print({x * x for x in range(10) if x % 2 == 0})
print({x: x * x for x in range(10) if x % 2 == 0})
print([x + y for x in [1, 2, 3] for y in [4, 5, 6]])
print({x + y for x in [1, 2, 3] for y in [4, 5, 6]})
print({x: y for x in [1, 2, 3] for y in [4, 5, 6]})

# Примеры некоторых стандартных итерабельных объектов.
# список

my_list = [1, 2, 5, 7, 32, 148]

# Обход списка
for element in my_list:
    print(element)


# Функция enumerate возвращает итерабельный объект, который возвращает пары индекс-значение
for index, element in enumerate(my_list):
    print('my_list[{}] = {}'.format(index, element))




# Примеры некоторых стандартных итерабельных объектов.
# строка

string = 'A string'
# Обход строки посимвольно
for char in string:
    print(char)

# Create my function ,my_for

#
#

def my_for(iterable, callback):
    it = iter(iterable)
    while True:
        try:
            value = next(it)
            callback(value)
        except StopIteration:
            break

def loop_body(value):
    print('Next value received:', value)

my_for(range(10), loop_body)

# Примеры некоторых стандартных итерабельных объектов.
#  диапазон

# В Python 3 range -- это итерабельный объект, который задаёт диапазон.
# В Python 2 для этого служит xrange, а range является функцией,
# которая возвращает список.

my_range = range(2, 17, 2)

for counter in my_range:
    print(counter)

# iterable_with_getitem

# Итерабельные объекты должны реализовывать как минимум один из двух методов:
# -  __iter__(self)
# -  __getitem__(self, key)
#
# Метод __iter__ возвращает объект - итератор(будет рассмотрен далее).
# Метод __getitem__ возвращает элемент контейнера по ключу или индексу.
# Встроенная фукнция iter(автоматически вызывается циклом for ) вызывает метод __iter__, если он существует.Иначе, если
# существует метод __getitem__, то автоматически создаётся итератор, который вызывает метод __getitem__ с
# возрастающими индексами, начиная от нуля, до возникновения исключения IndexError.Если объект не реализовавает ни один из
# этих методов, то данный объект не является итерабельным и выбрасывается исключение TypeError.


class SimpleIterable(object):
    """Класс итерабельного объекта с методом __getitem__"""

    def __getitem__(self, index):
        if 0 <= index < 5:
            return index * 2
        else:
            raise IndexError('iterable index out of range')


# Создание объекта
iterable = SimpleIterable()

# Вывод некоторых значений
print('iterable[0] =', iterable[0])
print('iterable[3] =', i)

# list_iterator
# Функция обхода итерабельного объекта

# Итератор (iterator) – это объект, который представляет поток данных.
# Повторяемые вызовы метода __next__() (next() в Python 2) итератора
# или передача его встроенной функции next() возвращает последующие
# элементы потока.
#
# Если больше не осталось данных, выбрасывается исключение StopIteration.
# После этого итератор исчерпан и любые последующие вызовы его метода __next__()
# снова генерируют исключение StopIteration.
#
# Итераторы обязаны иметь метод __iter__, который возвращает сам объект итератора.
# Таким образом, любой итератор сам по себе также является итерабельным объектом.


def traverse(iterable):
    print('Traversing {}:'.format(type(iterable).__name__))
    for element in iterable:
        print(element)
    print()


# Объявление списка
my_list = [1, 2, 3, 5, 8]

# Получение его итератора
list_iterator = iter(my_list)

# Обход списка
traverse(my_list)

# Обход итератора списка
traverse(list_iterator)

# Очередной обход списка -- работает корректно, так как создаётся
# новый объект-итератор
traverse(my_list)

# Очередной обход итератора -- не выводится ничего, так как
# эле






# range-generator
def my_range(first, second=None, step=1):
    """Функция-генератор, работающая подобно стандартному классу range"""

    if second is None:
        current = 0
        end = first
    else:
        current = first
        end = second

    if step == 0:
        raise ValueError('step must not be zero')

    while (step > 0 and current < end) or (step < 0 and current > end):
        # yield выдаёт текущее значение и приостанавливает работу генератора.
        # При следующем вызове next выполнение продолжится с этого места.
        yield current
        current += step


# fibonacci-sequence
def fibonacci(max_count):
    """Генерация max_count чисел Фибоначчи"""
    count = 0
    first, second = 0, 1

    while count < max_count:
        count += 1
        yield second
        first, second = second, first + second


def main():
    # Вывод 15 первых чисел Фибоначчи
    for number in fibonacci(15):
        print(number)


if __name__ == '__main__':
    main()

# generator-expressions

# Некоторые простые генераторы могут быть записаны в виде выражения.
# Они выглядят как выражение, содержащее некоторые переменные, после
# которого одно или несколько ключевых слов for, задающих, какие значения
# должны принимать данные переменные (синтаксис соответствует заголовку
#     цикла for), и ноль или несколько условий, фильтрующих генерируемые
# значения (синтаксис соответствует заголовку оператора if). Такие выражения
# называются выражениями-генераторами (generator expressions).
#
generator = (x ** 2 + y for x in range(2, 7) for y in range(3) if x != 6)
for number in generator:
    print(number)

print()

print(sum(2 * x for x in range(5)))

# delegating-to-subgenerator

# В Python 3 существуют так называемые подгенераторы (subgenerators).
# Если в функции-генераторе встречается пара ключевых слов yield from,
# после которых следует объект-генератор, то данный генератор делегирует
# доступ к подгенератору, пока он не завершится (не закончатся его значения),
# после чего продолжает своё исполнение.
#
#
def generator():
    yield from (3 * x for x in range(5))
    yield from (2 * x for x in range(5, 10))


for i in generator():
    print(i)

# producer-consumer-coroutines

# """
# Сопрограмма (англ. coroutine) — компонент программы, обобщающий понятие
# подпрограммы, который дополнительно поддерживает множество входных точек
# (а не одну, как подпрограмма) и остановку и продолжение выполнения с
# сохранением определённого положения.

# Rolling our own Next method

class Squares:
    def __init__(self):
        self.i = 0

    def next_(self):
        result = self.i ** 2
        self.i += 1
        return result


sq = Squares()
sq.next_()
sq.next_()

for i in range(10):
    print(sq.next_())

# Rolling our own Next method
# mplement a __len__ method to support the len() function

class Squares:
    def __init__(self, length):
        self.length = length
        self.i = 0

    def next_(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

    def __len__(self):
        return self.length

sq = Squares(3)
len(sq)
sq.next_()
sq.next_()
sq.next_()
#
# So now, we can essentially loop over the collection in a very similar way to how we did it with sequences and the __getitem__ method:
#
sq = Squares(5)
while True:
    try:
        print(sq.next_())
    except StopIteration:
        # reached end of iteration
        # stop looping
        break

# Iterating Collections
# class RandomNumbers:

import random

class RandomNumbers:
    def __init__(self, length, *, range_min=0, range_max=10):
        self.length = length
        self.range_min = range_min
        self.range_max = range_max
        self.num_requested = 0

    def __len__(self):
        return self.length

    def __next__(self):
        if self.num_requested >= self.length:
            raise StopIteration
        else:
            self.num_requested += 1
            return random.randint(self.range_min, self.range_max)


numbers = RandomNumbers(10)
len(numbers)

while True:
    try:
        print(next(numbers))
    except StopIteration:
        break

# We still cannot use a for loop, and if we want to 'restart' the iteration, we have to create a new object every time.
#
numbers = RandomNumbers(10)

for item in numbers:
    print(item) #error


# Iterators and Iterables
# build class Cities

class Cities:
    def __init__(self):
        self._cities = ['New York', 'Newark', 'New Delhi', 'Newcastle']
    def __len__(self):
        return len(self._cities)
    def __getitem__(self, s):
        print('getting item...')
        return self._cities[s]
    def __iter__(self):
        print('Calling Cities instance __iter__')
        return self.CityIterator(self)
    class CityIterator:
        def __init__(self, city_obj):
            # cities is an instance of Cities
            print('Calling CityIterator __init__')
            self._city_obj = city_obj
            self._index = 0
        def __iter__(self):
            print('Calling CitiyIterator instance __iter__')
            return self
        def __next__(self):
            print('Calling __next__')
            if self._index >= len(self._city_obj):
                raise StopIteration
            else:
                item = self._city_obj._cities[self._index]
                self._index += 1
                return item
# cities = Cities()
# cities[0]
# next(iter(cities))
# cities = Cities()
# for city in cities:


# Python Built-In Iterables and Iterators
# for the list
#
# Since the list l is an iterable it also implements the __iter__ method:
# Of course, since lists are also sequence types, they also implement the __getitem__ method:

l = [1, 2, 3]
iter_l = iter(l)
#or could use iter_1 = l.__iter__()
type(iter_l)
next(iter_l)
next(iter_l)
next(iter_l)

'__iter__' in dir(l)
'__getitem__' in dir(l)

# But what does the iterator for a dictionary actually return?
#
# To iterate over the values, we could use the values() method which returns an iterable over the values of the dictionary:
#
# And to iterate over both the keys and values, dictionaries provide an items() iterable:

d = dict(a=1, b=2, c=3)
iter_d = iter(d)
next(iter_d)

# Dictionary iterators will iterate over the keys of the dictionary.

iter_vals = iter(d.values())
next(iter_vals)

iter_items = iter(d.items())
next(iter_items)

# Cyclic Iterators

class CyclicIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.lst[self.i % len(self.lst)]
        self.i += 1
        return result

iter_cycl = CyclicIterator('NSWE')

for i in range(10):
    print(next(iter_cycl))
#
n = 10
iter_cycl = CyclicIterator('NSWE')
for i in range(1, n+1):
    direction = next(iter_cycl)
    print(f'{i}{direction}')

# And re-working this into a list comprehension:
#
n = 10
iter_cycl = CyclicIterator('NSWE')
[f'{i}{next(iter_cycl)}' for i in range(1, n+1)]
#
# Of course, there's an easy alternative way to do this as well, using: repetition, zip
# a list comprehension

n = 10
list(zip(range(1, n+1), 'NSWE' * (n//4 + 1)))

# There's actually an even easier way yet, and that's to use our CyclicIterator, but instead of building it ourselves, we can simply use the one provided by Python in the standard library!!

import itertools
n = 10
iter_cycl = CyclicIterator('NSWE')
[f'{i}{next(iter_cycl)}' for i in range(1, n+1)]

n = 10
iter_cycl = i




# Lazy Iterables

# Lazy evaluation is when evaluating a value is deferred until it is actually requested.



# Simple examples of lazy evaluation are often seen in classes for calculated properties.
#
# As you can see, in this circle class, every time we set the radius, we re-calculate and store the area.
# When we request the area of the circle, we simply return the stored value.

import math


class Circle:
    def __init__(self, r):
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self.area = math.pi * r ** 2


c = Circle(1)
c.area
c.radius = 2
c.radius, c.area

# Simple examples of lazy evaluation are often seen in classes for calculated properties.
#
# But instead of doing it this way, we could just calculate the area every time
# it is requested without actually storing the value

class Circle:
    def __init__(self, r):
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r

    @property
    def area(self):
        return math.pi * self.radius ** 2


c = Circle(1)
c.area
c.radius = 2
c.area


# Simple examples of lazy evaluation are often seen in classes for calculated properties.

class Circle:
    def __init__(self, r):
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None

    @property
    def area(self):
        if self._area is None:
            print('Calculating area...')
            self._area = math.pi * self.radius ** 2
        return self._area


c = Circle(1)
c.area
c.area
c.radius = 2
c.area

# Python's Built-In Iterables and Iterators
# Let's look at the simple range function first:
#
# But it is not an iterator:
#
# However, we can request an iterator by calling the __iter__ method, or simply using the iter() function:
#
# And of course this is now an iterator:

r_10 = range(10)
'__iter__' in dir(r_10)

'__next__' in dir(r_10)

r_10_iter = iter(r_10)

'__iter__' in dir(r_10_iter)

'__next__' in dir(r_10_iter)


# Python's Built-In Iterables and Iterators
# zip
# Just like range() though, it also uses lazy evaluation, so we need to iterate through the iterator and make a list
# for example in order to see the contents:
#
# Even reading a file line by line is done using lazy evaluation:
#
# As you can see, the open() function returns an iterator (of type TextIOWrapper), and we can read lines from the file
# one by one using the next() function, or calling the __next__() method. The class also implements a readline()
# method we can use to get the next row:

z = zip([1, 2, 3], 'abc')
z
print('__iter__' in dir(z))
print('__next__' in dir(z))

list(z)

with open('cars.csv') as f:
    print(type(f))
    print('__iter__' in dir(f))
    print('__next__' in dir(f))

with open('cars.csv') as f:
    print(next(f))
    print(f.__next__())
    print(f.readline())

# Python's Built-In Iterables and Iterators
# The enumerate function is another lazy iterator:
#
# As we can see, the object and its iterator are the same object.
#
# But enumerate is also lazy, so we need to iterate through it in order to recover all the elements:
# Of course, once we have exhausted the iterator, we cannot use it again:

e = enumerate('Python rocks!')

print('__iter__' in dir(e))
print('__next__' in dir(e))

iter(e)
e
list(e)
list(e)

# Python's Built-In Iterables and Iterators
# The dictionary object provides methods that return iterables for the keys, values or tuples of key/value pairs:
#
# More simply, we can just test to see if iter(keys) is the same object as keys - if not then we are dealing with an iterable.

d = {'a': 1, 'b': 2}
keys = d.keys()
'__iter__' in dir(keys), '__next__' in dir(keys)
iter(keys) is keys

# The iter() Function
# As we have seen before, the iter() function is used to request an iterator object from an iterable
# And we can use that iterator to iterate the collection by calling next() until a StopIteration exception is raised.

l = [1, 2, 3, 4]
l_iter = iter(l)
type(l_iter)
next(l_iter)
next(l_iter)

# The iter() Function
# class Squares with __getitem__

class Squares:
    def __init__(self, n):
        self._n = n

    def __len__(self):
        return self._n

    def __getitem__(self, i):
        if i >= self._n:
            raise IndexError
        else:
            return i ** 2


for i in sq:
    print(i)

sq_iter = iter(sq)
type(sq_iter)
'__next__' in dir(sq_iter)


# How to test if an object is iterable

# Basically an object is iterable if it:
#
#     implements the iterable protocol (__iter__ that returns an iterator)
#     implements the sequence protocol (__getitem__, and __len__) - although __len__ is not required for iteration

#  the best way, if you have some need to detect if something is iterable or not, is the following:

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

is_iterable(SimpleIter())
is_iterable(Squares(5))

# In this example we are going to create a counter function (using a closure) - it's a pretty simplistic function -
# counter() will return a closure that we can then call to increment an internal counter by 1 every time it is called:

def counter():
    i = 0

    def inc():
        nonlocal i
        i += 1
        return i

    return inc


cnt = counter()
cnt()
cnt()

# you may want to iterater through random numbers until a specific random number is generated:

import random
random.seed(0)
for i in range(10):
    print(i, random.randint(0, 10))

random_iterator = iter(lambda : random.randint(0, 10), 8)

random.seed(0)

for num in random_iterator:
    print(num)

#  try a countdown example like the one we discussed in the lecture.
def countdown(start=10):
    def run():
        nonlocal start
        start -= 1
        return start
    return run

takeoff = countdown(10)
for _ in range(15):
    print(takeoff())

takeoff  = countdown(10)
takeoff_iter = iter(takeoff, -1)
for val in takeoff_iter:
    print(val)

# Delegating Iterators
#
# Technically we can see the underlying data by accessing the (pseudo) private variable _persons.
#
# But we really would prefer making our PersonNames instances iterable.
#
# To do so we need to implement the __iter__ method that returns an iterator that can be used for iterating over the _persons list.
#
# And of course we can sort, use list comprehensions, and so on - our PersonNames is an iterable.

from collections import namedtuple
Person = namedtuple('Person', 'first last')
class PersonNames:
    def __init__(self, persons):
        try:
            self._persons = [person.first.capitalize()
                             + ' ' + person.last.capitalize()
                            for person in persons]
        except (TypeError, AttributeError):
            self._persons = []

persons = [Person('michaeL', 'paLin'), Person('eric', 'idLe'),
           Person('john', 'cLeese')]

person_names = PersonNames(persons)
person_names._persons
class PersonNames:
    def __init__(self, persons):
        try:
            self._persons = [person.first.capitalize()
                             + ' ' + person.last.capitalize()
                            for person in persons]
        except TypeError:
            self._persons = []
    def __iter__(self):
        return iter(self._persons)
persons = [Person('michaeL', 'paLin'), Person('eric', 'idLe'),
           Person('john', 'cLeese')]
person_names = PersonNames(persons)
for p in person_names:
    print(p)

# yield statement

# The yield statement is used almost like a return statement in a function - but there is a huge difference -
# when the yield statement is encountered, Python returns whatever value yield specifies,
# but it "pauses" execution of the function. We can then "call" the same function again and it will "resume"
# from where the last yield was encountered.

# yield statement simple example
# And in fact that's exactly what Python generators are - they are iterators.
# If generators are iterators, they should implement the iterator protocol.
#
# And so we just have an iterator, which we can use with the iter() function and the next() function like any other iterator:

def my_func():
    print('line 1')
    yield 'Flying'
    print('line 2')
    yield 'Circus'

my_func()
gen_my_func = my_func()
next(gen_my_func)
next(gen_my_func)
# And let's call it one more time:
next(gen_my_func) # error

gen_my_func = my_func()
'__iter__' in dir(gen_my_func)
'__next__' in dir(gen_my_func)

gen_my_func
iter(gen_my_func)

# Yielding and Generators
# create def squares(sentinel):
# without error

def squares(sentinel):
    i = 0
    while True:
        if i < sentinel:
            yield i**2
            i += 1 # note how we can incremenet **after** the yield
        else:
            return 'all done!'

for num in squares(5):
    print(num)

# Yielding and Generators
#
# So now let's see how we could re-write our initial factorial example:

def factorials(n):
    for i in range(n):
        yield math.factorial(i)

for num in factorials(5):
    print(num)

facts = factorials(5)
list(facts)
list(facts)
next(facts) # error

# Making an Iterable from a Generator
#
# As we now know, generators are iterators.
# This means that they become exhausted - so sometimes we want to create an iterable instead.
#
# But, sq was an iterator - so now it's been exhausted:
#
# To restart the iteration we have to create a new instance of the generator (iterator):

def squares_gen(n):
    for i in range(n):
        yield i ** 2

sq = squares_gen(5)

for num in sq:
    print(num)

next(sq)

sq = squares_gen(5)
[num for num in sq]

# Generators used with other Generators
# Now enumerate is lazy, so sq had not, at this point, been consumed:
#
# Since we have consumed two elements from sq, when we now use enumerate it will have two less elements from sq:

def squares(n):
    for i in range(n):
        yield i ** 2

sq = squares(5)
enum_sq = enumerate(sq)

next(sq)
next(sq)

next(enum_sq)

# Generator Expressions
# Recall how list comprehensions worked:
#
# We can easily create a generator by using () parentheses instead of the [] brackets:
#
# Note that g is a generator, and is also lazily evaluated:

l = [i ** 2 for i in range(5)]
l
# The expression inside the [] brackets is called a comprehension expression.

g = (i ** 2 for i in range(5))

type(g)

for item in g:
    print(item)

# Generator Expressions
#
# We can iterate over the same list comprehension multiple times, since it is an iterable.
# However, we can only iterate over a comprehension expression once, since it is an iterator.

l = [i * 2 for i in range(5)]
type(l)

g = (i ** 2 for i in range(5))
type(g)

# Nested Comprehensions
#
# Just as with list comprehensions, we can nest generator expressions too:
#
# A multiplication table:
# Using a list comprehension approach first:
#
# The equivalent generator expression would be:
#
# We can iterate through mult_list:
#
# But you'll notice that our rows are themselves generators!
# o fully materialize the table we need to iterate through the row generators too:

start = 1
stop = 10

mult_list = [ [i * j
               for j in range(start, stop+1)]
             for i in range(start, stop+1)]

mult_list

start = 1
stop = 10

mult_list = ( (i * j
               for j in range(start, stop+1))
             for i in range(start, stop+1))

mult_list

table = list(mult_list)
table

table_rows = [list(gen) for gen in table]
table_rows

# Nested Comprehensions
#
# Of course, we can mix list comprehensions and generators.
#
# In this modification, we'll make the rows list comprehensions, and retain the generator expression in the outer comprehension:
#
# Notice what is happening here, the table itself is lazy evaluated, i.e. the rows are not yielded until they
# are requested - but once a row is requested, the list comprehension that defines the row will be entirely
# evaluated at that point:

start = 1
stop = 10

mult_list = ( [i * j
               for j in range(start, stop+1)]
             for i in range(start, stop+1))

for item in mult_list:
    print(item)

# Let's try Pascal's triangle again:
# Here's how we did it using a list comprehension:

from math import factorial

def combo(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

size = 10  # global variable
pascal = [ [combo(n, k) for k in range(n+1)] for n in range(size+1) ]

# Let's try Pascal's triangle again:
#
# If we want to materialize the triangle into a list we'll need to do so ourselves:

size = 10  # global variable
pascal = ( (combo(n, k) for k in range(n+1)) for n in range(size+1) )

[list(row) for row in pascal]

# Yield From
# Suppose we want an iterator to iterate over all the values of the matrix, element by element.
#
# All we have done here is create a generator (iterator) that can be used to iterate of the elements of a nested iterator.

def matrix_iterator(n):
    for row in matrix(n):
        for item in row:
            yield item

for i in matrix_iterator(3):
    print(i)

# Yield From
# But we can avoid using that nested for loop by using a special form of yield: yield from

def matrix_iterator(n):
    for row in matrix(n):
        yield from row

for i in matrix_iterator(3):
    print(i)

# Yield From
#
# we need to read car brands from multiple files to get it as a single collection.

def brands(*files):
    for f_name in files:
        with open(f_name) as f:
            yield from f

files = 'car-brands-1.txt', 'car-brands-2.txt', 'car-brands-3.txt'

for brand in brands(*files):
    print(brand, end=', ')

# Yield From
#
# we are going to create generators that can read each line of the file, and yield a clean result, and we'll yield from that generator:
#
# As you can see, this generator function will clean each line of the file before yielding it. Let's try it with a single file and make sure it works:
#
# So now, we can proceed with our overarching generator function as before, except we'll yield from our generators, instead of directly from the file iterator:
#
# I want to point out that in this particular instance, we are using yield from as a simple replacement for a for loop

def gen_clean_read(file):
    with open(file) as f:
        for line in f:
            yield line.strip('\n')

f1 = gen_clean_read('car-brands-1.txt')
for line in f1:
    print(line, end=', ')

files = 'car-brands-1.txt', 'car-brands-2.txt', 'car-brands-3.txt'

def brands(*files):
    for file in files:
        yield from gen_clean_read(file)

for brand in brands(*files):
    print(brand, end=', ')

# Aggregators
#
# Suppose we want to test if an iterable contains only numeric values.
#
# First, we need to figure out how we determine if something is a number.

l = [10, 20, 30, 40]

is_all_numbers = True
for item in l:
    if not isinstance(item, Number):
        is_all_numbers = False
        break
print(is_all_numbers)

l = [10, 20, 30, 40, 'hello']

is_all_numbers = True
for item in l:
    if not isinstance(item, Number):
        is_all_numbers = False
        break
print(is_all_numbers)

# Aggregator
#
# Suppose we have a file and we want to make sure that all the rows in the file have length > some number.
#
# We can easily test to make sure that every brand in our file is at least 3 characters long:
#
# And we can test to see if any line is more than 10 characters:
#
# More than 13?
#
# Of course, we can also do this using generator expressions instead of map:

with open('car-brands.txt') as f:
    for row in f:
        print(len(row), row, end='')

with open('car-brands.txt') as f:
    result = all(map(lambda row: len(row) >= 3, f))
print(result)

with open('car-brands.txt') as f:
    result = any(map(lambda row: len(row) > 10, f))
print(result)

with open('car-brands.txt') as f:
    result = any(map(lambda row: len(row) > 13, f))
print(result)

with open('car-brands.txt') as f:
    result = any(len(row) > 13 for row in f)
print(result)

# Slicing Iterables
# We know that sequence types can be sliced:
#
# Equivalently we can use the slice object:

l = [1, 2, 3, 4, 5]
l[0:2]

s = slice(0, 2)
l[s]

# Selecting and Filtering Iterators
#
# Remember that the filter function can work with any iterable, including of course iterators and generators.
#
# Now let's say we only want to use cubes that are odd.
#
# We need a function that will return a True if the number is odd, False otherwise. (This is technically called a predicate by the way - any function that given an input returns True or False is called a predicate)
#
# Let's make sure the function works as expected:
#
# Now we can use that function (or we could have just used a lambda as well) with the filter function.
#
# Note that the filter function is also lazy.

def gen_cubes(n):
    for i in range(n):
        print(f'yielding {i}')
        yield i**3

def is_odd(x):
    return x % 2 == 1

is_odd(4), is_odd(81)

filtered = filter(is_odd, gen_cubes(10))

list(filtered)


# Selecting and Filtering Iterators
#
# e could use the filterfalse function in the itertools module that does the same work as filter but retains values w
# here the predicate is False (instead of True as the filter function does).

from itertools import filterfalse

def gen_cubes(n):
    for i in range(n):
        print(f'yielding {i}')
        yield i**3

def is_odd(x):
    return x % 2 == 1

evens = filterfalse(is_odd, gen_cubes(10))

# No print output --> lazy evaluation

list(evens)

# Infinite Iterators
# The count function is similar to range, except it does not have a stop value. It has both a start and a step:
#
# Unlike the range function, whose arguments must always be integers, count works with floats as well:
#
# In fact, we can even use other data types as well:
#
# We can even use Decimal numbers:

from itertools import count
g = count(10)
list(islice(g, 5))
g = count(10, step=2)
list(islice(g, 5))

g = count(10.5, 0.5)
list(islice(g, 5))

g = count(1+1j, 1+2j)
list(islice(g, 5))

from decimal import Decimal
g = count(Decimal('0.0'), Decimal('0.1'))
list(islice(g, 5))

# Infinite Iterators
# cycle is used to repeatedly loop over an iterable:
#
# One thing to note is that this works even if the argument is an iterator (i.e. gets exhausted after the first complete iteration over it)!
#
# As expected, cols was exhausted after the first iteration.
# Now let's see how cycle behaves:
#
# As you can see, cycle iterated over the elements of iterator, and continued the iteration even though the first run through the iterator technically exhausted it.

g = cycle(('red', 'green', 'blue'))
list(islice(g, 8))

def colors():
    yield 'red'
    yield 'green'
    yield 'blue'

cols = colors()
list(cols)
list(cols)

cols = colors()
g = cycle(cols)
list(islice(g, 10))

# Infinite Iterators
# The repeat function is used to create an iterator that just returns the same value again and again. By default it is infinite, but a count can be specified optionally:
#
# And we also optionally specify a count to make the iterator finite:
#
# The important thing to note as well, is that the "value" that is returned is the same object every time!

g = repeat('Python')
for _ in range(5):
    print(next(g))

g = repeat('Python', 4)
list(g)

l = [1, 2, 3]
result = list(repeat(l, 3))
result

l is result[0], l is result[1], l is result[2]

# Infinite Iterators
# repeat
#
# If you want to end up with three separate copies of your argument, then you'll need to use a copy mechanism (either shallow or deep depending on your needs).
#
# This is easily done using a comprehension expression:

l = [1, 2, 3]
result = [item[:] for item in repeat(l, 3)]
l is result[0], l is result[1], l is result[2]
result[0][0] = 100
result


# Chaining and Teeing Iterators
#
# suppose we have some generators producing squares:
#
# And we want to essentially iterate through all the values as if they were a single iterator.
#
# In fact, we could even create our own generator function to do this:
#
# a much simpler way is to use chain in the itertools module:
#
# As you can see, it simply took our list and handed it back directly - there was nothing else to chain with:
#
# Instead, we could use unpacking:

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

for gen in (l1, l2, l3):
    for item in gen:
        print(item)

def chain_iterables(*iterables):
    for iterable in iterables:
        yield from iterable

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

for item in chain_iterables(l1, l2, l3):
    print(item)

from itertools import chain

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

for item in chain(l1, l2, l3):
    print(item)

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

lists = [l1, l2, l3]
for item in chain(lists):
    for i in item:
        print(i)

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

lists = [l1, l2, l3]
for item in chain(*lists):
    print(item)

# Chaining and Teeing Iterators
#
# But, unpacking is not lazy!! Here's a simple example that shows this, and why we have to be careful using unpacking if we want to preserve lazy evaluation:
#
# Instead we can use an alternate "constructor" for chain, that takes a single iterable (of iterables) and lazily iterates through the outer iterable as well:
#
# Note also, that we can easily reproduce the same behavior of either chain quite easily:
#
# And we can use those just as we saw before with chain and chain.from_iterable:

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

def squares():
    print('yielding 1st item')
    yield (i**2 for i in range(4))
    print('yielding 2nd item')
    yield (i**2 for i in range(4, 8))
    print('yielding 3rd item')
    yield (i**2 for i in range(8, 12))

def read_values(*args):
    print('finised reading args')

read_values(*squares())

c = chain.from_iterable(squares())

for item in c:
    print(item)

def chain_(*args):
    for item in args:
        yield from item

def chain_iter(iterable):
    for item in iterable:
        yield from item

c = chain_(*squares())

c = chain_iter(squares())
for item in c:
    print(item)

# "Copying" an Iterator
#
# Sometimes we may have an iterator that we want to use multiple times for some reason.
#
# As we saw, iterators get exhausted, so
# simply making multiple references to the same iterator will not work - they will just point to the same iterator object.
#
# What we would really like is a way to "copy" an iterator and use these copies independently of each other.
#
# As you can see iters is a tuple contains 3 iterators - let's put them into some variables and see what each one is:

from itertools import tee

def squares(n):
    for i in range(n):
        yield i**2

gen = squares(10)
gen

iters = tee(squares(10), 3)
iters

iter1, iter2, iter3 = iters
next(iter1), next(iter1), next(iter1)
next(iter2), next(iter2)
next(iter3)

# "Copying" an Iterator
#
# As you can see, iter1, iter2, and iter3 are essentially three independent "copies" of our original iterator (squares(10))
#
# Note that this works for any iterable, so even sequence types such as lists:
#
# But you'll notice that the elements of lists are not lists themselves!
#
# As you can see, the elements returned by tee are actually iterators - even if we used an iterable such as a list to start off with!

l = [1, 2, 3, 4]
lists = tee(l, 2)
lists[0]
lists[1]

list(lists[0])
list(lists[0])

lists[1] is lists[1].__iter__()
'__next__' in dir(lists[1])

# Zipping
# t zips up two iterables and yields tuples containing elements from all iterables in "parallel". It is also lazy, and it will stop once the first iterable is exhausted.

l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4]
l3 = [1, 2, 3]

list(zip(l1, l2, l3))

# Zipping
#
# As you can see, the shortest iterable we provided to the zip function had a length of 3 (so it reached the end of iteration first), and our output therefore only had 3 tuples in it.
#
# Of course, this works with iterators and generators too:

def integers(n):
    for i in range(n):
        yield i


def squares(n):
    for i in range(n):
        yield i ** 2


def cubes(n):
    for i in range(n):
        yield i ** 3


iter1 = integers(6)
iter2 = squares(5)
iter3 = cubes(4)

list(zip(iter1, iter2, iter3))

# Zipping
#
# Sometimes we want to zip up iterables but completely iterate all the iterables, and not stop at the shortest
#
# Simple, we just need to provide a default "filler" value.
#
# And that's how the zip_longest function from itertools works:
#
# As you can see, we can only specify a single default value, this means that default will be used for any provided iterable once it has been fully iterated.
#
# As expected, zip_longest yields its values - it is lazy.

from itertools import zip_longest

help(zip_longest

l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4]
l3 = [1, 2, 3]

list(zip_longest(l1, l2, l3, fillvalue='N/A'))

# Zipping
# zip_longest
#
# Of course, since this zips over the longest iterable, beware of using an infinite iterable!
#
# You don't have to worry about this with the normal zip function as long as at least one of the iterables is finite:

def squares():
    i = 0
    while True:
        yield i ** 2
        i += 1

def cubes():
    i = 0
    while True:
        yield i ** 3
        i += 1

iter1 = squares()
iter2 = cubes()
list(zip(range(10), iter1, iter2))

# Combinatorics
# Cartesian Product
# The cartesian product is actually a lot more useful than it might appear at first.
#
# Consider this example, where we want to create a multiplication table as we have seen before:
#
# We can look at a few elements using islice:
#
# So, the Cartesian product of two iterables in general can be generated using a nested loop:
#
# We can achieve the same result with the product function in itertools. As usual, it is lazy as well.

def matrix(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            yield f'{i} x {j} = {i*j}'

list(itertools.islice(matrix(10), 10, 20))

l1 = ['x1', 'x2', 'x3', 'x4']
l2 = ['y1', 'y2', 'y3']
for x in l1:
    for y in l2:
        print((x, y), end=' ')
    print('')

l1 = ['x1', 'x2', 'x3', 'x4']
l2 = ['y1', 'y2', 'y3']
list(itertools.product(l1, l2))

# Combinatorics
# Cartesian Product
#
# As a simple example, let's go back to the multiplication table we created using a generator function.
#
# And of course this is now simple enough to even use just a generator expression:

def matrix(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            yield (i, j, i*j)

list(matrix(4))

def matrix(n):
    for i, j in itertools.product(range(1, n+1), range(1, n+1)):
        yield (i, j, i*j)

list(matrix(4))

def matrix(n):
    return ((i, j, i*j)
            for i, j in itertools.product(range(1, n+1), range(1, n+1)))

list(matrix(4))


# Combinatorics
# Cartesian Product
#
# You'll notice how we repeated the range(1, n+1) twice?
#
# This is a great example of where tee can be useful:

from itertools import tee

def matrix(n):
    return ((i, j, i*j)
            for i, j in itertools.product(*itertools.tee(range(1, n+1), 2)))

list(matrix(4))

# A common usage of Cartesian products might be to generate a grid of coordinates.
#
# For a 2D space for example, we might want to generate a grid of points ranging from -5 to 5 in both the x and y axes, with a step of 0.5.
#
# We can't use a range since ranges need integral numbers, but we have the count function in itertools we have seen before:
#
# And of course we can now do it in 3D as well:

def grid(min_val, max_val, step, *, num_dimensions=2):
    axis = itertools.takewhile(lambda x: x <= max_val,
                               itertools.count(min_val, step))

    # to handle multiple dimensions, we just need to repeat the axis that
    # many times - tee is perfect for that
    axes = itertools.tee(axis, num_dimensions)

    # and now we just need the product of all these iterables
    return itertools.product(*axes)


list(grid(-1, 1, 0.5))

list(grid(-1, 1, 0.5, num_dimensions=3))

# Another simple application of this might be to determine the odds of rolling an 8 with a pair of dice (with values 1 - 6).
#
# We can brute force this by generating all the possible results (the sample space), and counting how may items add up to 8.
#
# Now we want to filter out the tuples whose elements add up to 8:
#
# And we can calculate the odds by dividing the number acceptable outcomes by the size of the sample space. I'll actually use a Fraction so we retain our result as a rational number:

sample_space = list(itertools.product(range(1, 7), range(1, 7)))
print(sample_space)

outcomes = list(filter(lambda x: x[0] + x[1] == 8, sample_space))
print(outcomes)

from fractions import Fraction
odds = Fraction(len(outcomes), len(sample_space))
print(odds)

# Permutations
#
# In mathematics, the notion of permutation relates to the act of arranging all the members of a set into some sequence or order, or if the set is already ordered, rearranging (reordering) its elements, a process called permuting. These differ from combinations, which are selections of some members of a set where order is disregarded.
#
# We can create permutations of length n from an iterable of length m (n <= m) using the permutation function:
#
# As you can see all the permutations are, by default, the same length as the original iterable.
#
# We can create permutations of smaller length by specifying the r value:
#
# The important thing to note is that elements are not 'repeated' in the permutation. But the uniqueness of an element is not based on its value, but rather on its position in the original iterable.
#
# This means that the following will yield what looks like the same permutations when considering the values of the iterable:

l1 = 'abc'
list(itertools.permutations(l1))

list(itertools.permutations(l1, 2))

list(itertools.permutations('aaa'))

list(itertools.permutations('aba', 2))

# Combinations
#
# Combinations refer to the combination of n things taken k at a time without repetition. To refer to combinations in which repetition is allowed, the terms k-selection,[1] k-multiset,[2] or k-combination with repetition are often used.
#
# itertools offers both flavors - with and without replacement.
#
# Let's look at a simple example with replacement first:
#
# As you can see (4, 3) is not included in the result since, as a combination, it is the same as (3, 4) - order is not important.

list(itertools.combinations([1, 2, 3, 4], 2))

list(itertools.combinations_with_replacement([1, 2, 3, 4], 2))



# Coroutines
# The word co actually comes from cooperative.
# A coroutine is a generalization of subroutines (think functions), focused on cooperation between routines.
#
# If you have some concepts of multi-threading, this is similar in some ways. But whereas in multi-threaded applications the operating system usually decides when to suspend one thread and resume another, without asking permission, so-called preemptive multitasking, here we have routines that voluntarily yield control to something else - hence the term cooperative.

# Coroutines
#
# We can specify a maximum size for the queue when create it - this allows us to limit the number of items in the queue.
#
# (Note that I'm avoiding calling it the start and end of the queue, because what you consider the start/end of the queue might depend on how you are using it)

from collections import deque

dq = deque([1, 2, 3, 4, 5])
dq

dq.append(100)
dq

dq.appendleft(-10)
dq

dq.pop()
dq
dq.popleft()

# Coroutines
#
# We can create a capped queue:
#
# As you can see the first item (2) was automatically discarded from the left of the queue when we added 300 to the right.
#
# We can also find the number of elements in the queue by using the len() function:
# as well as query the maxlen:

from collections import deque
dq = deque([1, 2, 3, 4], maxlen=5)
dq.append(100)
dq
dq.append(200)
dq
dq.append(300)
dq

len(dq)
dq.maxlen

# Coroutines
# Now let's create an empty queue, and write two functions - one that will add elements to the queue, and one that will consume elements from the queue:

def produce_elements(dq):
    for i in range(1, 36):
        dq.appendleft(i)

def consume_elements(dq):
    while len(dq) > 0:
        item = dq.pop()
        print('processing item', item)

def coordinator():
    dq = deque()
    producer = produce_elements(dq)
    consume_elements(dq)

coordinator()

# Coroutines
#
# The goal is to process these after some time, and not wait until all the items have been added to the queue - maybe the incoming stream is infinite even.
#
# In that case, we want to "pause" adding elements to the queue, process (consume) those items, then once they've all been processed we want to resume adding elements, and rinse and repeat.
#
# We'll use a capped deque, and change our producer and consumers slightly, so that each one does it's work, the yields control back to the caller once it's done with its work - the producer adding elements to the queue, and the consumer removing and processing elements from the queue:

def produce_elements(dq, n):
    for i in range(1, n):
        dq.appendleft(i)
        if len(dq) == dq.maxlen:
            print('queue full - yielding control')
            yield


def consume_elements(dq):
    while True:
        while len(dq) > 0:
            print('processing ', dq.pop())
        print('queue empty - yielding control')
        yield


def coordinator():
    dq = deque(maxlen=10)
    producer = produce_elements(dq, 36)
    consumer = consume_elements(dq)
    while True:
        try:
            print('producing...')
            next(producer)
        except StopIteration:
            # producer finished
            break
        finally:
            print('consuming...')
            next(consumer)


coordinator()

# Generator States
# We create an generator object by calling the generator function:
#
# At this point the generator object is created, but we have not actually started running it. To do so, we call next(), which then starts running the function body until the first yield is encountered:
#
# Now the generator is suspended, waiting for us to call next again:
#
# Every time we call next, the generator function runs, or is in a running state until the next yield is encountered, or no more results are yielded and the function actually returns:

def gen(s):
    for c in s:
        yield c

g = gen('abc')

next(g)

next(g)

next(g)

# Generator States
#
# We can actually request the state of a generator programmatically by using the inspect module's getgeneratorstate() function:
#
# We can start running the generator by calling next:
#
# And the state is now:
# Once we exhaust the generator:
# The generator is now in a closed state:

from inspect import getgeneratorstate
g = gen('abc')
getgeneratorstate(g)

next(g)

getgeneratorstate(g)

next(g), next(g), next(g)

# Generator States
#
# Now we haven't seen the running state - to do that we just need to print the state from inside the generator - but to do that we need to have a reference to the generator object itself. This is not that easy to do, so I'm going to cheat and assume that the generator object will be referenced by a global variable global_gen:

def gen(s):
    for c in s:
        print(getgeneratorstate(global_gen))
        yield c

global_gen = gen('abc')

next(global_gen)

# Generator States
#
# Finally it is really important to understand that when a yield is encountered, the generator is suspended exactly at that point, but not before it has evaluated the expression to the right of the yield statement so it can produce that value in the return value of the next() function.
#
# As you can see square(i) was evaluated, then the value was yielded, and the genrator was suspended exactly at the point the yield statement was encountered:
#
# As you can see, only now does the right after yield string get printed from our generator.

def square(i):
    print(f'squaring {i}')
    return i ** 2

def squares(n):
    for i in range(n):
        yield square(i)
        print ('right after yield')

sq = squares(5)
next(sq)

next(sq)

# Sending data to Generators

# With PEP 342, generators were enhanced to allow not just sending data out (yielding), but also receiving data.
#
# The basic idea is that when a generator is suspended after a yield statement, why not allow sending it some data when we resume its execution, exactly at the point where it resumes.
#
# In other words, immediately after the yield statement.
#
# And not on the next line of code, but actually in the same line as the yield - we should now think of the yield keyword, not just as a statement, but as an expression that also receives data - and we can assign that received value to a variable using an assignment. We can send data to the suspended generator (and resume running it) by using the send() method of the generator (instead of just using the __next__ method (or, same thing, next()).
#
# Note: The same yield keyword is actually used to do both - but make no mistake, these are very different usages of the same keyword.
#
# The key difference is that yield is actually an expression, not a simple statement - and of course we can assign expressions to variables.

# Sending data to Generators
# simple example
#
# We now have a generator object, but what is it's state?
#
# t will first evaluate the right hand side - at which time it will yield and therefore become suspended!
#
# Now that it is waiting to resume, we can send it data, and the generator will received that data as if it were the right hand side of the assignment:
#
# And now the generator continued running until it hit a yield again - which it does since we have our yield inside an infinite loop:
#
# So, the send method essentially resume the generator just as the __next__ does - but it also sends in some data that we can capture if we want to, inside the generator.
#
# What happens if we do call next() or __next__ instead of send()?
#
# The same as if we had sent the None value:

def echo():
    while True:
        received = yield
        print('You said:', received)

e = echo()

from inspect import getgeneratorstate
getgeneratorstate(e)
next(e)
getgeneratorstate(e)
e.send('python')
e.send('I said')
next(e)
next(None)

# Sending data to Generators
#
# At this point we can see that generators can be used to both send and receive data.

def squares(n):
    for i in range(n):
        received = yield i ** 2
        print('received:', received)

sq = squares(5)
next(sq)

yielded = sq.send('hello')
print('yielded:', yielded)

yielded = sq.send('hello')
print('yielded:', yielded)

# Sending data to Generators
# Of course, once the generator no longer yields, but returns we'll get the same StopIteration exception:
#
# The next send is going to resume the generator, it will print what we send it, and continue running - but this time the loop is done, so it will print our final that's all, folks, and the function will return (None) and hence cause a StopIteration exception to be raised:

def echo(max_times):
    for i in range(max_times):
        received = yield
        print('You said:', received)
    print("that's all, folks!")

e = echo(3)
next(e)

e.send('python')
e.send('is')

e.send('awesome')

# Sending data to Generators
#
# Consider this example where we want a generator/coroutine that maintains (and yields) a running average of values we send it.
#
# Let's first see how we would do it without using a coroutine - instead we'll use a closure so we can maintain the state (total and count):
#
# And now the same, but using a coroutine:

def averager():
    total = 0
    count = 0
    def inner(value):
        nonlocal total
        nonlocal count
        total += value
        count += 1
        return total / count
    return inner

def running_averages(iterable):
    avg = averager()
    for value in iterable:
        running_average = avg(value)
        print(running_average)

running_averages([1, 2, 3, 4])

def running_averager():
    total = 0
    count = 0
    running_average = None
    while True:
        value = yield running_average
        total += value
        count += 1
        running_average = total / count

def running_averages(iterable):
    averager = running_averager()
    next(averager)  # prime generator
    for value in iterable:
        running_average = averager.send(value)
        print(running_average)

running_averages([1, 2, 3, 4])

# Closing Generators
#
# We can actually close a generator by sending it a special message, calling its close() method.

import csv

def parse_file(f_name):
    print('opening file...')
    f = open(f_name, 'r')
    try:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        next(f)  # skip header row
        reader = csv.reader(f, dialect=dialect)
        for row in reader:
            try:
                yield row
            except GeneratorExit:
                print('got a close...')
                raise
    finally:
        print('cleaning up...')
        f.close()

parser = parse_file('cars.csv')
for row in itertools.islice(parser, 5):
    print(row)

parser.close()

# Closing Generators
#
# We can actually close a generator by sending it a special message, calling its close() method.

def parse_file(f_name):
    print('opening file...')
    f = open(f_name, 'r')
    try:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        next(f)  # skip header row
        reader = csv.reader(f, dialect=dialect)
        for row in reader:
            try:
                yield row
            except GeneratorExit:
                print('got a close...')
                return
    finally:
        print('cleaning up...')
        f.close()

parser = parse_file('cars.csv')
for row in itertools.islice(parser, 5):
    print(row)

parser.close()

# Closing Generators
# def save_to_db()
#
# Notice how we're not even catching the GeneratorExit exception - we really don't need to - that exception will be raised, the finally block will run, and the GeneratorExit exception will be bubbled up to Python who will expect it after the call to close()

def save_to_db():
    print('starting new transaction')
    is_abort = False
    try:
        while True:
            data = yield
            print('sending data to database:', eval(data))
    except Exception:
        is_abort = True
        raise
    finally:
        if is_abort:
            print('aborting transaction')
        else:
            print('committing transaction')

trans = save_to_db()
next(trans)
trans.send('1 + 1')
trans.close()

trans = save_to_db()
next(trans)
trans.send('1 / 0')

# Sending Exceptions to Generators
# In fact we can also raise any exception inside a generator by using the throw() method

def gen():
    try:
        while True:
            received = yield
            print(received)
    finally:
        print('exception must have happened...')

g = gen()
next(g)
g.send('hello')g.throw(ValueError, 'custom message')

# Sending Exceptions to Generators
# As you can see, the exception occurred inside the generator, and then propagated up to the caller (we did not intercept and silence the exception). Of course we can do that if we want to:

def gen():
    try:
        while True:
            received = yield
            print(received)
    except ValueError:
        print('received the value error...')
    finally:
        print('generator exiting and closing')

g = gen()
next(g)
g.send('hello')
g.throw(ValueError, 'stop it!')

# Sending Exceptions to Generators
#
# if the generator catches the exception and yields a value, that is the return value of the throw() method
#
# And the generator is now in a suspended state, waiting for our next call:

from inspect import getgeneratorstate

def gen():
    while True:
        try:
            received = yield
            print(received)
        except ValueError as ex:
            print('ValueError received...', ex)

g = gen()
next(g)
g.send('hello')
g.throw(ValueError, 'custom message')
g.send('hello')
getgeneratorstate(g)


# Sending Exceptions to Generators
#
# if the generator does not catch the exception, the exception is propagated back to the caller
#
# And the generator is now in a closed state:

def gen():
    while True:
        received = yield
        print(received)

g = gen()
next(g)
g.send('hello')


# Sending Exceptions to Generators
#
# if the generator catches the exception, and exits (returns), the StopIteration exception is propagated to the caller

def gen():
    try:
        while True:
            received = yield
            print(received)
    except ValueError as ex:
        print('ValueError received', ex)
        return None

g = gen()
next(g)
g.send('hello')

g.throw(ValueError, 'custom message')

# Sending Exceptions to Generators
#
# if the generator catches the exception, and raises another exception, that exception is propagated to the caller
#
# And out generator is, once again, in a closed state:

def gen():
    try:
        while True:
            received = yield
            print(received)
    except ValueError as ex:
        print('ValueError received...', ex)
        raise ZeroDivisionError('not really...')

g = gen()
next(g)
g.send('hello')

g.throw(ValueError, 'custom message')

getgeneratorstate(g)

# Sending Exceptions to Generators
#
# As you can see our traceback includes both the ZeroDivisionError and the ValueError that caused the ZeroDivisionError to happen in the first place. If you don't want to have that traceback you can easily remove it and only display the ZeroDivisionError (I will cover this and exceptions in detail in a later part of this series):

def gen():
    try:
        while True:
            received = yield
            print(received)
    except ValueError as ex:
        print('ValueError received...', ex)
        raise ZeroDivisionError('not really...') from None

g = gen()
next(g)
g.send('hello')

g.throw(ValueError, 'custom message')

# Sending Exceptions to Generators
#
# Suppose we have a coroutine that handles writing data to a database. We have seen in some previous examples where we could use a coroutine to start and either commit or abort a transaction - based on closing the generator or forcing an exception to happen in the body of the generator.
#
# Let's revisit this example, but now we'll want to use exceptions to indicate to our generator whether to commit or abort a transaction, without necessarily exiting the generator:

class CommitException(Exception):
    pass

class RollbackException(Exception):
    pass

def write_to_db():
    print('opening database connection...')
    print('start transaction...')
    try:
        while True:
            try:
                data = yield
                print('writing data to database...', data)
            except CommitException:
                print('committing transaction...')
                print('opening next transaction...')
            except RollbackException:
                print('aborting transaction...')
                print('opening next transaction...')
    finally:
        print('generator closing...')
        print('aborting transaction...')
        print('closing database connection...')

sql = write_to_db()
next(sql)
sql.send(100)
sql.throw(CommitException)
sql.send(200)
sql.throw(RollbackException)
sql.send(200)
sql.throw(CommitException)
sql.close()

# Sending Exceptions to Generators
#
# throw() and close()
#
# The close() method does essentially the same thing as throw(GeneratorExit) except that when that exception is thrown using throw(), Python does not silence the exception for the caller:

def gen():
    try:
        while True:
            received = yield
            print(received)
    finally:
        print('closing down...')

g = gen()
next(g)
g.send('hello')
g.close()

g = gen()
next(g)
g.send('hello')
g.throw(GeneratorExit)

# Sending Exceptions to Generators
#
# throw() and close()
#
#
# Even if we catch the exception, we are still exiting the generator, so using throw will result in the caller receiving a StopIteration exception.
#
# So, we can use throw to close the generator, but as the caller we now have to handle the exception that propagates up to us:

def gen():
    try:
        while True:
            received = yield
            print(received)
    except GeneratorExit:
        print('received generator exit...')
    finally:
        print('closing down...')

g = gen()
next(g)
g.close()

g = gen()
next(g)
g.throw(GeneratorExit)

g = gen()
next(g)
try:
    g.throw(GeneratorExit)
except StopIteration:
    print('silencing GeneratorExit...')
    pass

# Using decorators to prime coroutines
#
# We saw how we always to 'prime' a coroutine (i.e. get the generator in a suspended state) before we can start sending values to it.
#
# This is something that must always be done - and this is an excellent use case for decorators.
#
# We're going to create a decorator that will create and prime the coroutine for us.
#
# Essentially we want to be able to:
#
#     create the coroutine (gen())
#     prime the coroutine (next(g))
#
# in one step - so that's what the decorator is going to do - it will wrap our original coroutine and return a new function that will perform those steps for us, and return the newly created and primed coroutine:
#
# As you can see our generator was automatically advanced from CREATED to SUSPENDED - and we can now use it straight away:

def coroutine(gen_fn):
    def inner():
        gen = gen_fn()
        next(gen)
        return gen
    return inner

@coroutine
def echo():
    while True:
        received = yield
        print(received)

ec = echo()

import inspect
inspect.getgeneratorstate(ec)

ec.send('hello')

# Using decorators to prime coroutines
#
# Now, we still need to expand this slightly to accomodate passing arguments to our generator function (coroutine):
#
# And now our generator stops functioning, it is in a closed state:

def coroutine(gen_fn):
    def inner(*args, **kwargs):
        gen = gen_fn(*args, **kwargs)
        next(gen)
        return gen
    return inner

import math

@coroutine
def power_up(p):
    result = None
    while True:
        received = yield result
        result = math.pow(received, p)

squares = power_up(2)
cubes = power_up(3)

squares.send(2)

cubes.send(2)

inspect.getgeneratorstate(squares)

# Using decorators to prime coroutines
#
# In this particular case, we don't want our generator to close down - it should simply yield None and ignore the exception, so it can continue working:
#
# Of course, we can close the generator ourselves still:

def coroutine(gen_fn):
    def inner(*args, **kwargs):
        gen = gen_fn(*args, **kwargs)
        next(gen)
        return gen
    return inner

@coroutine
def power_up(p):
    result = None
    while True:
        received = yield result
        try:
            result = math.pow(received, p)
        except TypeError:
            result = None

squares = power_up(2)
squares.send(2)
squares.send('abc')
squares.send(3)

squares.close()
inspect.getgeneratorstate(squares)

# Yield From - Two-Way Communications
#
# In the last section on generators, we started looking at yield from and how we could delegate iteration to another iterator.
#
# Alternatively we could write the same thing this way:

def squares(n):
    for i in range(n):
        yield i ** 2

def delegator(n):
    for value in squares(n):
        yield value

gen = delegator(5)
for _ in range(5):
    print(next(gen))

def delegator(n):
    yield from squares(n)


gen = delegator(5)
for _ in range(5):
    print(next(gen))


# Yield From - Two-Way Communications
# Let's start by looking at how the delegator works when a subgenerator closes by itself:
# We'll want to inspect the delegator and the subgenerator, so let's import what we'll need from the inspect module:
#
# Here play_song is the delegator, and song is the subgenerator. We, the Jupyter notebook, are the caller.
#
# As you can see, no local variables have been created in player yet - that's because it is created, not actually started.
#
# We can now get a handle to the subgenerator s:
#
# And we can check the state of s:
#
# As we can see the subgenerator is suspended.
# Let's iterate a few more times:

from inspect import getgeneratorstate, getgeneratorlocals

def song():
    yield "I'm a lumberjack and I'm OK"
    yield "I sleep all night and I work all day"

def play_song():
    count = 0
    s = song()
    yield from s
    yield 'song finished'
    print('player is exiting...')

player = play_song()
print(getgeneratorstate(player))
print(getgeneratorlocals(player))

next(player)

print(getgeneratorstate(player))
print(getgeneratorlocals(player))
s = getgeneratorlocals(player)['s']

print(getgeneratorstate(s))

print(next(player))
print(getgeneratorstate(player))
print(getgeneratorstate(s))

print(next(player))
print(getgeneratorstate(player))
print(getgeneratorstate(s))

# Yield From - Two-Way Communications
#
# Important to note here is that when the subgenerator returned, the delegator continued running normally.
#
# Let's make a tweak to our player generator to make this even more evident:

def player():
    count = 1
    while True:
        print('Run count:', count)
        yield from song()
        count += 1

p = player()
next(p), next(p)
next(p), next(p)
next(p), next(p)

# Yield From - Sending Data
#
# When we use yield from to delegate to a subgenerator, the established communication conduit also carries any data sent to the delegator generator.
#
# Let's write a simple coroutine that will receive string data and print the reversed string to the console:
#
# We can use this coroutine this way:
#
# And we can close the generator:

def echo():
    while True:
        received = yield
        print(received[::-1])

e = echo()
next(e)  # prime the coroutine

e.send('stressed')
e.send('tons')
e.close()

# Yield From - Sending Data
#
# Now let's write a simple delegator generator:
#
# We can create the delegator generator and prime the delegator:
#
# Now, calling next on the delegator will establish the connection to the subgenerator and automatically prime it as well.
#
# We can easily see this by doing some inspection:
#
# We can now send data to the delegator, and it will pass that along to the subgenerator:

def delegator():
    e = echo()
    yield from e

d = delegator()
next(d)

from inspect import getgeneratorstate, getgeneratorlocals
getgeneratorlocals(d)
e = getgeneratorlocals(d)['e']
print(getgeneratorstate(d))
print(getgeneratorstate(e))

# Yield From - Sending Data
#
# Let's modify our echo coroutine to both receive and yield a result, instead of just printing to the console:
#
# And we can use delegation as follows:

def echo():
    output = None
    while True:
        received = yield output
        output = received[::-1]

e = echo()
next(e)
e.send('stressed')

def delegator():
    yield from echo()

d = delegator()
next(d)

d.send('stressed')

# Let's take a look at a more interesting example of yield from.
#
# Our goal is to flatten a list containing nested lists to any level.
#
# And of course we can, if we prefer, make a list out of it:

l = [1, 2, [3, 4, [5, 6]], [7, [8, 9, 10]]]

def flatten_gen(curr_item):
    if isinstance(curr_item, list):
        for item in curr_item:
            yield from flatten_gen(item)
    else:
        yield curr_item

for item in flatten_gen(l):
    print(item)

list(flatten_gen(l))

# Our goal is to flatten a list containing nested lists to any level.
#
# Why are we getting this recursion error?
#
# That's because strings are iterables too - even a single character string!
#
# So, two issues: we may not want to treat strings as iterables, and if we do, then we need to be careful with single character strings.
#
# We're going to tweak our is_iterable function, and our flatten generator to handle these two issues:
#
# Let's just make sure our function works as expected:
#
# Good, now we can tweak our flatten generator so we can tell it whether to handle strings as iterables or not:

l = [1, 2, [3, 4, [5, 6]], [7, [8, 9, 10]]]

def is_iterable(item, *, str_is_iterable=True):
    try:
        iter(item)
    except:
        return False
    else:
        if isinstance(item, str):
            if str_is_iterable and len(item) > 1:
                return True
            else:
                return False
        else:
            return True

print(is_iterable([1, 2, 3]))
print(is_iterable('abc'))
print(is_iterable('a'))

print(is_iterable([1, 2, 3], str_is_iterable=False))
print(is_iterable('abc', str_is_iterable=False))
print(is_iterable('a', str_is_iterable=False))

def flatten_gen(curr_item, *, str_is_iterable=True):
    if is_iterable(curr_item, str_is_iterable=str_is_iterable):
        for item in curr_item:
            yield from flatten_gen(item, str_is_iterable=str_is_iterable)
    else:
        yield curr_item

llist(flatten_gen(l))
list(flatten_gen(l, str_is_iterable=False))

# we saw we could use yield from recursively. In fact a generator can be both a delegator and a subgenerator. Here's a simple example of this:

def coro():
    while True:
        received = yield
        print(received)


def gen1():
    yield from gen2()


def gen2():
    yield from gen3()


def gen3():
    yield from coro()


g = gen1()
next(g)

g.send('hello')

# Yield From - Closing and Return
#
# Just as we can send next and send through a delegator, we can also send close.
#
# How does this affect the delegator and the subgenerator?
# At this point, both the delegator and the subgenerator are primed and suspended:
#
# We can send data to the delegator:
#
# We can even send data directly to the subgenerator since we now have a handle on it:
#
# In fact, we can close it too:
#
# So, what is the state of the delegator now?
#
# But the subgenerator closed, so let's see what happens when we call next on d:
#
# As you can see, the generator code resume right after the yield from, and we can do this one more time to close the delegator:

def subgen():
    try:
        while True:
            received = yield
            print(received)
    finally:
        print('subgen: closing...')

def delegator():
    s = subgen()
    yield from s
    yield 'delegator: subgen closed'
    print('delegator: closing...')

d = delegator()
next(d)

from inspect import getgeneratorstate, getgeneratorlocals

getgeneratorlocals(d)

s = getgeneratorlocals(d)['s']
print(getgeneratorstate(d))
print(getgeneratorstate(s))

d.send('hello')
s.send('python')
s.close()

getgeneratorstate(d)

next(d)

# Yield From - Closing and Return
#
# so this is what happens when the subgenerator closes (directly or indirectly) - the delegator simply resumes running right after the yield from when we call next.
#
# But what happens if we close the delegator instead of just closing the subgenerator?
#
# As you can see the subgenerator also closed. Is the delegator closed too?

d = delegator()
next(d)
s = getgeneratorlocals(d)['s']
print(getgeneratorstate(d))
print(getgeneratorstate(s))

d.close()

print(getgeneratorstate(d))
print(getgeneratorstate(s))

# Yield From - Closing and Return
#
# Yes. So closing the delegator will close not only the delegator itself, but also close the currently active subgenerator (if any).
#
# We should notice that when we closed the subgenerator directly no apparent exception was raised in our context.
#
# What happens if the subgenerator returns something when it closes?
#
# Hmmm, the StopIteration exception was silenced. Let's do this a different way, since we know the StopIteration exception should contain the return value:

def subgen():
    try:
        while True:
            received = yield
            print(received)
    finally:
        print('subgen: closing...')
        return 'subgen: return value'

s = subgen()
next(s)
s.send('hello')
s.close()
s = subgen()
next(s)
s.send('hello')
s.throw(GeneratorExit, 'force exit')

# Yield From - Closing and Return
#
# OK, so now we can see that the StopIteration exception contains the return value.
#
# The yield from actually captures that value as it's return value - in other words yield from is not just a statement, it is in fact, like yield, also an expression.
#
# Let's see how that works:
#
# As you can see the return value of the subgenerator ended up as the result of the yield from expression.

def subgen():
    try:
        yield 1
        yield 2
    finally:
        print('subgen: closing...')
        return 100

def delegator():
    s = subgen()
    result = yield from s
    print('subgen returned:', result)
    yield 'delegator suspended'
    print('delegator closing')

d = delegator()
next(d)
next(d)
next(d)

# Yield From - Throwing Exceptions
#
# We have seen that yield from allows us to establish a 2-way communication channel with a subgenerator and we could use next, and send to send a "request" to a delegated subgenerator via the delegator generator.
#
# In fact, we can also send exceptions by throwing an exception into the delegator, just like a send

class CloseCoroutine(Exception):
    pass

def echo():
    try:
        while True:
            received = yield
            print(received)
    except CloseCoroutine:
        return 'coro was closed'
    except GeneratorExit:
        print('closed method was called')

e = echo()
next(e)

e.throw(CloseCoroutine, 'just closing')

e = echo()
next(e)
e.close()

# Yield From - Throwing Exceptions
#
# As we can see the difference between throw and close is that although close causes an exception to be raised in the generator, Python essentially silences it.
#
# It works the same way when we delegate to the coroutine in a delegator:

def delegator():
    result = yield from echo()
    yield 'subgen closed and returned:', result
    print('delegator closing...')

d = delegator()
next(d)
d.send('hello')

d.throw(CloseCoroutine)

# Yield From - Throwing Exceptions
#
# Now what happens if the throw in the subgenerator does not close subgenerator but instead silences the exception and yields a value instead?

class CloseCoroutine(Exception):
    pass

class IgnoreMe(Exception):
    pass

def echo():
    try:
        while True:
            try:
                received = yield
                print(received)
            except IgnoreMe:
                yield "I'm ignoring you..."
    except CloseCoroutine:
        return 'coro was closed'
    except GeneratorExit:
        print('closed method was called')

d = delegator()
next(d)

d.send('python')

result = d.throw(IgnoreMe, 1000)

result

d.send('rocks!')
d.close()


# Yield From - Throwing Exceptions
#
# Why did we not get a yielded value back?
#
# That's because the subgenerator was paused at the yield that yielded "I'm, ignoring you".
#
# If we want to coroutine to continue running normally after ignoring that exception we need to tweak it slightly:

def echo():
    try:
        output = None
        while True:
            try:
                received = yield output
                print(received)
            except IgnoreMe:
                output = "I'm ignoring you..."
            else:
                output = None
    except CloseCoroutine:
        return 'coro was closed'
    except GeneratorExit:
        print('closed method was called')

d = delegator()
next(d)

d.send('hello')
d.throw(IgnoreMe)
d.send('python')
d.close()

# Yield From - Throwing Exceptions
#
# What happens if we do not handle the error in the subgenerator and simply let the exception propagate up? Who gets the exception, the delegator, or the caller?

def echo():
    while True:
        received = yield
        print(received)

def delegator():
    yield from echo()

d = delegator()
next(d)

d.throw(ValueError)

# Yield From - Throwing Exceptions
#
# OK, so we, the caller see the exception. But did the delegator see it too? i.e. can we catch the exception in the delegator?
#
# As you can see, we were able to catch the exception in the delegator. Of course, the way we wrote our code, the delegator still closed, and hence we now see a StopIteration exception.

def delegator():
    try:
        yield from echo()
    except ValueError:
        print('got the value error')
d = delegator()
next(d)

d.throw(ValueError)





