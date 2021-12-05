import time
from random import Random

from threading import Barrier, Thread

matrix_size = 200
matrix_a = [[0] * matrix_size for a in range(matrix_size)]
matrix_b = [[0] * matrix_size for b in range(matrix_size)]
result = [[0] * matrix_size for r in range(matrix_size)]
random = Random()
work_start = Barrier(matrix_size + 1)
work_complete = Barrier(matrix_size + 1)

def generate_random_matrix(matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            matrix[row][col] = random.randint(-5, 5)

def work_out_row(row):
    while True:
        work_start.wait()
        for col in range(matrix_size):
            for i in range(matrix_size):
                result[row][col] += matrix_a[row][i] * matrix_b[i][col]
        work_complete.wait()


for row in range(matrix_size):
    Thread(target=work_out_row, args=([row])).start()
start = time.time()
for t in range(10):
    generate_random_matrix(matrix_a)
    generate_random_matrix(matrix_b)
    result = [[0] * matrix_size for r in range(matrix_size)]
    work_start.wait()
    work_complete.wait()
end = time.time()
print("Done, time taken", end - start)
