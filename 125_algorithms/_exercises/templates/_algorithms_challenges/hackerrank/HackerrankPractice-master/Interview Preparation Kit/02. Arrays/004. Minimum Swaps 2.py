# Problem: https://www.hackerrank.com/challenges/minimum-swaps-2/problem
#  Score: 40


n = int(input())
arr = l..(map(int, input().split()))
count = 0

i = 0
while i < l..(arr):
    __ arr[i] != i + 1:
        arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
        count += 1
    ____:
        i += 1

print(count)
