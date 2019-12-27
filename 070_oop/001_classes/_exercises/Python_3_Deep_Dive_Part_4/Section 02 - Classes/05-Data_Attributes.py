# # %%
# '''
# ### Data Attributes
# '''
#
# # %%
# '''
# Let's focus on data attributes first (non-callables).
# As we saw before we can have class attributes - they live in the class dictionary:
# '''
#
# # %%
# c_ BankAccount
#     apr _ 1.2
#
# # %%
# print ?.-d
#
# # %%
# print ?.a..
#
# # %%
# '''
# Now when we create instances of that class:
# '''
#
# # %%
# acc_1 _ ?
# ._2 _ ?
#
# # %%
# '''
# The instance dictionaries are currently empty:
# '''
#
# # %%
# print ._1.-d ._2.-d
#
# # %%
# '''
# Yet, these instances do have an `apr` attribute:
# '''
#
# # %%
# print ._1.a__ a_2.a__
#
# # %%
# '''
# Where is that value coming from? The class the objects were created from!
# '''
#
# # %%
# '''
# In fact, if we modify the class attribute:
# '''
#
# # %%
# ?.a.. _ 2.5
#
# # %%
# '''
# We'll see this reflected in the instances as well:
# '''
#
# # %%
# print._1.a__ ._2.a__
#
# # %%
# '''
# And if we a a class attribute to `BankAccount`:
# '''
#
# # %%
# ?.account_type _ 'Savings'
#
# # %%
# print ._1.a.. ._2.a..
#
# # %%
# '''
# As you can see modifying attributes in the **class** are reflected in the instances too - that's because Python
# does not find an `apr` attribute in the instance dic tionary, so next it looks in the class that was used to create
# the instance.
# Which raises the question, what happens if we add `apr` to the **instance** dictionary?
# '''
#
# # %%
# ._1.a__ _ 0
#
# # %%
# '''
# Well that did not raise an exception - so what's happening now:
# '''
#
# # %%
# print ._1.-d ._2.-d
#
# # %%
# '''
# As you can see, we actually create an entry for `apr` in the state dictionary of `acc_1`.
# Now that we have it there, it we try to get the attribute value `apr` for `acc_1`, Python will find it in the instance
# dictionary, so it will use that instead!
# '''
#
# # %%
# print ._1.a__ ._2.a__
#
# # %%
# '''
# In effect, the instance attribute `apr` is **hiding** the class attribute.
# You'll notice also that `acc_2` was **not** affected - this is because we did not modify `acc_2`'s dictionary,
# just the dictionary for `acc_1`.
# And the `getattr` and `setattr` functions work the same way as dotted notation:
# '''
#
# # %%
# ._1 _ ?
# print ._1.-d
# print ._1.a__
# print g.... ._1 'a__'
#
# # %%
# setattr ._1 'a__' 0
# print ._1.-d
# print ._1.a__
# print g.... ._1 'a__'
#
# # %%
# '''
# We can even add instance attributes directly to an instance:
# '''
#
# # %%
# ._1.bank _ 'Acme Savings & Loans'
#
# # %%
# print ._1.-d
#
# # %%
# '''
# But this is specific to the instance, and only that specific instance:
# '''
#
# # %%
# ._2 _ ?
#
# # %%
# print ._2.-d
#
# # %%
# '''
# As you can see `acc_2` has an empty instance dictionary.
# '''
#
# # %%
# '''
# So it is really important to distingush between **class attributes** and **instance attributes**.
# **Class attributes** are like attributes that are "common" to all instances - because the attribute does not live
# in the instance, but in the class itself.
# On the other hand, **instance attributes** are specific to each instance, and values for the same attribute can be
# different across multiple instances, as we just saw with `acc_1.apr` and `acc_2.apr`.
# '''
#
# # %%
# '''
# So, in summary, classes and instances each have their own state - usually maintained in a dictionary, available through
# `__dict__`. Irrespective of where the state is stored, when we look up an attribute on an instance, Python will first
# look for the attribute in the instance's local state. If it does not find it there, it will next look for it
# in the class of the instance.
# '''
#
# # %%
# '''
# One other thing to note is the difference in type between class and instance `__dict__`.
# Classes as we saw, return a `mapping proxy` object:
# '''
#
# # %%
# print ?.-d
#
# # %%
# '''
# But instances, return a real dictionary:
# '''
#
# # %%
# print ._1.-d
#
# # %%
# '''
# So with instances, unlike with classes, we can manipulate that dictionary directly:
# '''
#
# # %%
# c_ Program
#     language _ 'Python'
#
# # %%
# p _ ?
#
# # %%
# print ?.-d
#
# # %%
# ?.-d 'version' _ '3.7'
#
# # %%
# print ?.-d
#
# # %%
# print ?.v.. g.... ? 'v...
#
# # %%
# '''
# But once again, this only affects that specific **instance**.
# '''
#
# # %%
