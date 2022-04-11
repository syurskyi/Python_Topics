# _______ p__
#
# ____ ? _______ ?
#
# friends 'Bob Dante Julian Martin'.s..
#
#
# ?p__.m__.p.('test_input,expected', [
#     (('Bob', 'Dante'), T..),
#     (('Bob', 'Julian'), T..),
#     (('Bob', 'Martin'), T..),
#     (('Dante', 'Julian'), T..),
#     (('Dante', 'Martin'), T..),
#     (('Julian', 'Martin'), T..),
#     # order does not matter
#     (('Dante', 'Bob'), F..),
#     (('Julian', 'Bob'), F..),
#     (('Martin', 'Bob'), F..),
#     (('Julian', 'Dante'), F..),
#     (('Martin', 'Dante'), F..),
#     (('Martin', 'Julian'), F..),
#     # not with self
#     (('Julian', 'Julian'), F..),
#
# ___ test_team_of_two_order_does_not_matter test_input e..
#     """First test lists all combos"""
#     combos l.. f.. f, t.._2, o.._F..
#     ... l.. ? __ 6
#     __ e..
#         ... t.. __ ?
#     ____
#         ... t.. n.. __ ?
#
#
# ?p__.m__.p. 'test_input,expected', [
#     (('Bob', 'Dante'), T..),
#     (('Dante', 'Julian'), T..),
#     (('Dante', 'Martin'), T..),
#     # order does matter
#     (('Dante', 'Bob'), T..),
#     (('Julian', 'Dante'), T..),
#     (('Martin', 'Dante'), T..),
#
# ___ test_team_of_two_order_does_matter(test_input, e..
#     """From here on just test a subset of combos"""
#     combos l.. f.. f, t.._2, o.._T..
#     ... l.. ? __ 12
#     ... t.. __ ?
#
#
# ?p__.m__.p. 'test_input,expected', [
#     (('Bob', 'Dante', 'Julian'), T..),
#     (('Bob', 'Dante', 'Martin'), T..),
#     (('Bob', 'Julian', 'Martin'), T..),
#     (('Dante', 'Julian', 'Martin'), T..),
#     # order does not matter
#     (('Dante', 'Bob', 'Martin'), F..),
#     (('Julian', 'Martin', 'Dante'), F..),
#     # no one goes twice
#     (('Dante', 'Dante', 'Martin'), F..),
#
# ___ test_team_of_three_order_does_not_matter(test_input, e..
#     combos l.. f.. f.. t.._3 o.._F..
#     ... l.. ? __ 4
#     __ e..
#         ... t.. __ ?
#     ____
#         ... t.. n.. __ ?
#
#
# ?p__.m__.p.'test_input,expected', [
#     (('Bob', 'Dante', 'Julian'), T..),
#     (('Bob', 'Dante', 'Martin'), T..),
#     (('Bob', 'Julian', 'Martin'), T..),
#     (('Dante', 'Julian', 'Martin'), T..),
#     # order does matter
#     (('Dante', 'Bob', 'Martin'), T..),
#     (('Julian', 'Martin', 'Dante'), T..),
#
# ___ test_team_of_three_order_does_matter(test_input, e..
#     combos l.. f.. f.. t.._3 o.._T..
#     ... l.. ? __ 24
#     ... t.. __ ?
