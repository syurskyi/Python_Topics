# Problem: https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
#  Score: 20


___ array_left_rotation(a, k
    result = a[k:] + a[:k]
    r_ result


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
print(*array_left_rotation(a, k))
