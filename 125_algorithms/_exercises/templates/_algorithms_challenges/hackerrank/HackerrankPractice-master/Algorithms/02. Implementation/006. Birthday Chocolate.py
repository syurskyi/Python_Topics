# Problem: https://www.hackerrank.com/challenges/the-birthday-bar/problem
# Score: 10


n, s = int(input().strip()), list(map(int, input().split()))
d, m = map(int, input().split())
print(su.([su.(s[i: i + m]) __ d ___ i in range(le.(s) - m + 1)]))
