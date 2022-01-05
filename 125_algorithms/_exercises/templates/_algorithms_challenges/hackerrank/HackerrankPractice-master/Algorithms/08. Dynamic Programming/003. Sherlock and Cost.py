# Problem: https://www.hackerrank.com/challenges/sherlock-and-cost/problem
# Score: 50


test = i..(input())
___ i __ r..(test):
    n = i..(input())
    b = l..(map(i.., input().s..()))

    dp = [[0], [0]]

    ___ i __ r..(1, l..(b)):
        add_1 = m..(dp[0][-1], dp[1][-1] + b[i - 1] - 1)
        add_max = m..(dp[0][-1] + b[i] - 1, dp[1][-1] + abs(b[i] - b[i - 1]))
        dp[0].a..(add_1)
        dp[1].a..(add_max)

    print(m..(dp[0][-1], dp[1][-1]))
