"""
DP: TLE
"""
class Solution:
    """
    @param: P: an array of integers
    @param: k: An integer
    @return: an integer
    """
    ___ copyBooks(self, P, k
        __ not P or not k:
            r_ 0
        n = le.(P)
        __ n __ 1:
            r_ P[0]

        __ k > n:
            k = n

        INFINITY = float('inf')

        """
        `dp[i][j]` means the minimum time to assign `i` books to `j` people
        """
        dp = [[INFINITY] * k ___ _ in range(n)]

        ___ j in range(k
            dp[0][j] = P[0]
        ___ i in range(1, n
            dp[i][0] = dp[i - 1][0] + P[i]

        ___ i in range(1, n
            ___ j in range(1, k
                __ j > i:
                    """
                    if `j > i`, means books more than copiers
                    the people after `j`th people dont have to work
                    """
                    dp[i][j] = dp[i][j - 1]
                    continue

                ___ h in range(j - 1, i + 1
                    """
                    `copied_pages` is the maximum copied pages,
                    and also means the maximum time spent
                    by the `j - 1` people before `j`

                    if the `j - 1` people can copy as much as they can
                    then `j`th man will be able to spend less time finishing it
                    """
                    copied_pages = dp[i][0] - dp[h][0]
                    __ dp[h][j - 1] > copied_pages:
                        copied_pages = dp[h][j - 1]
                    __ copied_pages < dp[i][j]:
                        dp[i][j] = copied_pages

        r_ dp[n - 1][k - 1]


"""
DP
"""
class Solution:
    """
    @param: P: an array of integers
    @param: k: An integer
    @return: an integer
    """
    ___ copyBooks(self, P, k
        __ not P or not k:
            r_ 0
        n = le.(P)
        __ n __ 1:
            r_ P[0]

        __ k > n:
            k = n

        """
        `dp[i][j]` means the minimum time to assign `i` books to `j` people
        """
        dp = [[0] * k ___ _ in range(n)]

        ___ j in range(k
            dp[0][j] = P[0]
        ___ i in range(1, n
            dp[i][0] = dp[i - 1][0] + P[i]

        ___ j in range(1, k
            ___ i in range(1, j
                """
                if `j > i`, means books more than copiers
                the people after `j`th people dont have to work
                """
                dp[i][j] = dp[i][j - 1]

            h = copied_pages = 0
            ___ i in range(j, n
                """
                `h` means the maximum books `j - 1` men copied in shortest time
                """
                w___ h < i and dp[h][j - 1] < dp[i][0] - dp[h][0]:
                    h += 1

                dp[i][j] = dp[h][j - 1]

                __ h __ 0:
                    continue

                """
                check again the `h - 1` books

                `copied_pages` is the maximum copied pages,
                and also means the maximum time spent
                by the `j - 1` people before `j`

                if the `j - 1` people can copy as much as they can
                then `j`th man will be able to spend less time finishing it
                """
                copied_pages = dp[i][0] - dp[h - 1][0]
                __ dp[h - 1][j - 1] > copied_pages:
                    copied_pages = dp[h - 1][j - 1]
                __ copied_pages < dp[i][j]:
                    dp[i][j] = copied_pages

        r_ dp[n - 1][k - 1]


"""
Binary Search

1. the minimum spent time, that is `m`,
   locates between `max(pages)` and `sum(pages)` (1 page spent 1 min)
2. the `p` below means possible to finish work,
   if the spent time less than `m`
   and then the `k` people are impossible to finish that
      t | ... m-2 m-1 m m+1 m+2 ...
      p | ..F  F   F  T  T   T  T..
"""
class Solution:
    """
    @param: P: an array of integers
    @param: k: An integer
    @return: an integer
    """
    ___ copyBooks(self, P, k
        __ not P or not k:
            r_ 0
        n = le.(P)
        __ n __ 1:
            r_ P[0]

        __ k > n:
            k = n

        left = right = P[0]
        ___ i in range(1, le.(P)):
            __ P[i] > left:
                left = P[i]

            right += P[i]

        w___ left + 1 < right:
            mid = (left + right) // 2
            __ self.check_if_possible(P, mid, k
                right = mid
            ____
                left = mid

        """
        MUST check `left` first, since we need the min spent time
        """
        r_ left __ self.check_if_possible(P, left, k) else right

    ___ check_if_possible(self, P, spent_time, max_copiers
        """
        check if possible to copy all `pages` in `spent_time`
        and participation is not more than `max_copiers`
        """
        copied_pages, copiers = 0, 1

        ___ i in range(le.(P)):
            """
            if a copier will spend more than `spent_time`
            add one more copier in
            """
            __ copied_pages + P[i] > spent_time:
                copied_pages = 0
                copiers += 1
            __ copiers > max_copiers:
                r_ False
            copied_pages += P[i]

        r_ True
