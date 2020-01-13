# # Python Built-In Iterables and Iterators
# # for the list
# # Since the list l is an iterable it also implements the __iter__ method:
# # Of course, since lists are also sequence types, they also implement the __getitem__ method:
#
# l _ 1 2 3  # list
# iter_l _ it__ l
# #or could use iter_1 = l.__iter__()
# ty__ iter_l
# n____ iter_l
# n____ iter_l
# n____ iter_l
#
# '__iter__' i_ di. l
# '__getitem__' i_ di. l
#
# # But what does the iterator for a dictionary actually return?
# # To iterate over the values, we could use the values() method which returns an iterable over the values of the dictionary:
# # And to iterate over both the keys and values, dictionaries provide an items() iterable:
#
# d _ di__ a_1 b_2 c_3
# iter_d _ it__ d
# n____ i.._d
#
# # Dictionary iterators will iterate over the keys of the dictionary.
#
# iter_vals _ it__ d.va..
# n____ i.._v..
#
# iter_items _ it__ d.it...
# n____ i._i.
#
# # Cyclic Iterators
#
# c_ CyclicIterator
#     ___ __init__ ____ lst
#         ____.l.. _ lst
#         ____.i _ 0
#
#     ___ __iter__ ____
#         r_ ____
#
#     ___ __next__(self):
#         result = self.lst[self.i % len(self.lst)]
#         self.i += 1
#         r_ result
#
# iter_cycl _ C..I. NSWE
#
# ___ i i_ ra___10
#     print n____ i___c__
# #
# n _ 10
# iter_cycl _ C...  NSWE
# ___ i i_ ra___ 1 n+1
#     direction _ n____ iter_cycl
#     print _*|i||d...|*
#
# # Python's Built-In Iterables and Iterators
# # Let's look at the simple range function first:
# # But it is not an iterator:
# # However, we can request an iterator by calling the __iter__ method, or simply using the iter() function:
# # And of course this is now an iterator:
#
# r_10 _ n____ 10
# '__iter__' i_ di. r_10
#
# '__next__' i_ di. r_10
#
# r_10_iter = it__ r_10
#
# '__iter__' i_ di. r_10_iter
#
# '__next__' i_ di. r_10_iter
#
#
# # Python's Built-In Iterables and Iterators
# # zip
# # Just like range() though, it also uses lazy evaluation, so we need to iterate through the iterator and make a list
# # for example in order to see the contents:
# # Even reading a file line by line is done using lazy evaluation:
# # As you can see, the open() function returns an iterator (of type TextIOWrapper), and we can read lines from the file
# # one by one using the next() function, or calling the __next__() method. The class also implements a readline()
# # method we can use to get the next row:
#
# z _ zi. 1 2 3|; 'abc'
# z
# print '__iter__' i_ di. z
# print '__next__' i_ di. z
#
# li__(z)
#
# w____ o... cars.csv a_ f
#     print ty__ f
#     print '__iter__' i_ di. f
#     print('__next__' i_ di.f
#
# w___ o... cars.csv a_ f
#     print n____ f
#     print f.__n___
#     print f.r...
#
# # Python's Built-In Iterables and Iterators
# # The enumerate function is another lazy iterator:
# #
# # As we can see, the object and its iterator are the same object.
# #
# # But enumerate is also lazy, so we need to iterate through it in order to recover all the elements:
# # Of course, once we have exhausted the iterator, we cannot use it again:
#
# e _ en___ Python rocks!
#
# print '__iter__' i_ di. e
# print '__next__' i_ di. e
#
# it.. e
# e
# li__ e
# li__ e
#
# # Python's Built-In Iterables and Iterators
# # The dictionary object provides methods that return iterables for the keys, values or tuples of key/value pairs:
# #
# # More simply, we can just test to see if iter(keys) is the same object as keys - if not then we are dealing with an iterable.
#
# d _  'a' 1 'b' 2   # dictionary
# keys _ d.k..
# '__iter__' i_ di. k..; '__next__' i_ di. k...
# it__ k... i_ k...
