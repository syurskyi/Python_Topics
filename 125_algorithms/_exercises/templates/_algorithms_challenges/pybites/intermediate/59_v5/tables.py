# c_ MultiplicationTable
#
#     ___ -  length
#         """Create a 2D self._table of (x, y) coordinates and
#            their calculations (form of caching)"""
#         _len ?
#         _table x * y ___ ? __ r.. 1 l.. + 1 ___ ? __ r.. 1 l.. + 1
#
#     ___ -l
#         """Returns the area of the table (len x* len y)"""
#         r.. l.. _? * l.. _? 0
#
#     ___ -s
#         """Returns a string representation of the table"""
#         r.. '\n'.j.. ' | '.j.. s.. x ___ ? __ y ___ ? __ _?
#
#     ___ calc_cell  x y
#         """Takes x and y coords and returns the (pre-calculated) result"""
#         __ ? > _? o. y > _?
#             r.. I..
#         r.. _? ? - 1 ? - 1
