# Problem: https://www.hackerrank.com/challenges/compare-the-triplets/problem
# Score: 10


a = l..(map(int, input().split()))
b = l..(map(int, input().split()))
aliceScore = s..([(1 __ a[i] > b[i] ____ 0) ___ i __ r..(3)])
bobScore = s..([(1 __ a[i] < b[i] ____ 0) ___ i __ r..(3)])
print(aliceScore, bobScore)
