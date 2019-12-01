# # %%
# '''
# ### Class and Static Methods
# '''
#
# # %%
# '''
# Asd we saw, when we define a function inside a class, how it behaves (as a function or a method) depends on how
# the function is accessed: from the class, or from the instance. (We'll cover how that works when we look at descriptors
# later in this course).
# '''
#
# # %%
# c_ Person:
#     ___ hello ar._'default'
#         print _ Hello, with arg_|ar.
#
# # %%
# '''
# If we call `hello` from the class:
# '''
#
# # %%
# ?.h...
#
# # %%
# '''
# You'll notice that `hello` was called without any arguments, in fact, `hello` is a regular function:
# '''
#
# # %%
# print ?.h...
#
# # %%
# '''
# But if we call `hello` from an instance, things are different:
# '''
#
# # %%
# p _ ?
#
# # %%
# print ?.h...
#
# # %%
# ?.h...
#
# # %%
# hex(id(p))
#
# # %%
# '''
# And as you can see the instance `p` was passed as an argument to `hello`.
# Sometimes however, we define functions in a class that do not interact with the instance itself, but may need something
# from the class. In those cases, we want the class to be passed to the function as an argument, whether it is called
# from the class or from an instance of the class.
# These are called **class methods**. You'll note that the behavior needs to be different - we don't want the instance
# to be passed to the function when called from an instance, we want the **class** to be passed to it. In addition,
# when called from the class, we **also** want the class to be passed to it (this is similar to `static` methods in
# Java, not to be confused with, as we'll see in a bit, static methods in Python).
# We use the `@classmethod` decorator to define class methods, and the first argument of these methods will always be
# the class where the method is defined.
# '''
#
# # %%
# '''
# Let's see a simple example first:
# '''
#
# # %%
# c_ MyClass
#     ___ hello
#         # this IS an instance method, we just forgot to add a parameter to capture the instance
#         # when this is called from an instance - so this will fail
#         print('hello...')
#
#     ___ instance_hello a..
#         print _ hello from  |a..
#
#     0c.
#     ___ class_hello(arg):
#         print _ hello from |a..
#
#
# # %%
# m _ ?
#
# # %%
# ?.h...
#
# # %%
# '''
# But, as expected, this won't work:
# '''
#
# # %%
# t__
#     m.h...
# e___ T... a_ ex
#     print ?
#
# # %%
# '''
# On the other hand, notice now the instance method when called from the instance and the class:
# '''
#
# # %%
# ?.in..
#
# # %%
# t__
#     M__.i..
# e___ T... a_ ex
#     print ?
#
# # %%
# '''
# As you can see, the instance method needs to be called from the instance. If we call it from the class, no argument
# is passed to the function, so we end up with an exception.
# This is not the case with class methods - whether we call the method from the class, or the instance, that first
# argument will always be provided by Python, and will be the class object (not the instance).
# Notice how the bindings are different:
# '''
#
# # %%
# print(?.class_hello)
#
# # %%
# print ?.c..
#
# # %%
# '''
# As you can see in both these cases, `class_hello` is bound to the class.
# But with an instance method, the bindings behave differently:
# '''
#
# # %%
# print ?.in..
#
# # %%
# print ?.in..
# # %%
# '''
# So, whenever we call `class_hello` the method is bound to the **class**, and the first argument is the class:
# '''
#
# # %%
# ?.c..
#
# # %%
# m.c..
#
# # %%
# '''
# Although in this example I used `arg` as the parameter name in our methods, the normal **convention** is to use `self`
# and `cls` - that way everyone knows what we're talking about!
# '''
#
# # %%
# '''
# We sometimes also want to define functions in a class and always have them be just that - functions, never bound to
# either the class or the instance, however we call them. Often we do this because we need to utility function that is
# specific to our class, and we want to keep our class self-contained, or maybe we're writing a library of functions
# (though modules and packages may be more appropriate for this).
# '''
#
# # %%
# '''
# These are called **static** methods. (So be careful here, Python static methods and Java static methods do not have
# the same meaning!)
# '''
#
# # %%
# '''
# We can define static methods using the `@staticmethod` decorator:
# '''
#
# # %%
# c_ MyClass
#     ___ instance_hello ____
#         print _ Instance method bound to |____
#
#     0c.
#     ___ class_hello cl.
#         print _ Class method bound to |cl.
#
#     0s..
#     ___ static_hello
#         print('Static method not bound to anything')
#
# # %%
# m = ?
#
# # %%
# ?.i...
#
# # %%
# ?.c..
#
# # %%
# ?.c..
#
# # %%
# '''
# And the static method can be called either from the class or the instance, but is never bound:
# '''
#
# # %%
# print ?.s..
#
# # %%
# print ?.s..
#
# # %%
# ?.s..
#
# # %%
# m.s..
#
# # %%
# '''
# #### Example
# '''
#
# # %%
# '''
# Let's see a more concrete example of using these different method types.
# We're going to create a `Timer` class that will allow us to get the current time (in both UTC and some timezone),
# as well as record start/stop times.
# We want to have the same timezone for all instances of our `Timer` class with an easy way to change the timezone for
# all instances when needed.
# If you need to work with timezones, I recommend you use the `pyrz` 3rd party library. Here, I'll just use the standard
# library, which is definitely not as easy to use as `pytz`.
# '''
#
# # %%
# f___ da..ti.. ______ da..ti.. ti..zo.. ti..de..
#
# c_ Timer
#     tz _ t_z_.ut.  # class variable to store the timezone - default to UTC
#
#     0c.
#     ___ set_tz cls offset name
#         c__.t. _ t.z. t..d.. hou.._off..  n..
#
# # %%
# '''
# So `tz` is a class attribute, and we can set it using a class method `set_timezone` - any instances will share the same
# `tz` value (unless we override it at the instance level)
# '''
#
# # %%
# ?.s.. -7 MST
#
# # %%
# print ?.t.
#
# # %%
# t1 _ ?
# t2 _ ?
#
# # %%
# print(_1.tz, _2.t.
#
# # %%
# ?.s.._t. -8 PST
#
# # %%
# print(_1.t., _2.t.
#
# # %%
# '''
# Next we want a function to return the current UTC time. Obviously this has nothing to do with either the class or
# the instance, so it is a prime candidate for a static method:
# '''
#
# # %%
# c_ Timer
#     tz _ t..z_.u.  # class variable to store the timezone - default to UTC
#
#     0s..
#     ___ current_dt_utc
#         r_ d.t_.n.. t.z_.u..
#
#     0c.
#     ___ set_tz cls offset name
#         cl_.t. _ t.z_(t..d.. hou.._off.. n..
#
# # %%
# ?.cu..
#
# # %%
# t + ?
#
# # %%
# ?.cu..
#
# # %%
# '''
# Next we want a method that will return the current time based on the set time zone. Obviously the time zone
# is a class variable, so we'll need to access that, but we don't need any instance data, so this is a prime candidate
# for a class method:
# '''
#
# # %%
# c_ Timer
#     tz _ t.z_.u..  # class variable to store the timezone - default to UTC
#
#     0s..
#     ___ current_dt_utc
#         r_ d_t_.n.. t.z_.u..
#
#     0c.
#     ___ set_tz cls offset name
#         cl_.t. _ t.z_(t..d.. h.._off.. n..
#
#     0c.
#     ___ current_dt cls
#         r_ d.t_.n. cl_.t.
#
# # %%
# ?.cu.. ?.cu.._d
#
# # %%
# t1 _ ?
# t2 _ ?
#
# # %%
# _1.cu.. _1.cu.._d.
#
# # %%
# _2.cu..
#
# # %%
# '''
# And if we change the time zone (we can do so either via the class or the instance, no difference, since the `set_tz`
# method is always bound to the class):
# '''
#
# # %%
# _2.s._t. -7 MST
#
# # %%
# print ?.-d
#
# # %%
# ?.cu._d_u., ?.cu.._d. _1.cu.._d. _2.cu.._d
#
# # %%
# '''
# So far we have not needed any instances to work with this class!
# Now we're going to add functionality to start/stop a timer. Obviously we want this to be instance based,
# since we want to be able to create multiple timers.
# '''
#
# # %%
# c_ TimerError E...
#     """A custom exception used for Timer class"""
#     # (since """...""" is a statement, we don't need to pass)
#
# c_ Timer
#     tz _ t.z_.ut.  # class variable to store the timezone - default to UTC
#
#     ___ -  ____
#         # use these instance variables to keep track of start/end times
#         ____._time_start _ N...
#         ____._time_end _ N...
#
#     0s..
#     ___ current_dt_utc
#         """Returns non-naive current UTC"""
#         r_ d.t_.n. t.z_.ut.
#
#     0c.
#     ___ set_tz cls offset name
#         cl_.t. _ t.z_ t..d..hou.. _ off.. n..
#
#     0c.
#     ___ current_dt cl.
#         r_ d.t_.n.. cl_.t.
#
#     ___ start ____
#         # internally we always non-naive UTC
#         ____._time_start _ ____.cu..
#         ____._time_end _ N...
#
#     ___ stop ____
#         i_ ____._ti.._st.. i_ N...
#             # cannot stop if timer was not started!
#             r_ T... ('Timer must be started before it can be stopped.')
#         ____._time_end _ ____.cu..
#
#     0p...
#     ___ start_time ____
#         i_ ____._ti.._st.. i_ N...
#             r__ T...('Timer has not been started.')
#         # since tz is a class variable, we can just as easily access it from ____
#         r_ ____._ti._st_.a.t..z. ____.t.
#
#     0p..
#     ___ end_time ____
#         i_ ____._time_end i_ N...
#             r___ T....('Timer has not been stopped.')
#         r_ ____._time_end.a.ti..z.. ____.t.
#
#     0p...
#     ___ elapsed ____
#         i_ ____._time_start i_ N...
#             r_ T...('Timer must be started before an elapsed time is available')
#
#         i_ ____._time_end i_ N...
#             # timer has not ben stopped, calculate elapsed between start and now
#             elapsed_time _ ____.cu.. - ____._ti.._st..
#         e___
#             # timer has been stopped, calculate elapsed between start and end
#             elapsed_time _ ____._ti.._e.. - ____._ti.._st..
#
#         r_ el.._ti__.to.._se..
#
# # %%
# f___ ti.. ______ sl..
#
# t1 _ ?
# _1.st..
# sl... 2
# _1.st..
# print _ Start time: |_1.st.._t..
# print _ End time: |_1.e.._ti..
# print _ Elapsed: |_1.ela.. sec..
#
# # %%
# t2 _ ?
# _2.st..
# sl.. 3
# _2.st..
# print _ Start time: |_2.st.._ti..
# print _ End time: |_2.en._ti..
# print _ Elapsed: |_2.el.. sec..
#
# # %%
# '''
# So our timer works. Furthermore, we want to use `MST` throughout our application, so we'll set it, and since it's
# a class level attribute, we only need to change it once:
# '''
#
# # %%
# ?.set_t. -7 MST
#
# # %%
# print _ Start time: |_1.st.._ti..
# print _ End time: |_1.en._ti..
# print _ Elapsed: |_1.el.. sec..
#
# # %%
# print _ Start time: |_2.st.._ti..
# print _ End time: |_2.en._ti..
# print _ Elapsed: |_2.el.. sec..
#
# # %%
