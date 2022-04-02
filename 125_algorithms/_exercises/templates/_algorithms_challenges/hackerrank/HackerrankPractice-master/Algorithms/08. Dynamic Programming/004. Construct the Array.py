# Problem: https://www.hackerrank.com/challenges/construct-the-array/problem
# Score: 35


___ count_array(n, k, x
    dp = [[1], [1]]
    __ x __ 1:
        dp = [[1], [0]]
    ____:
        dp = [[1], [1]]

    ___ x __ r..(n - 2
        dp[0].a..(dp[0][-1] * (k - 1) % (10 ** 9 + 7))
        dp[1].a..((dp[0][-1] - dp[1][-1]) % (10 ** 9 + 7))
    r.. dp[1][-1]


n, k, x = map(i.., input().s..())
print(count_array(n, k, x))
