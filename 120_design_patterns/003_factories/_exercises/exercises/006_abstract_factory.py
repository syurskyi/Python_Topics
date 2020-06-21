# """Implementation of the abstract factory pattern"""
# ______ ra...
#
#
# c_ PetShop
#     """A pet shop"""
#
#     ___ - animal_factory_N..
#         """pet_factory is our abstract factory. We can set it at will."""
#         ?pet_factory _ ?
#
#     ___ show_pet
#         """Creates and shows a pet using the abstract factory"""
#         pet = ?p_f_.g_p..
#         print("This is a lovely", ?
#         print("It says", ?.s..
#         print("It eats", ?p_f__.g_f..
#
# # Stuff that our factory makes
#
#
# c_ Dog
#     ___ speak
#         r_ "woof"
#
#     ___ __str__
#         r_ "Dog"
#
#
# c_ Cat
#     ___ speak
#         r_ "meow"
#
#     ___ __str__
#         r_ "Cat"
#
#
# # Factory classes
# c_ DogFactory
#     ___ get_pet
#         r_ ?
#
#     ___ get_food
#         r_ "dog food"
#
#
# c_ CatFactory
#     ___ get_pet
#         r_ ?
#
#     ___ get_food
#         r_ "cat food"
#
#
# # Create the proper family
# ___ get_factory
#     """Let's be dynamic!"""
#     r_ ra__.ch.. D.. C..
#
# # Show pets with various factories
# shop = P..
# ___ i __ ra__ 3
#     ?.p_f.. _ g_f..
#     ?.s_p..
#     print("=" * 10)
