______ time
from random ______ Random

from threading ______ Barrier, Thread

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
    while True:
        work_start.wait()
        ___ col __ r...(matrix_size):
            ___ i __ r...(matrix_size):
                result[row][col] += matrix_a[row][i] * matrix_b[i][col]
        work_complete.wait()


___ row __ r...(matrix_size):
    Thread(t.._work_out_row, a.._([row])).start()
start = time.time()
___ t __ r...(10):
    generate_random_matrix(matrix_a)
    generate_random_matrix(matrix_b)
    result = [[0] * matrix_size ___ r __ r...(matrix_size)]
    work_start.wait()
    work_complete.wait()
end = time.time()
print("Done, time taken", end - start)
