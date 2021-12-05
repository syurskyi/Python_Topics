______ _
______ t___
____ random ______ Random

____ _ ______ Barrier

____ _.context ______ P..

process_count = 8
matrix_size = 200
random = Random()


___ generate_random_matrix(matrix):
    ___ row __ r...(matrix_size):
        ___ col __ r...(matrix_size):
            matrix[row * matrix_size + col] = random.randint(-5, 5)


___ work_out_row(id, matrix_a, matrix_b, result, work_start, work_complete):
    w... T..
        work_start.wait()
        ___ row __ r...(id, matrix_size, process_count):
            ___ col __ r...(matrix_size):
                ___ i __ r...(matrix_size):
                    result[row * matrix_size + col] += matrix_a[row * matrix_size + i] * matrix_b[i * matrix_size + col]
        work_complete.wait()


__ _____ __ _____
    _.set_start_method('spawn')
    work_start = Barrier(process_count + 1)
    work_complete = Barrier(process_count + 1)
    matrix_a = _.Array('i', [0] * (matrix_size * matrix_size), lock=False)
    matrix_b = _.Array('i', [0] * (matrix_size * matrix_size), lock=False)
    result = _.Array('i', [0] * (matrix_size * matrix_size), lock=False)
    ___ p __ r...(process_count):
        P..(t.._work_out_row, a.._(p, matrix_a, matrix_b, result, work_start, work_complete)).s..
    start = t___.t___()
    ___ t __ r...(10):
        generate_random_matrix(matrix_a)
        generate_random_matrix(matrix_b)
        ___ i __ r...(matrix_size * matrix_size):
            result[i] = 0
        work_start.wait()
        work_complete.wait()
    end = t___.t___()
    print("Done, time taken", end - start)
