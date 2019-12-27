# # %%
# '''
# ### Initializing Class Instances
# '''
#
# # %%
# '''
# When we create a new instance of a class two separate things are happening:
# 1. The object instance is **created**
# 2. The object instance is then further **initialized**
# '''
#
# # %%
# '''
# We can "intercept" both the creating and initialization phases, by using special methods `__new__` and `__init__`.
# We'll come back to `__new__` later. For now we'll focus on `__init__`.
# '''
#
# # %%
# '''
# What's important to remember, is that `__init__` is an **instance method**. By the time `__init__` is called,
# the new object has **already** been created, and our `__init__` function defined in the class is now treated like a
# **method** bound to the instance.
# '''
#
# # %%
# c_ Person:
#     def __init__(____):
#         print(f'Initializing a new Person object: {____}')
#
# # %%
# p = Person()
#
# # %%
# '''
# And we can see that `p` has the same memory address:
# '''
#
# # %%
# print(hex(id(p)))
#
# # %%
# '''
# Because `__init__` is an instance method, we have access to the object (instance) state within the method, so we can
# use it to manipulate the object state:
# '''
#
# # %%
# c_ Person:
#     ___ -i ____ name
#         ____.n.. _ n..
#
# # %%
# p _ ? Eric
#
# # %%
# print ?.-d
#
# # %%
# '''
# What actually happens is that after the new instance has been created, Python sees and automatically
# calls `<instance>.__init__(self, *args, **kwargs)`
# '''
#
# # %%
# '''
# So this is no different that if we had done it this way:
# '''
#
# # %%
# c_ Person
#     ___ initialize ____ name
#         ____.n.. _ n..
#
# # %%
# p _ ?
#
# # %%
# print ?.-d
#
# # %%
# ?.i.. Eric
#
# # %%
# print ?.-d
#
# # %%
# '''
# But by using the `__init__` method both these things are done automatically for us.
# Just remember that by the time `__init__` is called, the instance has **already** been created, and `__init__` is
# an instance method.
# '''