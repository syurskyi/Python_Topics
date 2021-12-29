# Problem: https://www.hackerrank.com/challenges/diagonal-difference/problem
# Score: 10


a    # list
result = 0
___ i __ r..(int(input())):
    a = l..(map(int, input().split()))
    result += a[i] - a[- 1 - i]
print(abs(result))
