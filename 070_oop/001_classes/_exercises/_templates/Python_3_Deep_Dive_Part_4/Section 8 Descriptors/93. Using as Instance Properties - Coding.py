# # %%
# '''
# ### Using as Instance Properties
# '''
#
# # %%
# '''
# So let's start exploring how we can use descriptors to read and write instance properties.
# '''
#
# # %%
# '''
# We might try something like this first:
# '''
#
# # %%
# c_ IntegerValue
#     ___ -s ____ instance value
#         i___.stored_value _ in. v..
#
#     ___ -g ____ instance owner_class
#         __ i.. __ N..
#             r_ ____
#         ____
#             r_ g.. i___ 'stored_value' N...
#
#
#
# # %%
# '''
# Basically we are going to use the instance dictionary to store the value under some name (symbol) in it -
# what name should we use? That could be an issue, and we'll come back to that.
# '''
#
# # %%
# c_ Point1D:
#     x = ?
#
# # %%
# p1, p2 = Point1D(), Point1D()
#
# # %%
# p1.x = 10.1
# p2.x = 20.2
#
# # %%
# print(p1.x, p2.x)
#
# # %%
# '''
# As you can see, we now have a descriptor that uses the instances themselves to store the data:
# '''
#
# # %%
# print(p1.__dict__, p2.__dict__)
#
# # %%
# '''
# But you'll notice that our descriptor is hard coded to using the same key in the instance dictionaries - which leads
# us to this problem:
# '''
#
# # %%
# c_ Point2D:
#     x = ?
#     y = ?
#
# # %%
# p = Point2D()
#
# # %%
# p.x = 10.1
#
# # %%
# print(p.__dict__)
#
# # %%
# '''
# And what happens if we set `y`? What symbol is the descriptor going to use to store the value in the instance?
# '''
#
# # %%
# p.y = 20.2
#
# # %%
# print(p.__dict__)
#
# # %%
# '''
# Yep, the **same** symbol!
# '''
#
# # %%
# print(p.x, p.y)
#
# # %%
# '''
# So that appropach is not going to work either. Somehow we would need to have a distinct storage name for each property.
# We could do this by using the `__init__` of our descriptor:
# '''
#
# # %%
# c_ IntegerValue
#     ___ - ____ name
#         ____.storage_name = '_' + ?
#
#     ___ -s ____ instance value
#         s_a_  i___ ____.s.. in. ?
#
#     ___ -g ____ instance owner_class
#         __ i___ __ N..
#             r_ ____
#         ____
#             r_ g.. i.. ____._s_n.. N..
#
# c_ Point2D
#     x = ?('x')
#     y = ?('y')
#
# # %%
# p1 = Point2D()
# p2 = Point2D()
#
# # %%
# p1.x = 10.1
# p1.y = 20.2
#
# # %%
# p1.__dict__
#
# # %%
# p2.x = 100.1
# p2.y = 200.2
#
# # %%
# p2.__dict__
#
# # %%
# '''
# So this approach can work just fine, but there are a few drawbacks:
#
# 1. The user needs to specify the name of the property twice
# 2. We assume that `_` + `name` is not also used by the class in which the descriptor exists (so that could be a major
# problem)
# 3. We assume we can add an attribute to the instance - but what if it uses slots?
# '''
#
# # %%
# '''
# One way we could get around each of those problems is by using the descriptor instance itself to store the instance
# values. But as we saw earlier, we can't just set an attribute in the descriptor instance, since that would be shared
# across multiple instances of the class containing the descriptor.
# Instead, we are going to **assume** that the `instance` is a hashable object, and use a dictionary in the descriptor
# to store instance specific values:
# '''
#
# # %%
# c_ IntegerValue:
#     ___ - ____
#         ____.values =     # dict
#
#     ___ -s ____ instance value
#         ____.? i..| = in. ?
#
#     ___ -g ____ instance owner_class
#         __ i___ __ N..
#             r_ ____
#         ____
#             r_ ____.v__.ge.  i..
#
# # %%
# c_ Point2D:
#     x = ?
#     y = ?
#
# # %%
# p1 = ?
# p2 = ?
#
# # %%
# p1.x = 10.1
# p1.y = 20.2
#
# # %%
# p1.x, p1.y
#
# # %%
# '''
# In fact, we can see the dictionary in the descriptor instances:
# '''
#
# # %%
# Point2D.x.values
#
# # %%
# Point2D.x.values
#
# # %%
# '''
# where the key in both of these is our `p1` object:
# '''
#
# # %%
# hex(id(p1))
#
# # %%
# '''
# We can now create a second point, and go through the same steps:
# '''
#
# # %%
# p2 = Point2D()
# p2.x = 100.1
# p2.y = 200.2
#
# # %%
# hex(id(p2))
#
# # %%
# Point2D.x.values
#
# # %%
# Point2D.y.values
#
# # %%
# '''
# And everything works just fine:
# '''
#
# # %%
# p1.x, p1.y, p2.x, p2.y
#
# # %%
# '''
# Or does it??
# '''
#
# # %%
# '''
# We actually have a potential memory leak - notice how the dictionary in the desccriptor instance is **also** storing
# a reference to the point object - as a **key** in the dictionary.
# '''
#
# # %%
# '''
# Let's write a simple utility function that allows us to get the reference count for an object given it's id
# (and it only makes sense if the id we use still has a valid non-destroyed object):
# '''
#
# # %%
# import ctypes
#
# ___ ref_count(address):
#     r_ ctypes.c_long.from_address(address).value
#
# # %%
# p1 = Point2D()
# id_p1 = id(p1)
#
# # %%
# ref_count(id_p1)
#
# # %%
# '''
# Now let's set the `x` property of `p1`:
# '''
#
# # %%
# p1.x = 100.1
#
# # %%
# '''
# And let's check the ref count again:
# '''
#
# # %%
# ref_count(id_p1)
#
# # %%
# '''
# As you can see it's now `2`. if we delete our main reference to `p1` that is in our global namespace:
# '''
#
# # %%
# 'p1' in globals()
#
# # %%
# del p1
#
# # %%
# 'p1' in globals()
#
# # %%
# ref_count(id_p1)
#
# # %%
# '''
# And our reference count is still `1`, which means the object itself has not been destroyed!
# '''
#
# # %%
# '''
# In fact, we can see that object referenced in our data descriptor dictionary:
# '''
#
# # %%
# Point2D.x.values.items()
#
# # %%
# hex(id_p1)
#
# # %%
# '''
# As you can see, the last element's key is the same id as what `p1` was referencing.
# '''
#
# # %%
# '''
# So, although we deleted `p1`, the object was not destroyed - this can result in a memory leak.
# '''
#
# # %%
# '''
# There are a few ways we can handle this issue. The first one we are going to look at is something called
# **weak references**. So let's segway into that next.
# '''
