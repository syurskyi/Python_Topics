# Problem: https://www.hackerrank.com/challenges/2d-array/problem
#  Score: 15


___ hourglasses(arr, i, j
    r.. s..(arr[i][j:j+3]) + arr[i+1][j+1] + s..(arr[i+2][j:j+3])


arr    # list
___ i __ r..(6
    arr.a..(l.. m..(i.., input().s..())))

ans = hourglasses(arr, 0, 0)
___ i __ r..(4
    ___ j __ r..(4
        ans = m..(ans, hourglasses(arr, i, j))
print(ans)
