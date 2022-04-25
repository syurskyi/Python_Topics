# ____ ? _______ ?
#
#
# c_ MatrixWithoutMatMul o..
#
#     ___ -  values
#         ? ?
#         col l.. ? 0
#         row l.. v..
#
#     ___ __matmul__  other
#         r.. N..
#
#
# ___ test_matmul
#     mat1 ? 1, 2], [3, 4
#     mat2 ? 11, 12], [13, 14
#     mat3 ? @ ?
#     ... ?.v.. __ 37, 40], [85, 92
#     mat3 ? @ ?
#     ... ?.v.. __ 47, 70], [55, 82
#
#
# ___ test_rmatmul
#     mat1 ? 1, 2], [3, 4
#     mat2 ? 11, 12], [13, 14
#     # mat2 does not implement matmul, so mat1's rmatmul is called
#     # which results in mat1 @ mat2
#     ret ? @ ?
#     ... ?.v.. __ 37, 40], [85, 92
#
#
# ___ test_imatmul
#     mat1 ? 11, 12], [13, 14
#     org_id_of_mat1 i. ?
#     mat2 ? 1, 2], [3, 4
#     mat1 @= ?
#     id_of_mat1_after_inplace_operation i. ?
#     ... ?.v.. __ 47, 70], [55, 82
#     # as @= is in place, the id of the object should not change!
#     ... org_id_of_mat1 __ ?
#
#
# ___ test_imatmul_other_way_around
#     mat1 ?([[11, 12], [13, 14]])
#     mat2 Matrix([[1, 2], [3, 4]])
#     org_id_of_mat2 id(mat2)
#     mat2 @= mat1
#     id_of_mat2_after_inplace_operation id(mat2)
#     ... mat2.values __ [[37, 40], [85, 92]]
#     ... org_id_of_mat2 __ id_of_mat2_after_inplace_operation
