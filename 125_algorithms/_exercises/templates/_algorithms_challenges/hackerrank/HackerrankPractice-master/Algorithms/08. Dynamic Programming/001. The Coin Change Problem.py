# Problem: https://www.hackerrank.com/challenges/coin-change/problem
# Score: 60


n, m m.. i.., i.. ).s..
coins l.. m..(i.., i.. ).s..()))
ans [1] + [0] * n
___ i __ r..(m
    ___ j __ r..(coins[i], n + 1
        ans[j] += ans[j - coins[i]]
print(ans[-1])
