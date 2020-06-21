# # %%
# '''
# ### Descriptors
# '''
#
# # %%
# '''
# Python **descriptors** are simply objects that implement the **descriptor protocol**.
# The protocol is comprised of the following special methods - not all are required.
# - `__get__`: used to retrieve the property value
# - `__set__`: used to store the property value (we'll see where we can do this in a bit)
# - `__del__`: delete a property ____ the instance
# - `__set_name__`: new to Python 3.6, we can use this to capture the property name as it is being defined in the owner
# class (the class where the property is defined).
#
# There are two types of descriptors we need to distingush as I explain in the video lecture:
# - non-data descriptors: these are descriptors that only implement `__get__` (and optionally `__set_name__`)
# - data descriptors: these implement the `__set__` method, and normally, also the `__get__` method.
# '''
#
# # %%
# '''
# Let's create a simple non-data descriptor:
# '''
#
# # %%
# ____ d_t_ _____ d_t_
#
# c_ TimeUTC
#     ___ -g ____ instance owner_class
#         r_ d_t_.u_n_.i_f_
#
# # %%
# '''
# So `TimeUTC` is a class that implements the `__get__` method only, and is therefore considered a non-data descriptor.
# '''
#
# # %%
# '''
# We can now use it to create properties in other classes:
# '''
#
# # %%
# c_ Logger
#     current_time _ ?
#
# # %%
# '''
# Note that `current_time` is a class attribute:
# '''
#
# # %%
# ?. -d
#
# # %%
# '''
# We can access that attribute ____ an instance of the `Logger` class:
# '''
#
# # %%
# l = L..
#
# # %%
# print(?.c..
#
# # %%
# '''
# We can also access it ____ the class itself, and for now it behaves the same (we'll come back to that later):
# '''
#
# # %%
# L__.c..
#
# # %%
# '''
# Let's consider another example.
# '''
#
# # %%
# '''
# Suppose we want to create class that allows us to select a random suit and random card ____ that suit ____ a deck
# of cards (with replacement, i.e. the same card can be picked more than once).
# '''
#
# # %%
# '''
# We could approach it this way:
# '''
#
# # %%
# ____ ra.. _____ ch.. se..
#
# c_ Deck
#     ?p..
#     ___ suit ____
#         r_ ch.. 'Spade', 'Heart', 'Diamond', 'Club'
#
#     ?p..
#     ___ card ____
#         r_ ch.. tu.. '23456789JQKA'| + '10';|
#
# # %%
# d = ?
#
# # %%
# seed(0)
#
# ___ _ __ ra.. 10     # _ the original
#     print(?.c.. ?.s..
#
# # %%
# '''
# This was pretty easy, but as you can see both properties essentially did the same thing - they picked a random choice
# ____ some iterable.
# Let's rewrite this using a custom descriptor:
# '''
#
# # %%
# c_ Choice
#     ___ - ____ $choices
#         ____.?  ?
#
#     ___ -g ____ instance, owner_class
#         r_ c..|____.c..
#
# # %%
# '''
# And now we can rewrite our `Deck` c_ this way:
# '''
#
# # %%
# c_ Deck
#     suit = C.. 'Spade', 'Heart', 'Diamond', 'Club'
#     card = C.. @'23456789JQKA', '10'
#
# # %%
# seed(0)
#
# d = D..
#
# ___ _ __ ra.. 10
#     print ?.c.. ?.s..
#
# # %%
# '''
# Of course we are not limited to just cards, we could use it in other classes too:
# '''
#
# # %%
# c_ Dice
#     die_1 = Choice(1,2,3,4,5,6)
#     die_2 = Choice(1,2,3,4,5,6)
#     die_3 = Choice(1,2,3,4,5,6)
#
# # %%
# seed(0)
#
# dice = Dice()
# for _ in range(10):
#     print(dice.die_1, dice.die_2, dice.die_3)
#
# # %%
