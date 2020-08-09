# Problem: https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
#  Score: 30


n = int(input())
a = list(map(int, input().split()))

count = 0

___ i in range(n
    ___ j in range(n-1
        __ a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            count += 1

print('Array is sorted in', count, 'swaps.')
print('First Element:', a[0])
print('Last Element:', a[-1])
