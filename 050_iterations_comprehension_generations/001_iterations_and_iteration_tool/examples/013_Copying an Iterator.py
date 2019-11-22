# "Copying" an Iterator
# Sometimes we may have an iterator that we want to use multiple times for some reason.
# As we saw, iterators get exhausted, so
# simply making multiple references to the same iterator will not work -
# they will just point to the same iterator object.
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
# As you can see, iter1, iter2, and iter3 are essentially three independent "copies" of our original
# iterator (squares(10))
# Note that this works for any iterable, so even sequence types such as lists:
# But you'll notice that the elements of lists are not lists themselves!
#
# As you can see, the elements returned by tee are actually iterators -
# even if we used an iterable such as a list to start off with!

l = [1, 2, 3, 4]
lists = tee(l, 2)
lists[0]
lists[1]

list(lists[0])
list(lists[0])

lists[1] is lists[1].__iter__()
'__next__' in dir(lists[1])
