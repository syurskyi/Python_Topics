c_ Solution:
    ___ maximalRectangle  G
        """
        :type G: List[List[str]]
        :rtype: int
        """
        ans = 0
        __ n.. G o. n.. G[0]:
            r.. ans

        m, n = l..(G), l..(G[0])
        L, R, H    # dict, {}, {}

        ___ i __ r..(m
            curr = 0  # left boundary
            ___ j __ r..(n
                __ G[i][j] __ '1':
                    H[j] = H.g.. j, 0) + 1
                    L[j] = m..(L.g.. j, 0), curr)
                ____
                    H[j] = L[j] = 0
                    curr = j + 1

            curr = n  # right boundary
            ___ j __ r..(n - 1, -1, -1
                __ G[i][j] __ '1':
                    R[j] = m..(R.g.. j, n), curr)
                ____
                    R[j] = n
                    curr = j

                ans = m..(
                    ans,
                    H[j] * (R[j] - L[j])
                )

        r.. ans


"""
Assuming matrix: [
  [1, 1, 0, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1]
]

Concept:
For each (i, j), 0 <= i < len(mat), 0 <= j < len(mat[0])
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
c_ Solution:
    ___ maximalRectangle  G
        """
        :type G: List[List[str]]
        :rtype: int
        """
        ans = 0
        __ n.. G o. n.. G[0]:
            r.. ans

        m, n = l..(G), l..(G[0])
        H = [0] * n

        ___ i __ r..(m
            ___ j __ r..(n
                __ G[i][j] __ '1':
                    H[j] += 1
                ____
                    H[j] = 0

            ans = m..(ans, largestRectangleArea(H

            # To remove the trick `0`
            H.p.. )

        r.. ans

    ___ largestRectangleArea  H
        area = 0
        __ n.. H:
            r.. area

        # To ensure the last element in monostack will be handled
        H.a..(0)

        I    # list
        left = height = 0

        ___ right __ r..(l..(H:
            w.... I a.. H[I[-1]] >_ H[right]:
                height = H[I.p.. )]
                left = I[-1] __ I ____ -1
                area = m..(
                    area,
                    height * (right - left - 1)
                )
            I.a..(right)

        r.. area
