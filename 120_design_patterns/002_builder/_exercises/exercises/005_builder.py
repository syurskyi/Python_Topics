# """
# *What is this pattern about?
# It decouples the creation of a complex object and its representation,
# so that the same process can be reused to build objects from the same
# family.
# This is useful when you must separate the specification of an object
# from its actual representation (generally for abstraction).
#
# *What does this example do?
#
# The first example achieves this by using an abstract base
# class for a building, where the initializer (__init__ method) specifies the
# steps needed, and the concrete subclasses implement these steps.
#
# In other programming languages, a more complex arrangement is sometimes
# necessary. In particular, you cannot have polymorphic behaviour in a constructor in C++ -
# see https://stackoverflow.com/questions/1453131/how-can-i-get-polymorphic-behavior-in-a-c-constructor
# - which means this Python technique will not work. The polymorphism
# required has to be provided by an external, already constructed
# instance of a different class.
#
# In general, in Python this won't be necessary, but a second example showing
# this kind of arrangement is also included.
#
# *Where is the pattern used practically?
#
# *References:
# https://sourcemaking.com/design_patterns/builder
#
# *TL;DR
# Decouples the creation of a complex object and its representation.
# """
#
#
# # Abstract Building
# c_ Building:
#     ___ -
#         b_f..
#         b_s..
#
#     ___ build_floor 
#         r.. N..
#
#     ___ build_size
#         r.. N..
#
#     ___ -r
#         r_ 'Floor: {0.f..| | Size: 0.s..|'.f.. ____
#
#
# # Concrete Buildings
# c_ House B..
#     ___ build_floor 
#         floor _ 'One'
#
#     ___ build_size 
#         size _ 'Big'
#
#
# c_ Flat B..
#     ___ build_floor 
#         floor _ 'More than One'
#
#     ___ build_size 
#         size _ 'Small'
#
#
# # In some very complex cases, it might be desirable to pull out the building
# # logic into another function (or a method on another class), rather than being
# # in the base class '__init__'. (This leaves you in the strange situation where
# # a concrete class does not have a useful constructor)
#
#
# c_ ComplexBuilding
#     ___ -r
#         r_ 'Floor: 0.f..| | Size: 0.s..|'.f.. ____
#
#
# c_ ComplexHouse CB..
#     ___ build_floor 
#         floor _ 'One'
#
#     ___ build_size 
#         size _ 'Big and fancy'
#
#
# ___ construct_building cls
#     building _ ?
#     ?.b_f..
#     ?.b_s..
#     r_ b..
#
#
# ___ main():
#     """
#     >>> house _ House()
#     >>> house
#     Floor: One | Size: Big
#
#     >>> flat _ Flat()
#     >>> flat
#     Floor: More than One | Size: Small
#
#     # Using an external constructor function:
#     >>> complex_house _ construct_building(ComplexHouse)
#     >>> complex_house
#     Floor: One | Size: Big and fancy
#     """
#
#
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
