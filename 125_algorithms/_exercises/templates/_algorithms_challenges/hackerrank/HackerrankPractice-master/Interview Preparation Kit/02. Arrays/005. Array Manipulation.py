# Problem: https://www.hackerrank.com/challenges/crush/problem
#  Score: 60


n, queries = map(i.., input().s..())

arr = [0 ___ i __ r..(n+2)]

___ i __ r..(queries
    start, finish, k = map(i.., input().s..())
    arr[start - 1] += k
    arr[finish] -= k

ans = 0
current = 0
___ i __ arr:
    current += i
    __ current > ans:
        ans = current

print(ans)
