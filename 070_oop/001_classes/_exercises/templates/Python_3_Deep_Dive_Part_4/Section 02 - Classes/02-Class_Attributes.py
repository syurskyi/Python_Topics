# # %%
# '''
# ### Class Attributes
# '''
#
# # %%
# '''
# As we saw, when we create a class Python automatically builds-in properties and behaviors into our class object,
# like making it callable, and properties like `__name__`.
# '''
#
# # %%
# c_ Person
#     p..
#
# # %%
# print ?.__n)
#
# # %%
# '''
# `__name__` is a **class attribute**. We can add our own class attributes easily this way:
# '''
#
# # %%
# c_ Program
#     language _ 'Python'
#     version _ '3.6'
#
# # %%
# print P_.__n
#
# # %%
# print P_.l..
#
# # %%
# print(P_.v..
#
# # %%
# '''
# Here we used "dotted notation" to access the class attributes. In fact we can also use dotted notation to set
#  the class attribute:
# '''
#
# # %%
# P_.v.. _ '3.7'
#
# # %%
# print P_.v..
#
# # %%
# '''
# But we can also use the functions `getattr` and `setattr` to read and write these attributes:
# '''
#
# # %%
# print g___ P_ 'version'
#
# # %%
# s.. P_ 'version', '3.6'
#
# # %%
# print P_.v.. g___ P_ 'version'
#
# # %%
# '''
# Python is a dynamic language, and we can create attributes at run-time, outside of the class definition itself:
# '''
#
# # %%
# P_.x _ 100
#
# # %%
# '''
# Using dotted notation we added an attribute `x` to the Person class:
# '''
#
# # %%
# print P_.x g___ P_ 'x'
#
# # %%
# '''
# We could also just have used a `setattr` function call:
# '''
#
# # %%
# s.. P_ 'y' 200
#
# # %%
# print P_.y g___ P_ 'y'
#
# # %%
# '''
# So where is the state stored? Usually in a dictionary that is attached to the **class** object
# (often referred to as the **namespace** of the class):
# '''
#
# # %%
# print P_.-d
#
# # %%
# '''
# As you can see that dictionary contains our attributes: `language`, `version`, `x`, `y` with their corresponding
# current values.
# '''
#
# # %%
# '''
# Notice also that `Program.__dict__` does not return a dictionary, but a `mappingproxy` object - this is essentially
# a read-only dictionary that we cannot modify directly (but we can modify it by using `setattr`, or dotted notation).
# '''
#
# # %%
# '''
# For example, if we change the value of an attribute:
# '''
#
# # %%
# s.. P_ 'x' -10
#
# # %%
# '''
# We'll see this reflected in the underlying dictionary:
# '''
#
# # %%
# print P_ -d
#
# # %%
# '''
# #### Deleting Attributes
# '''
#
# # %%
# '''
# So, we can create and mutate class attributes at run-time. Can we delete attributes too?
# The answer of course is yes. We can either use the `del` keyword, or the `delattr` function:
# '''
#
# # %%
# del P_.x
#
# # %%
# print P_.-d
#
# # %%
# d... P_, 'y'
#
# # %%
# '''
# #### Direct Namespace Access
# '''
#
# # %%
# print P_.-d
#
# # %%
# '''
# Although `__dict__` returns a `mappingproxy` object, it still is a hash map and essentially behaves like a read-only
#  dictionary:
# '''
#
# # %%
# print P_.-d'language'
#
# # %%
# print li.. P_.-d.it..
#
# # %%
# '''
# One word of caution: not every attribute that a class has lives in that dictionary (we'll come back to this later).
# For example, you'll notice that the `__name__` attribute is not there:
# '''
#
# # %%
# print P_.__n
#
# # %%
# print __n i_ P_.-d