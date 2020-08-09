class Solution:
    ___ lexicalOrder(self, n
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []

        __ not n:
            r_ ans

        stack = [1]

        w___ stack:
            x = stack.pop()
            ans.append(x)

            # considering the case no carry up if x + 1
            # that is, x in [1, 8]
            __ x < n and x % 10 < 9:
                stack.append(x + 1)

            __ x * 10 <= n:
                stack.append(x * 10)

        r_ ans
