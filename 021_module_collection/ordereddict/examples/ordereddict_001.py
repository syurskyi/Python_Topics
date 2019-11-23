# OrderedDict
#
# Prior to Python 3.7, dictionary key order was not guaranteed. This became part of the language in 3.7,
# so the usefullness of this OrderedDict is diminished - but necessary if you want your dictionaries to maintain key
# order and be compatible with Python versions earlier then 3.6 (technically dicts are ordered in 3.6 as well,
# but it was considered an implementation detail, and not actually guaranteed).
#
# We'll come back to a direct comparison of OrderedDict and plain dict in a subsequent video. For now let's look at
# the OrderedDict as if we were targeting our code to be compatible with earlier versions of Python.

from collections import OrderedDict

# Once again, OrderedDict is a subclass of dict.
#
# We can also pass keyword arguments to the constructor. However, in Python versions prior to 3.5, the order of
# the arguments is not guaranteed to be preserved - so to be fully backward-compatible, insert keys into the dictionary
# after you have created it as an empty dictionary.

d = OrderedDict()
d['z'] = 'hello'
d['y'] = 'world'
d['a'] = 'python'
d
# OrderedDict([('z', 'hello'), ('y', 'world'), ('a', 'python')])

# And if we iterate through the keys of the OrderedDict we will retain that key order as well:

for key in d:
    print(key)

# z
# y
# a

# The OrderedDict also supports reverse iteration using reversed():

for key in reversed(d):
    print(key)

# a
# y
# z

# This is not the case for a standard dictionary, even in Python 3.5+ where key order is maintained!
# In the next video we'll dig a little more into a comparison between OrderedDicts and dicts.

d = {'a': 1, 'b': 2}
# for key in reversed(d):
#     print(key)      # ERROR TypeError: 'dict' object is not reversible

# OrderedDicts are a subclass of dicts so all the usual operations and methods apply,
# but OrderedDicts have a couple of extra methods available to us:
#
#     popitem(last=True)
#     move_to_end(key, last=True)
#
# Since an OrderedDict has an ordering, it is natural to think of the first or last element in the dictionary.
#
# The popitem allows us to remove the last (by default) or first item (setting last=False):

d = OrderedDict()
d['first'] = 10
d['second'] = 20
d['third'] = 30
d['last'] = 40
d
# OrderedDict([('first', 10), ('second', 20), ('third', 30), ('last', 40)])

d.popitem()
# ('last', 40)

d
# OrderedDict([('first', 10), ('second', 20), ('third', 30)])

# As you can see the last item was popped off (and returned as a key/value tuple). To pop the first item we can do this:

d.popitem(last=False)
# ('first', 10)

d
# OrderedDict([('second', 20), ('third', 30)])

# The move_to_end method simply moves the specified key to the end (by default), or to the beginning
# (if last=False is specified) of the dictionary:

d = OrderedDict()
d['first'] = 10
d['second'] = 20
d['third'] = 30
d['last'] = 40
d.move_to_end('second')
d
# OrderedDict([('first', 10), ('third', 30), ('last', 40), ('second', 20)])

d.move_to_end('third', last=False)
d
# OrderedDict([('third', 30), ('first', 10), ('last', 40), ('second', 20)])

# Be careful if you specify a non-existent key, you will get an exception:

d.move_to_end('x')  # ERROR  KeyError: 'x'
