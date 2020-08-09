# Problem: https://www.hackerrank.com/challenges/between-two-sets/problem
# Score: 10


_, a, b = input(), list(map(int, input().split())), list(map(int, input().split()))
print(sum([all(i % x __ 0 for x in a) and
           all(x % i __ 0 for x in b) for i in range(max(a), min(b)+1)]))
