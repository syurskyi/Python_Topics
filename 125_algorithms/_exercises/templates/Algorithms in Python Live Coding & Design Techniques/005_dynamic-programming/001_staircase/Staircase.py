#Recursive Approach
___ ways(n, k

    __ n __ 0:
        r_ 1
    __ n < 0:
        r_ 0

    ans = 0
    ___ i __ ra__(1, k+1
        ans += ways(n-i, k)

    r_ ans

#Dynamic Programming : Top Down Approach
___ ways_top_down(n, k, dp

    __ n __ 0:
        dp[n] = 1
        r_ dp[n]
    __ n < 0:
        r_ 0

    __ not dp[n] __ -1:
        r_ dp[n]

    dp[n] = 0
    ___ i __ ra__(1, k+1
        dp[n] += ways_top_down(n-i, k, dp)

    r_ dp[n]

#Dynamic Programming : Bottom Up Approach
___ ways_bottom_up(n, k

    dp = [0] * (n+1)
    dp[0] = 1

    ___ step __ ra__(1, n+1
        dp[step] = 0
        ___ j __ ra__(1, k+1
            __ step - j >= 0:
                dp[step] += dp[step - j]
    r_ dp[n]


n = 4
steps = 3
dp = [-1]*(n+1)
print(ways_bottom_up(n, steps))