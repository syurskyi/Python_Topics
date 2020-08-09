# Problem: https://www.hackerrank.com/challenges/between-two-sets/problem
# Score: 10


_, a, b = input(), list(map(int, input().split())), list(map(int, input().split()))
print(su.([all(i % x __ 0 ___ x in a) and
           all(x % i __ 0 ___ x in b) ___ i in range(max(a), min(b)+1)]))
