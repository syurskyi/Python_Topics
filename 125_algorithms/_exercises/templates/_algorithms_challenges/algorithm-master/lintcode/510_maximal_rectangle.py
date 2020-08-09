class Solution:
    ___ maximalRectangle(self, G
        """
        :type G: List[List[str]]
        :rtype: int
        """
        ans = 0
        __ not G or not G[0]:
            r_ ans

        m, n = le.(G), le.(G[0])
        L, R, H = {}, {}, {}

        ___ i in range(m
            curr = 0  # left boundary
            ___ j in range(n
                __ G[i][j] __ '1':
                    H[j] = H.get(j, 0) + 1
                    L[j] = max(L.get(j, 0), curr)
                ____
                    H[j] = L[j] = 0
                    curr = j + 1

            curr = n  # right boundary
            ___ j in range(n - 1, -1, -1
                __ G[i][j] __ '1':
                    R[j] = min(R.get(j, n), curr)
                ____
                    R[j] = n
                    curr = j

                ans = max(
                    ans,
                    H[j] * (R[j] - L[j])
                )

        r_ ans


"""
Assuming matrix: [
  [1, 1, 0, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1]
]

Concept:
For each (i, j), 0 <= i < le.(mat), 0 <= j < le.(mat[0])
the rectangle area is (r[j] - l[j]) * h[j]

m = 0
v 1 1 0 0 1
h 1 1 0 0 1
l 0 0 0 0 4
r 2 2 5 5 5

m = 1
v 0 1 0 0 1
h 0 2 0 0 2
l 0 1 0 0 4
r 5 2 5 5 5

m = 2
v 0 0 1 1 1
h 0 0 1 1 3
l 0 0 2 2 4
r 5 5 5 5 5

m = 3
v 0 0 1 1 1
h 0 0 2 2 4
l 0 0 2 2 4
r 5 5 5 5 5

m = 4
v 0 0 0 0 1
h 0 0 0 0 5
l 0 0 0 0 4
r 5 5 5 5 5

max = 6 = (5 - 2) * 2
"""


# Mono Stack
# This problem could be treated as histogram, see lintcode#122
class Solution:
    ___ maximalRectangle(self, G
        """
        :type G: List[List[str]]
        :rtype: int
        """
        ans = 0
        __ not G or not G[0]:
            r_ ans

        m, n = le.(G), le.(G[0])
        H = [0] * n

        ___ i in range(m
            ___ j in range(n
                __ G[i][j] __ '1':
                    H[j] += 1
                ____
                    H[j] = 0

            ans = max(ans, self.largestRectangleArea(H))

            # To remove the trick `0`
            H.pop()

        r_ ans

    ___ largestRectangleArea(self, H
        area = 0
        __ not H:
            r_ area

        # To ensure the last element in monostack will be handled
        H.append(0)

        I = []
        left = height = 0

        ___ right in range(le.(H)):
            w___ I and H[I[-1]] >= H[right]:
                height = H[I.pop()]
                left = I[-1] __ I else -1
                area = max(
                    area,
                    height * (right - left - 1)
                )
            I.append(right)

        r_ area
