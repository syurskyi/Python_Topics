______ t___
____ random ______ Random

____ _ ______ Barrier, T..

matrix_size = 200
matrix_a = [[0] * matrix_size ___ a __ r...(matrix_size)]
matrix_b = [[0] * matrix_size ___ b __ r...(matrix_size)]
result = [[0] * matrix_size ___ r __ r...(matrix_size)]
random = Random()
work_start = Barrier(matrix_size + 1)
work_complete = Barrier(matrix_size + 1)

___ generate_random_matrix(matrix):
    ___ row __ r...(matrix_size):
        ___ col __ r...(matrix_size):
            matrix[row][col] = random.randint(-5, 5)

___ work_out_row(row):
    w... T..
        work_start.w..
        ___ col __ r...(matrix_size):
            ___ i __ r...(matrix_size):
                result[row][col] += matrix_a[row][i] * matrix_b[i][col]
        work_complete.w..


___ row __ r...(matrix_size):
    T..(t.._work_out_row, a.._([row])).s..
start = t___.t___()
___ t __ r...(10):
    generate_random_matrix(matrix_a)
    generate_random_matrix(matrix_b)
    result = [[0] * matrix_size ___ r __ r...(matrix_size)]
    work_start.w..
    work_complete.w..
end = t___.t___()
print("Done, time taken", end - start)
