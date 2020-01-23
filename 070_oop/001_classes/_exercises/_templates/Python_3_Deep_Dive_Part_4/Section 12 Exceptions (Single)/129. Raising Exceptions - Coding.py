#
# '''
# ### Raising Exceptions
# '''
#
# '''
# An exception workflow can be initiated by using the `raise` statement.
# To *raise* an exception we need to `raise` an **instance** of an exception ty.. (one that is a subclass of
# `BaseException`).
# You cannot raise an instance of a class that is not a subclass of `BaseException`.
# '''
#
# c_ Person
#     p..
#
# ___
#     r... P..
# _____ T... __ ex
#     print(re.. ?
#
# '''
# All the standard exceptions derive from `BaseException` and it allows for any number of positional arguments in
# the initializer (`*args`). The only place those arguments are actually used in `BaseException` is in the `args`
# attribute and the string representations:
# '''
#
# ex = B.. 'a', 'b', 'c'
# ?.args
# st. ?
# re.. ?
#
# '''
# This means that other standard exceptions, that inherit from `BaseException` support this too:
# '''
# ex _ V.. 'a', 'b', 'c'
# print ?.args
# print(st. ?
# print(re.. ?
#
# '''
# Often we only use a single argument, some ty.. of explanatory message, but it is handy to have the option of extra
# arguments available.
# So raising an exception is very easy:
# '''
#
# ___
#     r... V.. some message here
# _____ V.. __ ex
#     print(re.. ?
#
# '''
# But there are some useful variations on the `raise` statement.
# Sometimes we want to catch an exception, try to handle it, maybe because we realize we can't handle that specific
# exception, or because we want to perform some action before letting the exception continue to propagate -
# essentially inserting ourselves in the propagation workflow, but letting it continue once we're done.
# Here's a more concrete example:
# '''
# ___ div a b
#     ___
#         r_ a // b
#     _____ Z.. __ ex
#         print('logging zero division exception: ', ty.. ?. -n ?.a..
#         r...
#
# div(1, 0)
#
# '''
# As you can see, we interrupted the flow, logged what we needed, and resume the propagation flow.
# Sometimes we may want to change the particular exception we are raising - this is particularly useful when using
# custom exceptions, __ we'll cover later.
# But here's what I mean:
# '''
#
# c_ CustomError E..
#     """a custom exception"""
#
# ___ my_funca b
#     ___
#         r_ a // b
#     _____ Z.. __ ex
#         print('logging...')
#         r... C.. ?.a..
#
#
# my_func(1, 0)
#
#
# '''
# So, the exception we obtained was a `CustomError` exception - what we substituted for the `Z..`
# exception that occurred.
# One very important note here, is the traceback.
# Notice how we can see precisely the exception stack - first a `Z..`, that then resulted in a `CustomError`
# exception.
# Whenever we raise an exception in this way, the stack trace of the current exception is maintained and added to our
# new exception being raised.
# We could see this nested more levels:
# '''
#
# ___
#     r... V.. level 1
# _____ V..
#     ___
#         r... T... level 2
#     _____ T...
#         r... K.. level 3
#
# '''
# As you can see the entire stack trace is preserved.
# Sometimes we may want to modify whether we want to keep the original stack trace - we may be writing a function where
# the specific exceptions that result in the final exception we want to raise are implementation details we don't want
# our user to have to wade through.
# In that case, we can squash the current traceback completely, by using raise Exc from None - the from here tells
# Python what traceback to use - in this case `None`.
# Let's see where this might be handy. Remember that set of functions we wrote earlier to convert a value to it's
# boolean equivalent?
# Here it is again:
# '''
#
# c_ ConversionError E..
#     p..
#
# ___ convert_int val
#     __ no. isi.. ? in.  # remember this will work for booleans too!
#         r... T...
#     __ val no. __ {0, 1}
#         r... V.. Integer values 0 or 1 only
#     r_ bo.. ?
#
# ___ convert_str val
#     __ no. isi.. ? st.
#         r... T...
#
#     val _ ?.c.f.  # for case-insensitive comparisons
#     __ val __ {'0', 'f', 'false'}
#         r_ F..
#     ____ ? __ {'1', 't', 'true'}
#         r_ T..
#     ____
#         r... V.. Admissible string values are: T, F, True, False (case insensitive)
#
# ___ make_bool val
#     ___
#         ___
#             b _ c_i ?
#         _____ T...
#             # it wasn't an int/bool, so let's try it __ a string
#             ___
#                 b _ c_s ?
#             _____ T...
#                 r... C.. _*The ty.. |ty..|v..|. -n| cannot be converted to a bool
#     _____ V.. __ ex:
#         # this will catch V.. exceptions from either convert_int or convert_str
#         r... C.. _*The value |v..| cannot be converted to a bool: |?
#     ____
#         r_ b
#
# '''
# And when we call the function with a bad value:
# '''
#
# make_bool('ABC')
#
# '''
# Notice how the stack trace is quite complicated. Do we really want users of our function to see this? The internal
# implementation details of our function is not of interest to them, we just want to raise a "clean" `ConversionError`
# exception.
# We can do so by using `from None` when we raise our custom exception:
# '''
#
# c_ ConversionError E..
#     p..
#
# ___ convert_int val
#     __ no. isi.. ? in.   # remember this will work for booleans too!
#         r... T...
#     __ ? no. __ {0, 1
#         r... V.. Integer values 0 or 1 only
#     r_ bo.. ?
#
# ___ convert_str val
#     __ no. isi.. ? st.
#         r... T...
#
#     val _ ?.c.f.  # for case-insensitive comparisons
#     __ ? __ {'0', 'f', 'false'}
#         r_ F..
#     __ ? _ {'1', 't', 'true'
#         r_ T..
#     ____
#         r... V.. Admissible string values are: T, F, True, False (case insensitive)
#
# ___ make_bool val
#     ___
#         ___
#             b _ c_i ?
#         _____ T...
#             # it wasn't an int/bool, so let's try it __ a string
#             ___
#                 b _ c_s ?
#             _____ T...
#                 r... C.. _*The ty.. |ty..|v..|. -n| cannot be converted to a bool') f.. N..
#     _____ V.. __ ex
#         # this will catch V.. exceptions from either convert_int or convert_str
#         r... C.. _*The value |v..| cannot be converted to a bool: |? f.. N..
#     ____
#         r_ b
#
# make_bool('ABC')
# make_bool(1.0)
#
# '''
# As you can see, the traceback is much cleaner.
# We can also be very specific __ to which traceback to use when we raise an exception.
# '''
#
# ___
#     r... V.. level 1
# _____ V.. __ ex_1
#     ___
#         r... V.. level 2
#     _____ V.. __ ex_2
#         ___
#             r... V.. level 3
#         _____ V.. __ ex_3
#             r... V..( value error occurred
#
# '''
# Notice how the traceback contains the entire exception stack. We could of course remove it entirely:
# '''
#
# ___
#     r... V.. level 1
# _____ V.. __ ex_1
#     ___
#         r... V.. level 2
#     _____ V.. __ ex_2
#         ___
#             r... V.. level 3
#         _____ V.. __ ex_:
#             r... V..('value error occurred') f.. N..
#
# '''
# But we could also choose to only skip `level2` by using the traceback from `level1`:
# '''
#
# ___
#     r... V.. level 1
# _____ V.. __ ex_1
#     ___
#         r... V.. level 2
#     _____ V.. __ ex_2
#         ___
#             r... V.. level 3
#         _____ V.. __ ex_3
#             r... V..('value error occurred') f.. ex_1
#
# '''
# As you can see, we used the traceback from `ex_1` when we raised our final `V..`.
# This can be useful if you trap some exception, try to handle it, and in the process cause another exception to
# be raised.
# When you handle that secondary exception, you may very well consider it an implementation detail and wish to shield
# the user from that particular exception - but the original one is important enough to include it in the traceback.
# Let's look at an example that uses the `convert_int` function from earlier. We know that if we p.. it a non-integer
# value, it will give us a ty.. exception:
# '''
#
# convert_int(1.0)
#
# '''
# Now suppose we are writing a function that makes use of it:
# '''
#
# ___ calc b
#     ___
#         b_bool _ c_i b
#     _____ T... __ _1
#         # bad ty.., but maybe it was a float and we could try to convert it to an int first
#         ___
#             b_int _ in. b
#         _____ V.. T...
#             r... Cu.. Bad ty..
#
#         b_bool _ c_i b_
#
#     r_ b_b
#
# calc(1), calc(0)
# calc(1.0)
# calc('A')
#
# '''
# As you can see we get an ugly stack trace here, that includes the exception when we tried to cast our argument
# to an int. We can hide it by using the traceback from `ex_1` instead:
# '''
#
# ___ calc b
#     ___
#         b_bool = c_i ?
#     _____ T... __ _1
#         # bad ty.., but maybe it was a float and we could try to convert it to an int first
#         ___
#             b_int _ in. ?
#         _____ V.. T...
#             r... C.. 'Bad ty..'? from ex_1
#
#         b_bool = c_i b_i
#
#     r_ b_b..
# 
#
# calc('ab')
