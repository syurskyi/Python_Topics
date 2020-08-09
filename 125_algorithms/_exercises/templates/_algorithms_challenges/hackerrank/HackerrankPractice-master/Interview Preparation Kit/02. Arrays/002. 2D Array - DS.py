# Problem: https://www.hackerrank.com/challenges/2d-array/problem
#  Score: 15


___ hourglasses(arr, i, j
    r_ sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])


arr = []
for i in range(6
    arr.append(list(map(int, input().split())))

ans = hourglasses(arr, 0, 0)
for i in range(4
    for j in range(4
        ans = max(ans, hourglasses(arr, i, j))
print(ans)
