# Problem: https://www.hackerrank.com/challenges/coin-change/problem
# Score: 60


n, m = map(int, input().split())
coins = l..(map(int, input().split()))
ans = [1] + [0] * n
___ i __ r..(m):
    ___ j __ r..(coins[i], n + 1):
        ans[j] += ans[j - coins[i]]
print(ans[-1])
