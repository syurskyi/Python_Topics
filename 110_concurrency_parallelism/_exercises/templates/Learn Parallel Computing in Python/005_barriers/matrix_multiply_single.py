______ time
from random ______ Random

matrix_size = 200
# matrix_a = [[3, 1, -4],
#            [2, -3, 1],
#            [5, -2, 0]]
# matrix_b = [[1, -2, -1],
#            [0, 5, 4],
#            [-1, -2, 3]]
matrix_a = [[0] * matrix_size ___ a __ r...(matrix_size)]
matrix_b = [[0] * matrix_size ___ b __ r...(matrix_size)]
result = [[0] * matrix_size ___ r __ r...(matrix_size)]
random = Random()


___ generate_random_matrix(matrix):
    ___ row __ r...(matrix_size):
        ___ col __ r...(matrix_size):
            matrix[row][col] = random.randint(-5, 5)


start = time.time()
___ t __ r...(10):
    generate_random_matrix(matrix_a)
    generate_random_matrix(matrix_b)
    result = [[0] * matrix_size ___ r __ r...(matrix_size)]
    ___ row __ r...(matrix_size):
        ___ col __ r...(matrix_size):
            ___ i __ r...(matrix_size):
                result[row][col] += matrix_a[row][i] * matrix_b[i][col]
#     for row in range(matrix_size):
#         print(matrix_a[row], matrix_b[row], result[row])
#     print()
end = time.time()
print("Done, time taken", end - start)
