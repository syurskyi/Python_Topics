# Problem: https://www.hackerrank.com/challenges/sherlock-and-cost/problem
# Score: 50


test = int(input())
___ i in range(test
    n = int(input())
    b = list(map(int, input().split()))

    dp = [[0], [0]]

    ___ i in range(1, le.(b)):
        add_1 = max(dp[0][-1], dp[1][-1] + b[i - 1] - 1)
        add_max = max(dp[0][-1] + b[i] - 1, dp[1][-1] + abs(b[i] - b[i - 1]))
        dp[0].append(add_1)
        dp[1].append(add_max)

    print(max(dp[0][-1], dp[1][-1]))
