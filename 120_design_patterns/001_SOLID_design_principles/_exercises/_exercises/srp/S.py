#
# """
# Single-responsibility Principle
#
#
#
# bad -  problem : have two jobs    -    easy to use
# """
#
#
# c_ Animal
#     ___  -  name ?
#         ?  ?
#
#     ___ get_name(self) __ ?
#         p..
#
#     ___ save animal A..
#         p..
#
#
#
#
# """
# better  - two class, each have one job   - a little messy to use
# """
#
#
# c_ Animal
#     ___  -  name ?
#         ?  ?
#
#     ___ get_name
#         p..
#
#
# c_ AnimalDB
#     ___ get_animal id __ A..
#         p..
#
#     ___ save animal A..
#         p..
#
#
#
#
# """
# Best   -   using facade   -   each class have one job - easier to use
# """
#
#
# c_ Animal
#     ___  - ( name: ?
#         ?  ?
#         ?db _ ADB
#
#     ___ get_name
#         r_ ?n..
#
#     ___ get id
#         r_ ?d_.g_a.. ?
#
#     ___ save
#         ?d_.s.. animal=____
