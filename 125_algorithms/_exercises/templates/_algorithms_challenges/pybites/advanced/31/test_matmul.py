____ matmul _______ Matrix


c_ MatrixWithoutMatMul(o..

    ___ - , values
        values values
        col l..(values[0])
        row l..(values)

    ___ __matmul__  other
        r.. NotImplemented


___ test_matmul
    mat1 Matrix([[1, 2], [3, 4]])
    mat2 Matrix([[11, 12], [13, 14]])
    mat3 mat1 @ mat2
    ... mat3.values __ [[37, 40], [85, 92]]
    mat3 mat2 @ mat1
    ... mat3.values __ [[47, 70], [55, 82]]


___ test_rmatmul
    mat1 Matrix([[1, 2], [3, 4]])
    mat2 MatrixWithoutMatMul([[11, 12], [13, 14]])
    # mat2 does not implement matmul, so mat1's rmatmul is called
    # which results in mat1 @ mat2
    ret mat2 @ mat1
    ... ret.values __ [[37, 40], [85, 92]]


___ test_imatmul
    mat1 Matrix([[11, 12], [13, 14]])
    org_id_of_mat1 id(mat1)
    mat2 Matrix([[1, 2], [3, 4]])
    mat1 @= mat2
    id_of_mat1_after_inplace_operation id(mat1)
    ... mat1.values __ [[47, 70], [55, 82]]
    # as @= is in place, the id of the object should not change!
    ... org_id_of_mat1 __ id_of_mat1_after_inplace_operation


___ test_imatmul_other_way_around
    mat1 Matrix([[11, 12], [13, 14]])
    mat2 Matrix([[1, 2], [3, 4]])
    org_id_of_mat2 id(mat2)
    mat2 @= mat1
    id_of_mat2_after_inplace_operation id(mat2)
    ... mat2.values __ [[37, 40], [85, 92]]
    ... org_id_of_mat2 __ id_of_mat2_after_inplace_operation
