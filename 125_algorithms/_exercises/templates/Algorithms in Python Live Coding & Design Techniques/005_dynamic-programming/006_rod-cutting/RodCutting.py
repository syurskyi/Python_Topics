_____ sys


# Recursive Approach (exponential)
___ rod_cut(price, n
    __ n __ 0:
        r_ 0
    max_revenue = -sys.maxsize
    ___ i __ ra__(1, n + 1
        max_revenue = ma_(max_revenue, price[i - 1] + rod_cut(price, n - i))
    r_ max_revenue


# DP : Top Down Approach O(n^2)
___ rod_cut_topdown(price, n, dp
    __ n __ 0:
        r_ 0

    __ dp[n - 1] > 0:
        r_ dp[n - 1]

    max_revenue = -sys.maxsize
    ___ i __ ra__(1, n + 1
        max_revenue = ma_(max_revenue, price[i - 1] + rod_cut_topdown(price, n - i, dp))
    dp[n - 1] = max_revenue
    r_ dp[n - 1]


# DP : Bottom Up Approach O(n^2)
___ rod_cut_bottomup(price, n
    revenues = [0] * (n + 1)
    # revenues[0] = 0

    max_revenue = -sys.maxsize
    ___ i __ ra__(1, n + 1
        ___ j __ ra__(1, i + 1
            max_revenue = ma_(max_revenue, price[j - 1] + revenues[i - j])
        revenues[i] = max_revenue
    r_ revenues[n]


__ ___ __ '__main__':
    price = [4, 5, 8, 9]
    size = le_(price)
    print('max revenue', rod_cut(price, size))

    dp = [0] * size
    print('max revenue (top down):', rod_cut_topdown(price, size, dp))

    print('max revenue (bottom up):', rod_cut_bottomup(price, size))
