#
# c_ MultiplicationTable
#
#     ___ -  length
#         """Create a 2D self._table of (x, y) coordinates and
#            their calculations (form of caching)"""
#         _length ?
#         _table    # list
#         ___ i __ r.. 1 ? +1
#             row    # list
#             ?.a.. ?
#
#             j 1
#             current i
#             w.... ? < _?
#                 ? +_ ?
#                 ?.a.. c..
#                 ? +_ 1
#             _?.a.. ?
#
#     ___ -l
#         """Returns the area of the table (len x* len y)"""
#         _area ? * ?
#         r.. ?
#
#     ___ -s
#         """Returns a string representation of the table"""
#         _table_output ""
#         ___ row __ _table
#             table_row ""
#             ___ ele __ r.. |l.. r.. -1
#                 t.. +_ _*? | "
#             t.. +_ _? r.. -1
#             _? +_ _* ?\n
#         r.. ?
#
#     ___ calc_cell  x y
#         """Takes x and y coords and returns the re-calculated result"""
#         _x ?
#         _y ?
#
#         __ ? > _l.. o. ? > _l..
#             r.. I..
#         ____
#             _result ? * ?
#             r.. ?
#
#
# # if __name__ == "__main__":
# #     table = MultiplicationTable(4)
# #     print(table._table)
# #     print(table.__len__())
# #     print(table.__str__())
# #     print(table.calc_cell(4, 3))