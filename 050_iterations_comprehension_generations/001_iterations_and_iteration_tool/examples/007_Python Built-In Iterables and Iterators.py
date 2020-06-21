# Python Built-In Iterables and Iterators
# for the list
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
# To iterate over the values, we could use the values() method which returns an iterable over the values of the dictionary:
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

# Python's Built-In Iterables and Iterators
# Let's look at the simple range function first:
# But it is not an iterator:
# However, we can request an iterator by calling the __iter__ method, or simply using the iter() function:
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
# Even reading a file line by line is done using lazy evaluation:
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
