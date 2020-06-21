# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# """
# *What is this pattern about?
# The composite pattern describes a group of objects that is treated the
# same way as a single instance of the same type of object. The intent of
# a composite is to "compose" objects into tree structures to represent
# part-whole hierarchies. Implementing the composite pattern lets clients
# treat individual objects and compositions uniformly.
#
# *What does this example do?
# The example implements a graphic c_，which can be either an ellipse
# or a composition of several graphics. Every graphic can be printed.
#
# *Where is the pattern used practically?
# In graphics editors a shape can be basic or complex. An example of a
# simple shape is a line, where a complex shape is a rectangle which is
# made of four line objects. Since shapes have many operations in common
# such as rendering the shape to screen, and since shapes follow a
# part-whole hierarchy, composite pattern can be used to enable the
# program to deal with all shapes uniformly.
#
# *References:
# https://en.wikipedia.org/wiki/Composite_pattern
# https://infinitescript.com/2014/10/the-23-gang-of-three-design-patterns/
#
# *TL;DR80
# Describes a group of objects that is treated as a single instance.
# """
#
#
# c_ Graphic
#     ___ render
#         r_ N..("You should implement this.")
#
#
# c_ CompositeGraphic G..
#     ___ -
#         graphics _    # list
#
#     ___ render
#         ___ graphic _ g..
#             ?.r...
#
#     ___ add graphic
#         g___.ap.. ?
#
#     ___ remove graphic
#         g__.r.. ?
#
#
# c_ EllipseG..
#     ___ - name
#         ?  ?
#
#     ___ render
#         print("Ellipse: @".f.. n..
#
#
# __ _______ __ ______
#     ellipse1 _ E... "1"
#     ellipse2 _ E... "2"
#     ellipse3 _ E... "3"
#     ellipse4 _ E... "4"
#
#     graphic1 _ C..
#     graphic2 _ C..
#
#     _1.a.. _1
#     _1.a.. _2
#     _1.a.. _3
#     _2.a.. _4
#
#     graphic _ C..
#
#     ?.a.. _1
#     ?.a.. _2
#
#     ?.r..
#
# ### OUTPUT ###
# # Ellipse: 1
# # Ellipse: 2
# # Ellipse: 3
# # Ellipse: 4
