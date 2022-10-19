# """
# * counter
# * defaultdict
# * ordereddict
# * namedtuple
# * deque
#
# The main purpose of this video is to make you aware that these things exist, in case we have to use them later on (
# or when you encounter a situation where using one of these would be useful).
#
# Normally what happens in those situations is we struggle to build our own thing to do what we need it to do.
# Knowing that these exist could save you a lot of effort!
# """
#
# # # Counter
# """
# Allows us to count things. Give it a iterable or a mapping (such as a dict) and it will turn into a counter of elements.
# """
#
# ____ c... ____ C..
#
# device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]
#
# temperature_counter = C.. ?
# print ?[14.0])  # 2
#
# # # defaultdict
# """
# The `defaultdict` never raises a `KeyError`.
# Instead, it returns the value returned by the function specified when the object was instantiated.
# """
#
# alma_maters     # dict
#
# ___ coworker __ coworkers
#     __ ? 0 __ ?
#         ? ? 0     # list
#     ? ? 0 .a.. ?1
#
#
# ____ c... ____ d..
#
# coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]  #  Rolf got a master's
#
# coworker_alma_maters = d..(list)  # remember list is a function, returns []
#
# ___ coworker, place __ ?
#     ? ? .a.. ?
#
# print(?['Rolf'])
# print(?['Anne'])  # []
#
# """
# When you need a dictionary and all keys of that dictionary should be associated with an initial value,
# use `defaultdict`!
#
# Another example is to initialise places where coworkers work:
# """
#
# ____ c... ____ d..
#
# my_company = 'Teclado'
#
# coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
# other_coworkers = [('Rolf', 'Apple Inc.'), ('Anna', 'Google')]
#
# coworker_companies = d.. l__ m..
#
# ___ person, company __ o..
#     ? ? _ ?
#
# print(?['Jen'])  # Teclado
# print(?['Rolf'])  # Apple Inc.
#
# """
# If you want to change the default value in a `defaultdict`, just change its `default_factory` property:
# """
#
# ____ c... ____ d..
#
# int_dict = d..(int)
#
# ?['first'] += 1
# print(?['first'])  # 1
#
# ?.d.. = list
# ?['second'].a..('Rolf')
# print(?['second'])  # ['Rolf']
#
# ?.d.. = N..  # this is back to being a "normal dictionary"
#
# # # OrderedDict
#
# ____ c... ____ O..
#
# o = O..
# ? 'Rolf'] = 6
# ? 'Jose'] = 10
# ? 'Jen'] = 3
#
# print(o)  # keys are always in the order in which they were inserted
#
# ?.m.. ('Rolf')
# ?.m..('Jose', last=False)
#
# print ?
#
# ?.p..
#
# print ?
#
# """
# As of Python3.7, I expected `OrderedDict` to be less useful since dictionaries themselves will retain the order in
# which keys are inserted.
# """
#
# ## namedtuple
# """
# A namedtuple is another object that we can use like a tuple, where each of the elements of the tuple has a name.
# In addition, the tuple itself also has a name.
#
# It improves on tuples by making more explicit what it means.
#
# Take this as an example using normal tuples:
# """
#
# account = ('checking', 1850.90)
#
# print(?[0])  # name
# print(?[1])  # balance
#
# """
# Or, the explicitness of `namedtuple`:
# """
#
# ____ c... ____ n..
#
# Account = n..('Account', ['name', 'balance'])
#
# account = ?('checking', 1850.90)
# print ?.n..
# print ?.b..
#
# # Or even print the account itself with a nice __repr__
# print ?
#
# """
# I like to think of it very much like defining a class (where `Account` is the class or the type).
# However, remember it’s not quite the same, and a `namedtuple` is still a tuple after all.
#
# You can do things like these:
# """
#
# name, balance = account  # tuple destructuring
#
# ? ('checking', balance=1850.90)  # use positional or named arguments
#
# ?._m.. 'checking', 1850.90))
#
# accounts = [
#     ('checking', 1850.90),
#     ('savings', 3658.00),
#     ('credit', -450.00)
# ]
#
# account_tuples  m.. A__._m.. ?
#
# ?._a  # returns an OrderedDict representing the tuple
#
# """
# When you’re dealing with data and it doesn’t warrant creating classes for the data elements you’re working with,
# `namedtuple` is a great choice (and very flexible!).
# """
#
# # # Deque
# """
# The last element we’ll look at today is the `deque`, which stands for “Double-ended queue”.
#
# (Watch presentation about queues if you haven’t already).
#
# In a `deque`, we can push elements at the start or the end, and we can also remove elements from the start or the end.
#
# It is very efficient, performing very well, and also it’s thread-safe (we’ll be looking at threads soon!).
#
# When we look at asynchronous development, we’ll be talking more about the `deque` as we use it.
# For now, just remember it’s like a list on which you do operations like a list:
# """
#
# ____ c... ____ d..
#
# friends = d..(('Rolf', 'Charlie', 'Jen', 'Anna'))
# ?.a.. 'Jose'
# ?.a.. 'Anthony'
#
# print ?
#
# ?.p..
# print ?
#
# ?.p..
# print ?
#
# """
# For more info on deques and a comprehensive example on everything you can with it,
# check out the official Python documentation: [8.3. collections — Container datatypes — Python 3.6.4 documentation]
# """