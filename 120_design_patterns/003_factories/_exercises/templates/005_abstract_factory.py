# """
# *What is this pattern about?
#
# In Java and other languages, the Abstract Factory Pattern serves to provide an interface for
# creating related/dependent objects without need to specify their
# actual c_.
#
# The idea is to abstract the creation of objects depending on business
# logic, platform choice, etc.
#
# In Python, the interface we use is simply a callable, which is "builtin" interface
# in Python, and in normal circumstances we can simply use the c_ itself as
# that callable, because classes are first c_ objects in Python.
#
# *What does this example do?
# This particular implementation abstracts the creation of a pet and
# does so depending on the factory we chose (Dog or Cat, or random_animal)
# This works because both Dog/Cat and random_animal respect a common
# interface (callable for creation and .speak()).
# Now my application can create pets abstractly and decide later,
# based on my own criteria, dogs over cats.
#
# *Where is the pattern used practically?
#
# *References:
# https://sourcemaking.com/design_patterns/abstract_factory
# http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/
#
# *TL;DR
# Provides a way to encapsulate a group of individual factories.
# """
#
# _______ ra..
#
#
# c_ PetShop
#
#     """A pet shop"""
#
#     ___ - animal_factory_N..
#         """pet_factory is our abstract factory.  We can set it at will."""
#
#         ?pet_factory _ ?
#
#     ___ show_pet
#         """Creates and shows a pet using the abstract factory"""
#
#         pet = ?p..
#         print("We have a lovely @".f.. ?
#         print("It says @".f.. ?s..)
#
#
# c_ Dog
#     ___ speak
#         r_ "woof"
#
#     ___ -s
#         r_ "Dog"
#
#
# c_ Cat
#     ___ speak
#         r_ "meow"
#
#     ___ -s
#         r_ "Cat"
#
#
# # Additional factories:
#
# # Create a random animal
# ___ random_animal
#     """Let's be dynamic!"""
#     r_ ra__.ch.. D.. C..
#
#
# # Show pets with various factories
# __ _______ __ _____
#
#     # A Shop that sells only cats
#     cat_shop = P.. C..
#     ?.s_p..
#     print("")
#
#     # A shop that sells random animals
#     shop = P.. r_a..
#     ___ i __ ra.. 3
#         s__.s_p..
#         print("=" * 20)
#
# ### OUTPUT ###
# # We have a lovely Cat
# # It says meow
# #
# # We have a lovely Dog
# # It says woof
# # ====================
# # We have a lovely Cat
# # It says meow
# # ====================
# # We have a lovely Cat
# # It says meow
# # ====================
