# c_ MultiplicationTable
#
#     ___ -  length
#         """Create a 2D self._table of (x, y) coordinates and
#            their calculations (form of caching)"""
#         _length ?
#         _table  s.. x * y ___ ? __ r.. 1 l.. + 1 ___ ? __ r.. 1 l.. + 1
#
#     ___ -l
#         """Returns the area of the table (len x* len y)"""
#
#         r.. ?**2
#
#     ___ -s
#         """Returns a string representation of the table"""
#
#         s ''
#
#         ___ row __ _?
#             ? +_ (' | '.j.. ? + '\n'
#
#
#         r.. ?
#
#
#
#
#
#
#     ___ calc_cell  x, y
#         """Takes x and y coords and returns the re-calculated result"""
#
#
#         __ n.. 1 <_ ? <_ _? a.. 1 <_ y <_ _?
#             r.. I.. "Invalid x and y"
#
#
#         r.. i.. _? ? -1 ? -1
