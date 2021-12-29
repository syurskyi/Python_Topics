# Problem: https://www.hackerrank.com/challenges/np-arrays/problem
# Score: 10


import numpy


___ arrays(arr):
    return numpy.array(arr[::-1], float)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
