class Solution:
    ___ countCornerRectangles(self, G
        """
        :type G: List[List[int]]
        :rtype: int

        iterate every row and save all the pairs of 1 in current row
        if there is some pair with same indices in passed row
        and then we can ensure rectangles exist

        note that:
        1 pair:  0 rec
        2 pairs: 0+1= 1 rec
        4 pairs: 0+1+2+3= 6 recs
        n pairs: C(n, 2) = n * (n - 1) / 2 = 0+1+2+...+(n-1)

        example: 4 pairs => C(4, 2) = 6 recs
        1   1
        1   1
        1   1
        1   1
        """
        ans = 0

        __ not G:
            r_ ans

        n = 0
        count = {}
        for R in G:
            for end in range(1, le.(R)):
                __ R[end] __ 0:
                    continue

                for start in range(end
                    __ R[start] __ 0:
                        continue

                    __ (start, end) not in count:
                        count[start, end] = 0
                        continue

                    count[start, end] += 1

                    ans += count[start, end]

        r_ ans
