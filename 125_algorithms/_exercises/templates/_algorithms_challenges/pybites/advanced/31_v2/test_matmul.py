____ matmul _______ Matrix


___ test_matmul
    mat1 Matrix([[1, 2], [3, 4]])
    mat2 Matrix([[11, 12], [13, 14]])
    mat3 mat1 @ mat2
    ... mat3.values __ [[37, 40], [85, 92]]


___ test_rmatmul
    mat1 Matrix([[11, 12], [13, 14]])
    mat2 Matrix([[1, 2], [3, 4]])
    mat3 mat1 @ mat2
    ... mat3.values __ [[47, 70], [55, 82]]


___ test_imatmul
    mat1 Matrix([[11, 12], [13, 14]])
    mat2 Matrix([[1, 2], [3, 4]])
    mat1 @= mat2
    ... mat1.values __ [[47, 70], [55, 82]]

    mat1 Matrix([[11, 12], [13, 14]])
    mat2 Matrix([[1, 2], [3, 4]])
    mat2 @= mat1
    ... mat2.values __ [[37, 40], [85, 92]]


___ test_matmul_bigger
    mat1 Matrix([[11, 12], [13, 14], [15, 16]])
    mat2 Matrix([[1, 2, 3], [4, 5, 6]])
    mat3 mat1 @ mat2
    ... mat3.values __ [[59, 82, 105], [69, 96, 123], [79, 110, 141]]


___ test_imatmul_bigger
    mat1 Matrix([[11, 12], [13, 14], [15, 16]])
    mat2 Matrix([[1, 2, 3], [4, 5, 6]])
    mat1 @= mat2
    ... mat1.values __ [[59, 82, 105], [69, 96, 123], [79, 110, 141]]