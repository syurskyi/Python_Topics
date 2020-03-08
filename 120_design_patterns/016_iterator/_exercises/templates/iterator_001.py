# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# """
# http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/
# Implementation of the iterator pattern with a generator
#
# *TL;DR80
# Traverses a container and accesses the container's elements.
# """
#
# ____ -f ______ p..
#
#
# ___ count_to count
#     """Counts by word numbers, up to a maximum of five"""
#     numbers _ "one", "two", "three", "four", "five"
#     ___ ? __ ?|;c..
#         y.. ?
#
# # Test the generator
# count_to_two _ l____ c... 2
# count_to_five _ l____ c.. 5
#
# print('Counting to two...')
# ___ number __ c_t_t..
#     print ? e.._' ')
#
# print()
#
# print('Counting to five...')
# ___ number __ c_t_f..
#     print ? e.._' ')
#
# print()
#
# ### OUTPUT ###
# # Counting to two...
# # one two
# # Counting to five...
# # one two three four five
