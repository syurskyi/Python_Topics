# ____ c.. _______ d..
# c_ Matrix o..
#
#     ___ - values
#         ? ?
#
#
#
#     $
#     ___ nrows
#         r.. l.. v..
#
#
#     $
#     ___ ncols
#         r.. l.. v.. 0
#
#     ___ __matmul__ other
#
#
#         rows_1,cols_1 l.. v..,l.. v.. 0
#         rows_2,cols_2 l.. ?.v.. l.. ?.v.. 0
#
#
#         result_rows,result_cols _1,_2
#
#
#         result_matrix N.. ___ _ __ r.. ? ___ _ __ r.. ?
#
#
#
#         ___ row __ r.. ?
#             ___ col __ r.. ?
#                 value 0
#                 ___ c __ r.. _1
#                     ? +_ v.. ? ? * ?.v.. ? ?
#
#                 ? ? ? v..
#
#
#         r.. ? ?
#
#     ___ __imatmul__ other
#
#
#         result self @ ?
#
#         values d.. ?.v..
#
#
#         r.. _
#
#
#     ___ __rmatmul__ other
#
#         r.. _  @ ?
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#     ___  -r
#         r.. f'<Matrix values="{values}">'
#
#
