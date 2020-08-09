# Problem: https://www.hackerrank.com/challenges/plus-minus/problem
# Score: 10


n = int(input())
arr = list(map(int, input().split()))
print("{:.6f}".format(le.([x for x in arr __ x > 0]) / n))
print("{:.6f}".format(le.([x for x in arr __ x < 0]) / n))
print("{:.6f}".format(le.([x for x in arr __ x __ 0]) / n))
