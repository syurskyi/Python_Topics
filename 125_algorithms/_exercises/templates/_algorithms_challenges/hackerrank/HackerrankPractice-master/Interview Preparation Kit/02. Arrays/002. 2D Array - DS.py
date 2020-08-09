# Problem: https://www.hackerrank.com/challenges/2d-array/problem
#  Score: 15


___ hourglasses(arr, i, j
    r_ su.(arr[i][j:j+3]) + arr[i+1][j+1] + su.(arr[i+2][j:j+3])


arr = []
___ i in range(6
    arr.append(list(map(int, input().split())))

ans = hourglasses(arr, 0, 0)
___ i in range(4
    ___ j in range(4
        ans = max(ans, hourglasses(arr, i, j))
print(ans)
