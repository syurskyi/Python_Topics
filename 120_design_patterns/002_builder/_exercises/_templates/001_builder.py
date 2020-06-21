# #!/usr/bin/python
# # -*- coding : utf-8 -*-
#
# """
# *What is this pattern about?
# It decouples the creation of a complex object and its representation,
# so that the same process can be reused to build objects from the same
# family.
# This is useful when you must separate the specification of an object
# from its actual representation (generally for abstraction).
#
# *What does this example do?
# This particular example uses a director function to abstract the
# construction of a building. The user specifies a Builder (House or
# Flat) and the director specifies the methods in the order necessary,
# creating a different building depending on the specification
# (from the Builder c_).
#
# @author: Diogenes Augusto Fernandes Herminio <diofeher@gmail.com>
# https://gist.github.com/420905#file_builder_python.py
#
# *Where is the pattern used practically?
#
# *References:
# https://sourcemaking.com/design_patterns/builder
#
# *TL;DR80
# Decouples the creation of a complex object and its representation.
# """
#
#
# ___ construct_building builder
#     ?.n..
#     ?.b_f..
#     ?.b_s..
#     r_ ?.b..
#
#
# # Abstract Builder
# c_ Builder o..
#
#     ___ -
#         building _ N..
#
#     ___ new_building
#         ____.building _ B..
#
#     ___ build_floor
#         ra.. N...
#
#     ___ build_size
#         ra.. N..
#
# # Concrete Builder
#
#
# c_ BuilderHouse B..
#
#     ___ build_floor
#         building.floor _ 'One'
#
#     ___ build_size
#         building.size _ 'Big'
#
#
# c_ BuilderFlat B..
#     ___ build_floor ____
#         building.floor _ 'More than One'
#
#     ___ build_size
#         building.size _ 'Small'
#
#
# # Product
# c_ Building o..
#
#     ___ -
#         floor _ N..
#         size _ N..
#
#     ___ -r ____
#         r_ 'Floor: 0.f.. | Size: 0.s..'.f.. ____
#
#
# # Client
# __ _____ __ _______
#     building _ c... BH..
#     print ?
#     building _ c.. BF..
#     print ?
#
# ### OUTPUT ###
# # Floor: One | Size: Big
# # Floor: More than One | Size: Small
