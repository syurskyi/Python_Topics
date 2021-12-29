# Problem: https://www.hackerrank.com/challenges/kangaroo/problem
# Score: 10


___ kangaroo(x1, v1, x2, v2):
    r.. 'YES' __ (v1 > v2) and (x2 - x1) % (v2 - v1) __ 0 ____ 'NO'


x1, v1, x2, v2 = map(int, input().split())
print(kangaroo(x1, v1, x2, v2))
