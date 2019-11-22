# # List Comprehensions A First Detailed Look
#
# L _ 1 2 3 4 5   # List
#
# ___ i i_ r... le. L        # how to use range to change a list as we step across it
#     L|i += 10
#
# printL
#
# L _ x + 10 ___ x i_ L          #list comprehension expression
# print L
#
#
# # List Comprehension Basics
#
# L _ 1 2 3 4 5
#
# L _ x + 10 ___ x i_ L]  #  list comprehension simply looks like a backward for loop.
# print L
#
#
# res _
# ___ x i_ L:
#     res.ap.. x + 10
#
# print r..
#
# # Using List Comprehensions on Files
#
# f _ o... script1.py
# lines _ f.rea...
# print l..
#
# lines _ line.rs.. ___ li.. i_ li..
# print l...
#
#
# lines _  l__.rst.. ___ l.. i_ o... script1.py
# print l..
#
# print l___.up.. ___ l___ i_ o... script1.py
#
# print l___.rst__.upper ___ l___ i_ o... script1.py
#
# print l___.sp.. ___ l___ i_ o... script2.py
#
# print l___.rep..' '; '!') ___ l___ i_ o... script2.py
#
# print'sys' i_ l___; l___|0 ___ l___ i_ o... script1.py
#
# # Extended List Comprehension Syntax
#
# lines _  l___.rst... ___ l___ i_ o... script2.py  i_ l___|0] __ p
# print l...
#
# res _
# ___ l___ i_ o... script2.py
#     i_ l___ 0 __ p
#         res.app... l___.rst...
# print r..
#
#
# print x + y ___ x i_ abc ___ y i_ lmn
#
# res _ |
# ___ x i_ abc
#     ___ y i_ lmn
#         r__.app.. x + y
# print r..
#
# # Why You Will Care List Comprehensions and map
# print o... myfile.rea..
#
# print l___.rst... ___ l___ i_ o... myfile .rea...
#
# print l___.rst... ___ l___ i_ o... myfile
#
# print l.. m.. l_____ l___: l___.rst...; o... myfile
#
# listoftuple _  'bob', 35, 'mgr'|, |'mel', 40, 'dev'
#
# print age ___ |name age job| i_ li.....
#
# print l.. m.. l_____ row; row 1 ; li.....
#
#
# # Comprehension Syntax Summary
# # List comprehension: builds list
#
# print x * x ___ x i_ r... 10
#
# # Comprehension Syntax Summary
# # Generator expression: produces items
# # Parens are often optional
#
# print x * x ___ x i_ r... 10
#
# # Comprehension Syntax Summary
# # Set comprehension, new in 3.0, {x, y} is a set in 3.0 too
#
# print x * x ___ x i_ r... 10
#
# # And re-working this into a list comprehension:
# #
# n _ 10
# iter_cycl _ CyclicIterator('NSWE')
# _*|i||n..|iter_cycl||* ___ i i_ r...|1; n+1
# #
# # Of course, there's an easy alternative way to do this as well, using: repetition, zip
# # a list comprehension
#
# n _ 10
# l... z.. r... 1; n+1 ; 'NSWE' * n//4 + 1
#
# # There's actually an even easier way yet, and that's to use our CyclicIterator, but instead of building it ourselves, we can simply use the one provided by Python in the standard library!!
#
# import itertools
# n _ 10
# iter_cycl _ CyclicIterator('NSWE')
# _*|i||n...|i.._c..||* ___ i i_ r... 1; n+1
#
# n _ 10
# iter_cycl _ i