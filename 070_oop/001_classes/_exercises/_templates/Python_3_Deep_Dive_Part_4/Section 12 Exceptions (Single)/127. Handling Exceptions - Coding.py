# # -*- coding: utf-8 -*-
# '''
# ### Handling Exceptions
# '''
#
# '''
# We'll come back to how we can raise exceptions, but we've used it before, so I'll use it again now without explanation,
# just so we can raise some exceptions to examine exception **handling**.
# '''
#
# r.. V..('custom exception')
#
#
# # '''
# # If this exception had occured at the module level when running the module, the Python application would exit.
# # We did not **handle the exception, so the exception propagated all the way to the top and ended up aborting the
# # program execution.
#
#
# '''
# In here though, Jupyter basically handles any exception (prints it out and silences it) so our notebook does not crash!
# (By the way, this is a very good use case for a bare exception handler!)
# Let's try a simple handler first:
# '''
#
# ___
#     r.. V.. custom message
# _____ V.. __ ex:
#     print ?
#
# '''
# As you can see, the string representation of the `ValueError` exception object is just the custom message we supplied
# as an argument to the exception. Most standard exceptions will actually support multiple arguments in their constructor,
# so we can actually do something like this:
# '''
#
# ___
#     r.. V.. 'custom message', 'secondary message'
# _____ V.. __ ex
#     print ?
#
# '''
# Alternatively, we could use the `re..()` of the exception when printing it out:
# '''
#
# ___
#     r.. V.. 'custom message', 'secondary message'
# _____ V.. __ ex
#     print re.. ?
#
# '''
# When we guard code (in a `try` block), we can handle different exception types in separate exception **handlers**:
# '''
#
# ___ func_1
#     r.. V.. bad value
#
# ___
#     func_1
# _____ V.. __ ex
#     print('handling a value error' re.. ?
# _____ I.. __ ex
#     print('handling an index error' re.. ?
#
# '''
# But if `func_1` caused an `I..` exception to be raised, our second handler would catch it:
# '''
#
# ___ func_1
#     r.. I.. bad index
#
# ___
#     func_1
# _____ V.. __ ex
#     print('handling a value error' re.. ?
# _____ I.. __ ex:
#     print('handling an index error' re..?
#
# '''
# The first exception handler that "matches" (subclass!) the exception type will be used - so be careful about not
# catching broad exceptions first. For example, this will not handle the exception in the `ValueError` handler,
# because it is a subclass of `Exception` and that handler is defined first:
# '''
#
# ___
#     r.. V.. value error'
# _____ Exception __ ex
#     print handling Exception' re..?
# _____ V.. __ ex
#     print('handling ValueError' re..?
#
#
# '''
# Note that the exception is still an instance of `ValueError`, but is being handled by the code in the `_____ Exception`
# handler. If we write exception handlers, and none of them match the exception type, then the exception is essentially
# unhandled,  and it will propagate up:
# '''
#
# ___
#     r.. K.. bad key
# _____ V..
#     print('handling value error...'
# _____ I..
#     print('handling index error...')
#
# '''
# The `finally` block is guaranteed to execute, whether an exception is raised or not, and whether it is handled or not!
# '''
#
# ___
#     r.. V..('bad value')
# _____ V..
#     print('handling value error...')
# f___
#     print('running finally...')
#
# '''
# If no exception occurs:
# '''
#
# ___
#     p..
# _____ V..
#     print('handling value error...')
# f___
#     print('running finally...')
#
# '''
# And with an unhandled exception:
# '''
#
# ___
#     r.. V.. bad value
# _____ I..
#     print('handling index error...')
# f___
#     print('running finally...')
#
# '''
# This means that the `finally` block will execute even if there are no exception handlers defined, and whether or not
# an exception is raised:
# '''
#
# ___
#     p..
# f___
#     print('finally...')
#
# ___
#     r.. V..
# f___
#     print('finally...')
#
# '''
# The _____ clause on the other hand is a block that excues if no exceptions occurred - it requires at least one
# _____ clause to be present:
# '''
#
# ___
#     p..
# _____ V..
#     print('value error...')
# ____
#     print('no exception occurred...')
#
# ___
#     r.. V..
# _____ V..
#     print('value error...')
# ____
#     print('no exception occurred...')
#
# ___
#     r.. V..()
# _____ I..:
#     print('index error...')
# ____
#     print('no exception occurred...')
#
# '''
# Some developers often ignore the `else` clause altogether, and write the following:
# '''
#
# ___
#     p..
# _____ V..
#     print('value error...')
# ____
#     print('no exception occurred...')
#
# '''
# this way:
# '''
#
# ___
#     p..
# _____ V..
#     print('value error...')
# print('no exception occurred')
#
# '''
# These two are in fact **not** equivalent!
# What happens if a `ValueError` exception does occur?
# '''
#
# ___
#     r.. V..
# _____ V..
#     print('value error...')
# ____
#     print('no exception occurred...')
#
# ___
#     r.. V..
# _____ V..
#     print('value error...')
# print('no exception occurred')
#
# '''
# As you can see we do **not** have the same functionality.
# `try` statement can be nested. Obviously they can be nested if one `try` clause calls another function that itself
# contains a `try`. But they can also be nested, one within the other directly.
# Let's first see the direct nesting:
# Suppose we want to create a list of `Person` objects from a deserialized `json` object:
# '''
# ______ j..
#
# json_data = """{
#     "Alex": {"age": 18},
#     "Bryan": {"age": 21, "city": "London"},
#     "Guido": {"age": "unknown"}
# }"""
#
# '''
# First we can deserialize the json string into a dictionary:
# '''
#
# data = ____.l.. ?
# print ?
#
# '''
# Next we are going to create a list of `Person` objects, and iterate through the properties of each person in the `data`
# dict and set them directly on the `Person` instance.
# Firstly, the `city` attribute is going to be a problem since `Person` only has two slots defined (`name` and `age`).
# This will be an `AttributeError`.
# Secondly, `Guido`'s age is not a valid value - this is going to cause a `ValueError`.
# '''
#
# c_ Person
#     -s _ 'name', '_age'
#
#     ___ - ____  name
#         ____. ?  ?
#         ____._a.. _ N..
#
#     ?p..
#     ___ age ____
#         r_ ____._a..
#
#     ??.s..
#     ___ age ____ value
#         __ isi.. ? in. an. ? >= 0
#             ____._a.. _ ?
#         ____
#             r.. V.. nvalid age
#
#     ___ -r ____
#         r_ _  *P..|n.._ ____.n..| a.._ ____.age|
#
# '''
# The way we want to handle this is that if some "extra" attributes exist we just want to ignore them, but if a value is
# of the wrong type, we do not want to create the object in our list.
# '''
#
# persons _   # list
# ___ name attributes __ data.it..
#     ___
#         p = P.. n..
#
#         ___ attrib_name attrib_value __ attributes.it..
#             ___
#                 s.. ? a_n a_v
#             _____ A...
#                 print _*ignoring attribute: |n.|a_n _ |a_v
#     _____ V.. __ ex
#         print _*Data for P.. ||n..|| contains an invalid attribute value: |?
#     ____
#         # note that this runs if the outer try does not encounter an exception
#         # since the inner try catches and does not propagate an `AttributeError`
#         # this does not affect this else - the outer try never sees the inner exception
#         # since it was handled (and essentially silenced)
#         ?.ap.. ?
#
# print ?
#
# '''
# While we could certainly handle the `ValueError` in the nested `for` loop, it makes the logic a bit more difficult:
# '''
#
# persons =    # list
# ___ name attributes __ data.it..
#     p _ P.. n..
#
#     ___ attrib_name attrib_value __ at__.it..
#         skip_person _ F..
#         ___
#             s.. ? a_n a_v
#         _____ A..
#             print _*ignoring attribute: |n__.|a_n _ |a_v
#         _____ V.. __ ex
#             print _*Data for P..||na..|| contains an invalid attribute value: |?
#             s.. _ T..
#             b..
#     __ n.. s..
#         ?.ap.. ?
#
# print ?
#
# '''
# Obviously the nested `try` is more elegant, and easier to understand.
# Exception handlers may also be nested a different levels of the call stack, and either an exception is handled, or it
# is propagated up.
# Here we want to create a simple function to transform `0`, `1`, `"0"`, `"1"`, `"T"`, `"F"`, `"True"`, `"False"`,
# `True` and `False` into the equivalent boolean type, __ well __ case insensitive versions of the strings.
# '''
#
# ___ convert_int val
#     __ no. isi.. ? in.  # remember this will work for booleans too!
#         r.. T..
#     __ val no. __ |0, 1   # dict
#         r.. V.. Integer values 0 or 1 only
#     r_ bo.. v..
#
#
# ___ convert_str val
#     __ no. isi.. ? st.
#         r.. T..
#
#     val = ?.c.f.  # for case-insensitive comparisons
#     __ val __ {'0', 'f', 'false'}
#         r_ F..
#     ____ ? __ {'1', 't', 'true'}
#         r_ T..
#     ____
#         r.. V.. Admissible string values are: T, F, True, False (case insensitive)
#
# '''
# Now let's write the main converter function:
# '''
#
# c_ C.. E..
#     p..
#
# ___ make_bool val
#     ___
#         ___
#             b _ c_i ?
#         _____ T..
#             # it wasn't an int/bool, so let's try it __ a string
#             ___
#                 b _ c_s ?
#             _____ T..
#                 r.. C.. _*The type |ty.. ?|. -n| cannot be converted to a bool
#     _____ V.. __ ex
#         # this will catch ValueError exceptions from either convert_int or convert_str
#         r.. C.. _*The value |?| cannot be converted to a bool: |?
#     ____
#         r_ b
#
#
# '''
# The way we have this written, a `C..` exception will be raised, both on a type error, and a value error.
# Notice how we are using exception handling to control the execution flow of our code.
# In particular, we are not testing for conditions prior to attempting something (i.e. we do not check if something is
# an instance of an `int` before calling `convert_int` - we just try it, and catch the exception if that did not work,
# and then proceed to do the same with `convert_str`).
# This is called "asking for forgiveness later". Just try the code, and handle the exception (ask forgiveness) later.
# Now we can convert our values:
# '''
#
# values = [True, 0, 'T', 'false', 10, 'ABC', 1.0]
#
# ___ value in ?
#     ___
#         result _ m.. v..
#     _____ C.. __ ex
#         result _ st. ?
#
#     print v.. r..
#
# '''
# If having three lefvels of nested try's in a single fucntion is too much for you, we could simplify it a little,
# at the expense of some repetitive code (usually not a good idea):
# '''
#
# c_ C.. E..
#     p..
#
# ___ make_bool val
#     ___
#         b _ c_i ?
#     _____ T...
#         p..  # for now we ignore type errors
#     _____ V.. __ ex
#         # it wasn't an int/bool, so let's try it __ a string
#         r.. C.. _f*The value |v..| cannot be converted to a bool: |?
#     ____
#         r_ b
#
#     # reached here so we must have had a type error
#     ___
#         b = c_s ?
#     _____ T..
#         p..  # silence this again
#     _____ V.. __ ex
#         r.. C.. _*The value |v..| cannot be converted to a bool: |?
#     ____
#         r_ b
#
#     # reached here, so neither an int nor a string
#     r.. C.. _*The type |ty..|v__. -n| cannot be converted to a bool
#
#
# values = [True, 0, 'T', 'false', 10, 'ABC', 1.0]
#
# ___ value _ ?
#     ___
#         result _ m_b v..
#     _____ C.. __ ex
#         result = st. ?
#
#     print v.. r..
#
#
# '''
# We could have tried a different strategy here, the "look before you leap" strategy. In this case we try to not to
# cause exceptions by guarding against them.
# Here's an equivalent functionality using this approach. Note that we cannot really break out the `int` and `str`
# conversions cleanly, because we need to test for admissible types and values before we even try the conversion:
# '''
#
# ___ make_bool val
#     __ isi.. ? int.
#         __ ? __ {0, 1}
#             r_ bo.. ?
#         ____
#             r.. C.. Invalid integer value.
#     __ isi.. ? st.
#         __ ?.c.f. __ {'1', 'true', 't'}
#             r_ T..
#         __ v?.c.f. __ {'0', 'false', 'f'}
#             r_ F..
#         r.. C.. Invalid string value
#     r.. C.. Invalid type
#
# values = [True, 0, 'T', 'false', 10, 'ABC', 1.0]
#
# ___ value __ ?
#     ___
#         result _ m_b v..
#     _____ C.. __ ex
#         result _ st. ?
#
#     print v.. r..
#
# '''
# Usually the "ask forgiveness later" approach is favored over the "look before you leap" approach in Python.
# This is sometimes referred to __ **EAFP** - easier to ask for permission.
# But the above example shows you that that is not always clear cut - honestly I think the second version is more
# comprehensible than the first.
# Here's a much clear example. Let's write a function that needs to use an element at some index of a sequence type,
# and use a default value it it's not there:
# The "forgiveness" approach first:
# '''
#
# ___ get_item_forgive_me seq idx default_N..
#     ___
#         r_ ?|?
#     _____ I.. T.. K..
#         # catch either not indexable (TypeError), or index out of bounds,
#         # or even a K.. for mapping types
#         r_ de..
#
# '''
# The "ask permission" first is not that simple! How do we determine if an object is a sequence type?
# '''
#
# ___ get_item_ask_perm seq idx default_N..
#     __ h.. s.. '__getitem__'
#         __ i.. < le. s..
#             r_ s..|i.
#     r_ d..
#
# '''
# The first one works quite well:
# '''
#
# get_item_forgive_me([1, 2, 3], 0)
# get_item_forgive_me([1, 2, 3], 10, 'Nope')
#
# '''
# The second one seems to work ok:
# '''
#
# get_item_ask_perm([1, 2, 3], 0)
# get_item_ask_perm([1, 2, 3], 10, 'Nope')
#
# '''
# But what about this:
# '''
# get_item_forgive_me({'a': 100}, 'a')
# get_item_ask_perm({'a': 1}, 'a')
#
# '''
# So, now we would have to do a lot more work to support getting a key from a mapping using this approach.
# The dictionary has a `__getitem__` method, but does not support numerical indexing.
# We could get bogged down in more and more checks:
# '''
#
# ___ get_item_ask_perm seq idx default_N..
#     __ h.. s.. -g
#         # could be sequence type or mapping type, or something else altogether??
#         __ isi.. s.. di..
#             r_ s__.ge. i.. de..
#         ____ isi.. i.. in.
#             # looks like a numerical index...
#             __ i.. < le. s..
#                 r_ s..|i
#     r_ d..
#
#
# '''
# That fixes the problem somewhat:
# '''
#
# get_item_ask_perm({'a': 100}, 'a')
# get_item_ask_perm([1, 2, 3], 0)
#
# '''
# But now we are also relying on the sequence type having a length!
# '''
# c_ ConstantSequence
#     ___ - ____ val
#         ____.? ?
#
#     ___ -g ____ idx
#         r_ ____.v..
#
# '''
# This is a sequence, an infinite sequence in fact:
# '''
# seq = ConstantSequence(10)
# seq[0]
#
# '''
# And watch what happens with both our functions:
# '''
# get_item_forgive_me(seq, 10, 'Nope')
# get_item_ask_perm(seq, 10, 'Nope')
#
# '''
# And so on, we could really dig ourselves into a hole here. When all we're interested in in making this call `seq[idx]`,
# and using a default if that does not work.
# And that's why EAFP is favored - in Python, we are more interested in can an object perform this type of work, versus
# '''
