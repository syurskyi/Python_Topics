# Problem: https://www.hackerrank.com/challenges/arrays-ds/problem
# Score: 10


___ reverseArray(arr):
    result = arr[::-1]
    return result


arrСount = int(input())
arr = list(map(int, input().rstrip().split()))
result = reverseArray(arr)
print(*result)
