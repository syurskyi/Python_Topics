# # %%
# '''
# ### Properties and Descriptors
# '''
#
# # %%
# '''
# Let's start by creating a property using the decorator syntax:
# '''
#
# # %%
# ____ numbers ______ Inte...
#
# c_ Person
#     ??
#     ___ age ?
#         r_ ge.. ? '_age', N..
#
#     ??.?
#     ___ age ? value
#         __ no isi.. ? I..
#             r... V...('age: must be an integer.')
#         __ ? < 0
#             r... V...('age: must be a non-negative integer.')
#         ?._a.. ?
#
# # %%
# p = ?
#
# # %%
# ___
#     ?.a.. = -10
# ______ V... __ ex
#     print ?
#
# # %%
# '''
# And notice how the instance dictionary does not contain `age`, even though we have that instance `age` attribute:
# '''
#
# # %%
# p.age = 10
#
# # %%
# p.age, p.__dict__
#
# # %%
# '''
# Next, let's rewrite this using a `property` class instead of the decorators:
# '''
#
# # %%
# c_ Person
#     ___ get_age ?
#         r_ ge..  '_age', N..)
#
#     ___ set_age  value
#         __ no. isi..(?, I..
#             r... V...('age: must be an integer.')
#         __ ? < 0
#             r... V...('age: must be a non-negative integer.')
#         ?._a..  ?
#
#     age = ? fget_g.. fset_s..
#
# # %%
# '''
# And this works the exact same way as before:
# '''
#
# # %%
# p = ?
#
# # %%
# ___
#     ?.a.. _ -10
# ______ V... __ ex
#     print ?
#
# # %%
# p.age = 10
#
# # %%
# p.age, p.__dict__
#
# # %%
# '''
# Now, in both cases the property object instance can be accessed by using the class:
# '''
#
# # %%
# prop = Person.age
#
# # %%
# prop
#
# # %%
# '''
# And this property, is actually a data descriptor!
# '''
#
# # %%
# hasattr(prop, '__set__')
#
# # %%
# hasattr(prop, '__get__')
#
# # %%
# '''
# In this case, our property has both the `__get__` and `__set__` methods so we ended up with a data descriptor.
# '''
#
# # %%
# '''
# Even if we only defined a read-only property, we would still end up with a data descriptor:
# '''
#
# # %%
# ____ d_t_ ______ d_t_
#
# c_ TimeUTC
#     ??
#     ___ current_time ?
#         r_ d_t_.u_n_.iso..
#
# # %%
# t = TimeUTC
# ?.c..
#
# # %%
# prop = T__.c..
#
# # %%
# hasattr(prop, '__get__')
#
# # %%
# hasattr(prop, '__set__')
#
# # %%
# '''
# But the internal implemetation of the `__set__` method would refuse to set a value:
# '''
#
# # %%
# ___
#     ?.c.. = d_t_.u__.is...
# ______ A.. _ ex
#     print ?
#
# # %%
# '''
# So, if properties are implemented using data descriptors - this means that instance attributes with the same name will
# not shadow the descriptor:
# '''
#
# # %%
# t.__dict__
#
# # %%
# t.__dict__['current_time'] = 'not a time'
#
# # %%
# t.__dict__
#
# # %%
# t.current_time
#
# # %%
# '''
# OK, so given what we know about data descriptors all this should make sense.
# '''
#
# # %%
# '''
# Now let's try to implement our own version of the property type, decorators and all!
# '''
#
# # %%
# c_ MakeProperty
#     ___ -  fget_N.. fset_N..
#         ?  ?
#         ?  ?
#
#     ___ __set_name__  owner_class prop_name
#         ?p.. _ p..
#
#     ___ __get__ instance owner_class
#         print('__get__ called...')
#         __ ins.. i. N..
#             r_ ?
#         __ ?f.. __ N..
#             r... A_ _*|?p.. i. no. readable.')
#         r_ ?f.. i..
#
#     ___ __set__ instance value
#         print('__set__ called...')
#         __ ?f.. __ N..
#             r... A.. _*?p..| i. no. writable.')
#         ?f.. i.. ?
#
# # %%
# '''
# This is now sufficient to start creating properties using this data descriptor:
# '''
#
# # %%
# c_ Person
#     ___ get_name ?
#         r_ ?_n..
#
#     ___ set_name ? value
#         ?_name _ ?
#
#     name _ MP.. fget_g.. fset_s..
#
# # %%
# p = ?
#
# # %%
# p.__dict__
#
# # %%
# p.name = 'Guido'
#
# # %%
# p.name
#
# # %%
# '''
# And even if we try to shadow the property name in the instance, things will work just fine:
# '''
#
# # %%
# p.__dict__['name'] = 'Alex'
#
# # %%
# p.__dict__
#
# # %%
# p.name
#
# # %%
# '''
# Next we would like to have a decorator approach as well. To do that we're going to mimic the way the property
# decorators work (you may want to go back to those lectures and refresh your memory if needed).
# '''
#
# # %%
# '''
# So how should the `@MakeProperty` decorator work?
# It should take a function and return a descriptor object.
# In turn, that descriptor object should have a `setter` method that we can call to *add* the setter method
# to the descriptor, that also returns the descriptor object - just like we have with `property` types:
# '''
#
# # %%
# c_ MakeProperty
#     ___ -  fget_N.. fset_N..
#         ?  ?
#         ?  ?
#
#     ___ __set_name__  owner_class prop_name
#         ?p.. _ p..
#
#     ___ __get__  instance owner_class
#         print('__get__ called...')
#         __ i.. i. N..
#             r_ ?
#         __ ?f.. __ N..
#             r... A.. _* ?p..| i. no. readable.')
#         r_ ?f.. i..
#
#     ___ __set__ instance, value
#         print('__set__ called...')
#         __ ?f.. i. N..
#             r... A.. _*|?p.. i. no. writable.')
#         ?f.. i.. ?
#
#     ___ setter  fset
#         ?  ?
#         r_ ?
#
#
# # %%
# '''
# So both the `__init__` and the `setter` methods can be used like decorators, and we can now use our `MakeProperty`
# class with decorator syntax:
# '''
#
# # %%
# '''
# We can do it the "long" way first:
# '''
#
# # %%
# c_ Person
#     ___ get_first_name ?
#         r_ ge..  '_first_name' N..
#
#     ___ set_first_name  value
#         ?_fi.. _ ?
#
#     ___ get_last_name ?
#         r_ g..  '_last_name' N..
#
#     ___ set_last_name ? value
#         ?_l.. _ ?
#
#     first_name = MP.. fg.._g.. fs.._s..
#     last_name = MP.. fg.._g... fs.._s..
#
# # %%
# '''
# Or, we can use the "shorthand" decorator syntax:
# '''
#
# # %%
# c_ Person
#     ?MP..
#     ___ first_name ?
#         r_ g.. ? '_first_name' N..
#
#     ??.?
#     ___ first_name value
#         ?_f.. _ ?
#
#     ?MP..
#     ___ last_name ?
#         r_ g.. ? '_last_name' N..
#
#     ??.?
#     ___ last_name ? value
#         ?_l.. _ ?
#
# # %%
# p1 = ?
#
# # %%
# ?.first_name = 'Raymond'
#
# # %%
# p1.last_name = 'Hettinger'
#
# # %%
# p1.first_name
#
# # %%
# p1.last_name
#
# # %%
# '''
# And of course this will work with multiple instances of the `Person` class since we are using the instances themselves
# for the underlying storage:
# '''
#
# # %%
# p2 = Person()
# p2.first_name, p2.last_name = 'Alex', 'Martelli'
#
# # %%
# p1.first_name, p1.last_name, p2.first_name, p2.last_name
#
# # %%
# '''
# Of course our implementation is quite simplistic, but it should help solidy our understanding of properties,
# descriptors, and decorators too!
# '''
#
# # %%
