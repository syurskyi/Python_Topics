#!/usr/bin//env python
# coding: utf-8

# # `dict`

# ## Problem Statement: Vigenère Cipher
# Implement a Vigenère cipher.Plain text:  attackatdawn
# Key:         python
# Cipher text: prmhqxprwhka
# In[ ]:


from string import ascii_lowercase
from itertools import repeat, cycle, islice

CODEBOOK = {x: {y: z for y,z in zip(ascii_lowercase, islice(cycle(ascii_lowercase), i, None))}
            for i, x in enumerate(ascii_lowercase)}

def encipher(message, key, codebook=CODEBOOK):
    message = ''.join(m for m in message.lower() if m in codebook)
    return ''.join(codebook[k][m] for k, m in zip(cycle(key), message))

def decipher(message, key, codebook=CODEBOOK):
    decodebook = {x: {z:y for y,z in yz.items()} for x, yz in codebook.items()}
    return ''.join(decodebook[k][m] for k, m in zip(cycle(key), message))

msg = 'Attack at dawn!'
key = 'python'
enc_msg = encipher(msg, key)
print(enc_msg)

decipher(enc_msg, key)


# ## Problem Statement: Concordance (Word Count)
# Find the ten most commonly used words in a text file.
#
# get_ipython().system(" wget -O paradise-lost.txt 'http://www.gutenberg.org/cache/epub/26/pg26.txt'")
# get_ipython().system(' head -n 10 paradise-lost.txt')
print('#' * 20 + 'Concordance (Word Count)')

from re import sub

def concordance(text):
    freq = {}
    for word in text.split():
        word = sub('[^\w]', '', word.lower())
        if word not in freq:
            freq[word] = 0
        freq[word] += 1
    return freq

with open('paradise-lost.txt') as f:
    text = ''.join(f)

freq = concordance(text)
print(sorted(freq.items(), key=lambda kv: kv[1], reverse=True)[:10])


# ## dict
# - lookup-table
# - map
# - content-addressible storage
# - relation
# - hash
# - also: associative array, symbol table
# #### as a dictionary
print('#' * 20 + 'as a dictionary')



dictionary = {'one': 'uno',
              'two': 'dos',
              'three': 'tres'}

print(dictionary['one'])
# print(dictionary['uno'])  # KeyError: 'uno'
# dictionary['four']  # KeyError: 'uno'
dictionary['four'] = 'cuatro'
print(dictionary)

del dictionary['one']
del dictionary['two']
print(dictionary)


# #### as a map
print('#' * 20 + 'as a map')

course_professors = {'calculus':       'Prof. Kotter',
                     'diff eq':        'Prof. Feeny',
                     'linear algebra': 'Prof. Kotter',
                     'real analysis':  'Prof. Crabtree'}

student_courses = {'vinnie':    ['calculus', 'diff eq'],
                   'arnold':    ['calculus', 'linear algebra'],
                   'juan luis': ['real analysis']}

student_courses = {'vinnie':    {'calculus', 'diff eq'},
                   'arnold':    {'calculus', 'linear algebra'},
                   'juan luis': {'real analysis'}}

student_professors = {} # which student has which professor?

for student in student_courses:
    for course in student_courses[student]:
        if student not in student_professors:
            student_professors[student] = set()
        student_professors[student].add(course_professors[course])

print(student_professors)


# #### creating a `dict`
print('#' * 20 + 'creating a dict')
xs = {1: 1, 2: 4, 3:9}
print(xs)

xs = dict(one='uno', two='dos')
print(xs)

xs = dict([('uno',  'one'),
           ('dos',  'two'),
           ('tres', 'three'),])
print(xs)

from string import ascii_lowercase
xs = dict.fromkeys(ascii_lowercase)
print(xs)

# xs = {[1,2,3]: 10}  # unhashable type: 'list'

xs = {1:1, 2:4, 3:9}
ys = dict(xs)
print(ys)


# #### `dict.update`
print('#' * 20 + 'dict.update')

xs = {1:1, 2:4, 3:9}
ys = {}
ys.update(xs)
print(ys)

# #### `dict` methods
print('#' * 20 + 'dict` methods')

dir({})

print([attr for attr in dir({}) if '__' not in attr])


# #### `dict.clear`
print('#' * 20 + '`dict.clear`')

xs = {'one': 'uno'}
print(xs)

xs['two'] = 'dos'
print(xs)

xs.clear()
print(xs)

xs = {'one': 'uno'}
ys = xs.copy()
xs.clear()

print(xs)
print(ys)

xs = {'one': {'spanish': 'uno',
              'german':  'ein',
              'french':  'un'}}
print(xs)

ys = xs.copy()
xs['one'].clear()
print(ys)


# #### `dict.get`
print('#' * 20 + '`dict.get`')

xs = {'one': 'uno'}
# print(xs['two'])  # KeyError: 'two'


def get_word(d, word):
    if word in d:
        return d[word]
    return None

xs.get('two', 'unknown')

# #### `dict.pop`, `dict.popitem`
print('#' * 20 + '`dict.pop`, `dict.popitem`')

xs = {'one': 'uno', 'two': 'dos'}
xs.pop('one')
print(xs)
# xs.pop('one') # KeyError: 'one'
xs.pop('one', 'default')
xs.popitem()

# #### `dict.keys`, `dict.values`, `dict.items`
print('#' * 20 + '`dict.keys`, `dict.values`, `dict.items`')

d = {'uno': 'one', 'dos': 'two', 'tres': 'three'}

for key in d:
    print (key)

for key in d.keys():
    print (key)

for value in d.values():
    print (value)

for item in d.items():
    print (item)

# iterkeys, itervalues, iteritems in Python 2
# viewkeys, viewvalues, viewitems in Python 2
print('#' * 20 + 'dict` methods')

d = {'uno': 'one', 'dos': 'two', 'tres': 'three'}
keys = d.keys()
print(keys)

d['cinco'] = 'five'
print(d)
print(keys)

# #### `dict.setdefault`
print('#' * 20 + '`dict.setdefault`')

student_courses = {'vinnie':    {'calculus', 'diff eq'},
                   'arnold':    {'calculus', 'linear algebra'},
                   'juan luis': {'real analysis'}}

student_courses['vinnie'].add('linear algebra')

# student_courses['freddie'].add('linear algebra')  # KeyError: 'freddie'

if 'freddie' not in student_courses:
    student_courses['freddie'] = set()
student_courses['freddie'].add('linear algebra')

student_courses.setdefault('rosalie', set()).add('calculus')
print(student_courses)

# #### `dict.__missing__`
print('#' * 20 + '`dict.__missing__')


class lowercasedict(dict):
    def __missing__(self, key):
        return self[key.lower()]

d = lowercasedict({'uno': 'one', 'dos': 'two'})

print(d['UNO'])

# #### `dict`-comprehensions
print('#' * 20 + '`dict`-comprehensions')

print({x: x**2 for x in range(10)})


# substitution cipher
print('#' * 20 + 'substitution cipher')

from string import ascii_lowercase
print(ascii_lowercase)

from random import shuffle
print(ascii_lowercase)

alphabet = list(ascii_lowercase)
print(alphabet)

shuffle(alphabet)
print(alphabet)

codebook = {x:alphabet.pop() for x in ascii_lowercase}
print(codebook)

message = 'python is great'

encoded = ''.join(codebook.get(m,'') for m in message)
print(encoded)

reverse_codebook = {v:k for k,v in codebook.items()}
print (''.join(reverse_codebook.get(m,'') for m in 'ysdvmulizkwxd'))

# #### as a lookup-table
print('#' * 20 + 'as a lookup-table')

sine = [-0.0000, -0.0495, -0.0988, -0.1479,
        -0.1966, -0.2449, -0.2925, -0.3394,
        -0.3855, -0.4307, -0.4748, -0.5177,
        -0.5594, -0.5997, -0.6386, -0.6758,
        -0.7115, -0.7453, -0.7774, -0.8076,
        -0.8357, -0.8619, -0.8859, -0.9078,
        -0.9274, -0.9448, -0.9598, -0.9725,
        -0.9828, -0.9908, -0.9963, -0.9993,
        -0.9999, -0.9981, -0.9938, -0.9871,
        -0.9780, -0.9665, -0.9526, -0.9364,
        -0.9179, -0.8971, -0.8742, -0.8491,
        -0.8219, -0.7927, -0.7616, -0.7286,
        -0.6939, -0.6574, -0.6193, -0.5798,
        -0.5387, -0.4964, -0.4529, -0.4082,
        -0.3626, -0.3161, -0.2688, -0.2208,
        -0.1723, -0.1234, -0.0741, -0.0247,
         0.0247,  0.0741,  0.1234,  0.1723,
         0.2208,  0.2688,  0.3161,  0.3626,
         0.4082,  0.4529,  0.4964,  0.5387,
         0.5798,  0.6193,  0.6574,  0.6939,
         0.7286,  0.7616,  0.7927,  0.8219,
         0.8491,  0.8742,  0.8971,  0.9179,
         0.9364,  0.9526,  0.9665,  0.9780,
         0.9871,  0.9938,  0.9981,  0.9999,
         0.9993,  0.9963,  0.9908,  0.9828,
         0.9725,  0.9598,  0.9448,  0.9274,
         0.9078,  0.8859,  0.8619,  0.8357,
         0.8076,  0.7774,  0.7453,  0.7115,
         0.6758,  0.6386,  0.5997,  0.5594,
         0.5177,  0.4748,  0.4307,  0.3855,
         0.3394,  0.2925,  0.2449,  0.1966,
         0.1479,  0.0988,  0.0495,  0.0000,]

from math import pi
angle = 0
print(angle)

angle_index = int((pi + angle) / (2 * pi) * len(sine))
print(angle_index)

print(sine[angle_index-1])

from math import sin
sin(angle)

print(sine[angle_index], sine[angle_index-1])

# table of values
print('#' * 20 + 'table of values')

table = {-3.1416: -0.0000, -3.0921: -0.0495, -3.0426: -0.0988, -2.9932: -0.1479,
         -2.9437: -0.1966, -2.8942: -0.2449, -2.8447: -0.2925, -2.7953: -0.3394,
         -2.7458: -0.3855, -2.6963: -0.4307, -2.6469: -0.4748, -2.5974: -0.5177,
         -2.5479: -0.5594, -2.4984: -0.5997, -2.4490: -0.6386, -2.3995: -0.6758,
         -2.3500: -0.7115, -2.3005: -0.7453, -2.2511: -0.7774, -2.2016: -0.8076,
         -2.1521: -0.8357, -2.1026: -0.8619, -2.0532: -0.8859, -2.0037: -0.9078,
         -1.9542: -0.9274, -1.9047: -0.9448, -1.8553: -0.9598, -1.8058: -0.9725,
         -1.7563: -0.9828, -1.7068: -0.9908, -1.6574: -0.9963, -1.6079: -0.9993,
         -1.5584: -0.9999, -1.5090: -0.9981, -1.4595: -0.9938, -1.4100: -0.9871,
         -1.3605: -0.9780, -1.3111: -0.9665, -1.2616: -0.9526, -1.2121: -0.9364,
         -1.1626: -0.9179, -1.1132: -0.8971, -1.0637: -0.8742, -1.0142: -0.8491,
         -0.9647: -0.8219, -0.9153: -0.7927, -0.8658: -0.7616, -0.8163: -0.7286,
         -0.7668: -0.6939, -0.7174: -0.6574, -0.6679: -0.6193, -0.6184: -0.5798,
         -0.5689: -0.5387, -0.5195: -0.4964, -0.4700: -0.4529, -0.4205: -0.4082,
         -0.3711: -0.3626, -0.3216: -0.3161, -0.2721: -0.2688, -0.2226: -0.2208,
         -0.1732: -0.1723, -0.1237: -0.1234, -0.0742: -0.0741, -0.0247: -0.0247,
          0.0247:  0.0247,  0.0742:  0.0741,  0.1237:  0.1234,  0.1732:  0.1723,
          0.2226:  0.2208,  0.2721:  0.2688,  0.3216:  0.3161,  0.3711:  0.3626,
          0.4205:  0.4082,  0.4700:  0.4529,  0.5195:  0.4964,  0.5689:  0.5387,
          0.6184:  0.5798,  0.6679:  0.6193,  0.7174:  0.6574,  0.7668:  0.6939,
          0.8163:  0.7286,  0.8658:  0.7616,  0.9153:  0.7927,  0.9647:  0.8219,
          1.0142:  0.8491,  1.0637:  0.8742,  1.1132:  0.8971,  1.1626:  0.9179,
          1.2121:  0.9364,  1.2616:  0.9526,  1.3111:  0.9665,  1.3605:  0.9780,
          1.4100:  0.9871,  1.4595:  0.9938,  1.5090:  0.9981,  1.5584:  0.9999,
          1.6079:  0.9993,  1.6574:  0.9963,  1.7068:  0.9908,  1.7563:  0.9828,
          1.8058:  0.9725,  1.8553:  0.9598,  1.9047:  0.9448,  1.9542:  0.9274,
          2.0037:  0.9078,  2.0532:  0.8859,  2.1026:  0.8619,  2.1521:  0.8357,
          2.2016:  0.8076,  2.2511:  0.7774,  2.3005:  0.7453,  2.3500:  0.7115,
          2.3995:  0.6758,  2.4490:  0.6386,  2.4984:  0.5997,  2.5479:  0.5594,
          2.5974:  0.5177,  2.6469:  0.4748,  2.6963:  0.4307,  2.7458:  0.3855,
          2.7953:  0.3394,  2.8447:  0.2925,  2.8942:  0.2449,  2.9437:  0.1966,
          2.9932:  0.1479,  3.0426:  0.0988,  3.0921:  0.0495,  3.1416:  0.0000}


from bisect import bisect
# from __future__ import division


class interpolating_dict(dict):
    def __missing__(self, key):
        sorted_keys = sorted(self.keys())

        index = bisect(sorted_keys, key)

        if index == 0 or index == len(sorted_keys):
            raise KeyError('cannot extrapolate value {}'.format(key))

        left_key, right_key = sorted_keys[index-1], sorted_keys[index]
        left_val, right_val = self[left_key], self[right_key]

        slope = (right_val - left_val) / (right_key - left_key)
        self[key] = value = slope * (key - left_key) + left_val
        return value

sine = interpolating_dict(table)
print(sine[3.1416])
print(sine[0])

print(sine[pi/2])
print(sine)


#### as a relation or a function
print('#' * 20 + 'as a relation or a function')

from math import sqrt

def roots(a,b,c):
    return (-b + sqrt(b**2 - 4*a*c))/(2*a)

roots(1,2,1) # (x+1)(x+1) == x² + 2x + 1

class rootdict(dict): # ???
    def __missing__(self, key):
        a, b, c = key
        return (-b + sqrt(b**2 - 4*a*c))/(2*a)

d = rootdict()
print(d[1,2,1])

from sys import version_info
assert version_info.major == 3 and version_info.minor >= 3,   'requires PEP 362; Python 3.3 or later; python.org/dev/peps/pep-0362/'

from inspect import signature
class memoise(dict):
    def __init__(self, func):
        self.func, self.signature = func, signature(func)
    def __missing__(self, key):
        args, kwargs = key
        self[key] = self.func(*args, **dict(kwargs))
        return self[key]
    def __call__(self, *args, **kwargs):
        key = self.signature.bind(*args, **kwargs)
        return self[key.args, frozenset(key.kwargs.items())]

from time import sleep

@memoise
def roots(a,b,c):
    sleep(1)
    return (-b + sqrt(b**2 - 4*a*c))/(2*a)

# get_ipython().run_line_magic('time', 'roots(1,2,1)')
# get_ipython().run_line_magic('time', 'roots(1,2,1)')
roots(2,4,2)
print(roots)


# #### `__getitem__` and `__call__`
print('#' * 20 + '`__getitem__` and `__call__`')

d = {1: 1, 2:4}
print(d[2])
d.__getitem__(2)

class Foo:
    def __getitem__(self, key):
        return key**2

foo = Foo()
print(foo[13])

class Foo:
    def __call__(self, val):
        return val**2

foo = Foo()
foo(10)

# # #### `dict`-alikes
print('#' * 20 + '`__getitem__` and `__call__`')

# from contextlib import closing
# from pandas import HDFStore, DataFrame
# from numpy import linspace
#
# df = DataFrame()
# df['val'] = linspace(0, 10**4, 10000)
#
# with closing(HDFStore('test.hd5')) as store:
#     store['key'] = df
#
# store


# from IPython.display import display
#
# with closing(HDFStore('test.hd5')) as store:
#     display(store)
#     display(store['key'].head())


# #### `dict.__missing__`
print('#' * 20 + '`dict.__missing__`')

from collections import Iterable


class rangedict(dict):
    def __missing__(self, key):
        for k, v in self.items():
            if isinstance(k, Iterable):
                left, right = k
                if left <= key < right:
                    self[key] = v
                    return v
        raise KeyError('cannot find {} in rangedict'.format(key))


codes = rangedict({(  0,   10): 'red',
                   ( 10,  100): 'yellow',
                   (100, 1000): 'green', })

print(codes[105])
print(codes)


class passthrudict(dict):
    def __missing__(self, key):
        return key


censor = passthrudict({'hell': 'h***',
                       'darn': 'd*rn',})

sentence = "That darn cat!"
' '.join(censor[w] for w in sentence.split())
sentence = "Y'all can go to hell; I'm going to Texas!"
' '.join(censor[w] for w in sentence.split())


from itertools import groupby, chain
from unicodedata import category


def fancy_split(s):
    return [''.join(g) for k,g in groupby(s, key=lambda x: category(x)[0] == 'L')]


sentence = "Y'all can go to hell; I'm going to Texas!"
fancy_split(sentence)
''.join(censor[w] for w in fancy_split(sentence))


# #### `collections.defaultdict`
print('#' * 20 + '`collections.defaultdict`')

student_courses = {'vinnie':    {'calculus', 'diff eq'},
                   'arnold':    {'calculus', 'linear algebra'},
                   'juan luis': {'real analysis'}}

student_courses['freddie'] = set()
student_courses['freddie'].add('linear algebra')


from collections import defaultdict

student_courses = defaultdict(set)
student_courses.update({'vinnie':    {'calculus', 'diff eq'},
                        'arnold':    {'calculus', 'linear algebra'},
                        'juan luis': {'real analysis'}})
student_courses['freddie'].add('linear algebra')
print(student_courses)
print('foobar' in student_courses)
print(student_courses['foobar'])


# # #### as a hash
print('#' * 20 + 'as a hash')

# {[1,2,3]: 4} # TypeError: unhashable type: 'list'

english = ['one', 'two', 'three']
spanish = ['uno', 'dos', 'tres']
english.index('two')
print(spanish[english.index('three')])

from bisect import bisect_left
lookup = [en for en,es in sorted(zip(english, spanish))]
value  = [es for en,es in sorted(zip(english, spanish))]

key = 'one'
print(value[bisect_left(lookup, key)])


# hash(x) # name 'x' is not defined

# from numpy import array, linspace
# from numpy.random import choice, shuffle
# from string import ascii_lowercase
# from bisect import bisect_left
#
# MAX_SIZE = 10**4
#
# letters = array([c for c in ascii_lowercase])
# words   = choice(letters, size=(MAX_SIZE, 10))
# words   = array([''.join(w) for w in words])
#
# ns = linspace(1, MAX_SIZE, 500)
# list_times = []
# dict_times = []
# bisect_times = []
#
# for n in ns:
#     shuffle(words)
#
#     sample_list = list(words[:n])
#     sample_dict = dict.fromkeys(sample_list)
#     sample_bisect = sorted(sample_list)
#
#     lookup_words = choice(sample_list, size=10)
#
#     list_time = get_ipython().run_line_magic('timeit', '-q -n1 -o [sample_list.index(w) for w in lookup_words]')
#     dict_time = get_ipython().run_line_magic('timeit', '-q -n1 -o [sample_dict[w] for w in lookup_words]')
#     bisect_time = get_ipython().run_line_magic('timeit', '-q -n1 -o [bisect_left(sample_bisect, w) for w in lookup_words]')
#
#     list_times.append(list_time.best)
#     dict_times.append(dict_time.best)
#     bisect_times.append(bisect_time.best)
#
#
# get_ipython().run_line_magic('matplotlib', 'inline')


from matplotlib.pyplot import figure, plot, title, legend, ylabel, xlabel, show

fig = figure(figsize=(12,8))

#plot(ns, list_times, 'bo',   label=u'list lookup ~ O(n)')
# plot(ns, dict_times, 'go',   label=u'dict lookup ~ O(1)')
# plot(ns, bisect_times, 'ro', label=u'bisect lookup ~ O(log(n))')

# title('list vs dict vs bisect (binary-search) lookup')
# legend(loc='best')
# xlabel('input size (elements)', figure=fig)
# ylabel('best time out of 3 (s)', figure=fig)
# show()
#
#
# # #### dict vs object
print('#' * 20 + 'dict vs object')

class Foo:
    pass

foo = Foo()
foo.x = 10
print(foo.x)

getattr(foo, 'x') # "getattr protocol"

bar = {}
bar['y'] = 10
print(bar['y'])

from operator import getitem # "getitem protocol"

getitem(bar, 'y')

print(foo.__dict__)

class Base:
    z = 10

class Derived(Base):
    pass

d = Derived()
print(d.__dict__)

getattr(d, 'z')

class Foo:
    x = 10

foo = Foo()
foo.z = 10

bar = {'y': 20}

# get_ipython().run_line_magic('timeit', 'foo.z')
# get_ipython().run_line_magic('timeit', "bar['y']")

class Foo:
    def __getitem__(self, key):
        if key == 'x':
            return 10
        raise KeyError('no such key {}'.format(key))

    def __getattr__(self, attr):
        if attr == 'x':
            return 100
        raise AttributeError('no such attr {}'.format(attr))

foo = Foo()

# get_ipython().run_line_magic('timeit', 'foo.x')
# get_ipython().run_line_magic('timeit', "foo['x']")


# https://docs.python.org/3/reference/datamodel.html#customizing-attribute-access
#
# - `__getattr__` is invoked after other mechanisms fail.
#
#   "Called when an attribute lookup has not found the attribute in the usual places"
#
#
# - `__getattribute__` is always invoked, and it is invoked first.
#
#   "Called unconditionally to implement attribute accesses for instances of the class."


class Foo:
    def __getitem__(self, key):
        if key == 'x':
            return 10
        raise KeyError('no such key {}'.format(key))

    def __getattribute__(self, attr):
        if attr == 'x':
            return 10
        raise AttributeError('no such attr {}'.format(attr))

foo = Foo()

# get_ipython().run_line_magic('timeit', 'foo.x')
# get_ipython().run_line_magic('timeit', "foo['x']")


# #### semantics
print('#' * 20 + 'semantics')

class Foo:
    def __getattr__(self, attr):
        return attr
    def __getitem__(self, key):
        return key

foo = Foo()
print(foo['two words'], foo['123'], foo['abc/def'])

#foo.two words
#foo.123
#foo.abc/def

class Foo:
    def __init__(self):
        self.x = 10

foo = Foo()
print(foo.x, foo.__dict__['x'])

class Base:
    x = 10

class Derived(Base):
    pass

d = Derived()
Base.y = 100
print(d.y)

from collections import ChainMap

b = {}
d = ChainMap({}, b)

b['x'] = 10
print(d['x'])
d['x'] = 500
print(d['x'])


class BaseA:
    x = 10

class BaseB:
    x = 100
    y = 200

class Derived(BaseA, BaseB):
    pass

d = Derived()
print(d.x, d.y)

ba = {'x': 10}
bb = {'x': 100, 'y': 200}

d = ChainMap({}, ba, bb)
print(d['x'], d['y'])
Derived.__mro__
d = ChainMap({}, *(entry.__dict__ for entry in Derived.__mro__))
print(d['x'], d['y'])


class Foo:
    def __init__(self, x):
        self.x = x

foo = Foo(10)
print(foo.x)

class Foo:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        self._x += 1
        return self._x

foo = Foo(10)
print(foo.x, foo.x, foo.x)

class Foo:
    def __init__(self, x):
        self._x = x

    def __getitem__(self, key):
        if key == 'x':
            self._x += 1
            return self._x
        raise KeyError('no such key {}'.format(key))

foo = Foo(10)
print(foo['x'], foo['x'], foo['x'])


# #### attribute dictionary
print('#' * 20 + 'attribute dictionary')

class attrdict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self

quux = attrdict()
# quux['w']   # KeyError: 'w'
quux.w = 200

from itertools import count

try:
    for num in count(1):
        attrdict({i:i for i in range(1024*1024)})
except MemoryError:
    print('Out of memory after creating {} attrdicts'.format(num))

from gc import collect; collect()

# better formulation
print('#' * 20 + 'better formulation')

class attrdict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

try:
    for num in range(1,150+1):
        attrdict({i:i for i in range(1024*1024)})
except MemoryError:
    print('Out of memory after creating {} attrdicts'.format(num))

print('Survived creating {} attrdicts'.format(num+1))


# ## Problem: Vigenère Cipher
# Implement a Vigenère cipher.Plain text:  attackatdawn
# Key:         python
# Cipher text: prmhqxprwhka

print('#' * 20 + 'Implement a Vigenère cipher.Plain text:  attackatdawn')


#     a b c d e f g h i ...
#     ---------------------
# a | b c d e f g h i j
# b | c d e f g h i j k
# c | d e f g h i j k l
# d | e f g h i j k l m
# ...

# select the corresponding row, then map from the unencoded letter to the encoded letter


CODEBOOK = {
    'a': { 'a': 'b',
           'b': 'c', # ...
         },
    'b': { 'a': 'c',
           'b': 'd',
         },
}

print(CODEBOOK['a']['b'])

from string import ascii_lowercase

CODEBOOK = {x: {} for x in ascii_lowercase}
print(CODEBOOK)
CODEBOOK = {x: {y: None for y in ascii_lowercase} for x in ascii_lowercase}
print(CODEBOOK)
CODEBOOK = {x: {y: None for y in ascii_lowercase} for i, x in enumerate(ascii_lowercase)}
CODEBOOK = {x: {y: ascii_lowercase[(j+i+1) % len(ascii_lowercase)]
                for j,y in enumerate(ascii_lowercase)} for i, x in enumerate(ascii_lowercase)}
print(CODEBOOK)

from itertools import islice, cycle

CODEBOOK = {x: {y: z for y,z in zip(ascii_lowercase, islice(cycle(ascii_lowercase), i, None))}
            for i, x in enumerate(ascii_lowercase)}
print(CODEBOOK)
message = 'a b c 1 2 3'
message = ''.join(m for m in message.lower() if m in CODEBOOK)
print(message)


from string import ascii_lowercase
from itertools import repeat, cycle, islice

CODEBOOK = {x: {y: z for y,z in zip(ascii_lowercase, islice(cycle(ascii_lowercase), i, None))}
            for i, x in enumerate(ascii_lowercase)}

def encipher(message, key, codebook=CODEBOOK):
    message = ''.join(m for m in message.lower() if m in codebook)
    return ''.join(codebook[k][m] for k, m in zip(cycle(key), message))

def decipher(message, key, codebook=CODEBOOK):
    decodebook = {x: {z:y for y,z in yz.items()} for x, yz in codebook.items()}
    return ''.join(decodebook[k][m] for k, m in zip(cycle(key), message))


msg = 'Attack at dawn!'
key = 'python'
enc_msg = encipher(msg, key)
print(enc_msg)
decipher(enc_msg, key)


# ## Problem Statement: Concordance (Word Count)
# Find the ten most commonly used words in a text file.
print('#' * 20 + 'Concordance (Word Count)')


# get_ipython().system(' head -n 10 paradise-lost.txt')


with open('paradise-lost.txt', encoding='utf-8-sig') as f:
    text = ''.join(f)

print(text[:50])

def concordance(text):
    freq = {}
    for word in text.split():
        if word not in freq:
            freq[word] = 0
        freq[word] += 1
    return freq

concordance(text)

from re import sub

def concordance(text):
    freq = {}
    for word in text.split():
        word = sub('[^\w]', '', word.lower())
        if word not in freq:
            freq[word] = 0
        freq[word] += 1
    return freq

freq = concordance(text)
print(sorted(freq.items(), key=lambda kv: kv[1], reverse=True)[:10])

from re import sub

def concordance(text):
    freq = {}
    for word in text.split():
        word = sub('[^\w]', '', word.lower())
        freq[word] = freq.get(word, 0) + 1
    return freq

freq = concordance(text)
print(sorted(freq.items(), key=lambda kv: kv[1], reverse=True)[:10])

from collections import defaultdict

x = defaultdict(int)
print(x['asdfasdf'])
print(x[1])
print(x)

from re import sub
from collections import defaultdict

def concordance(text):
    freq = defaultdict(int)
    for word in text.split():
        word = sub('[^\w]', '', word.lower())
        freq[word] += 1
    return freq

freq = concordance(text)
print(sorted(freq.items(), key=lambda kv: kv[1], reverse=True)[:10])

from collections import Counter
Counter('aabbbc')

from re import sub
from collections import Counter

def concordance(text):
    return Counter(sub('[^\w]', '', word.lower()) for word in text.split())

freq = concordance(text)
print(sorted(freq.items(), key=lambda kv: kv[1], reverse=True)[:10])

