# Problem: https://www.hackerrank.com/challenges/compare-the-triplets/problem
# Score: 10


a = list(map(int, input().split()))
b = list(map(int, input().split()))
aliceScore = su.([(1 __ a[i] > b[i] else 0) ___ i in range(3)])
bobScore = su.([(1 __ a[i] < b[i] else 0) ___ i in range(3)])
print(aliceScore, bobScore)
