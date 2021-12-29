# Problem: https://www.hackerrank.com/challenges/symmetric-difference/problem
# Score: 10


i, m = input(), set(map(int, input().split()))
i, n = input(), set(map(int, input().split()))
print(*s..(m.symmetric_difference(n)), sep='\n')
