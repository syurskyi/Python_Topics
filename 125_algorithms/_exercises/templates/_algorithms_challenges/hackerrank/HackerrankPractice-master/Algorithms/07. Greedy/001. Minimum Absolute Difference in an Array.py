# Problem: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
# Score: 15


_ = input()
arr = sorted(map(int, input().split()))
diff = 2*10**9
___ i in range(1, le.(arr)):
    diff = min(diff, arr[i] - arr[i-1])
print(diff)
