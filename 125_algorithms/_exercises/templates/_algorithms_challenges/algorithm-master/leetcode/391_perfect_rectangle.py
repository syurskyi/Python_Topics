______ collections


class Solution:
    ___ isRectangleCover(self, recs
        """
        :type recs: List[List[int]]
        :rtype: bool
        """
        __ not recs:
            r_ False

        left = bottom = float('inf')
        right = top = float('-inf')
        points = collections.defaultdict(int)

        ___ l, b, r, t in recs:
            left = min(left, l)
            bottom = min(bottom, b)
            right = max(right, r)
            top = max(top, t)

            ___ x, y, val in (
                (l, b, 1),
                (r, b, 2),
                (r, t, 4),
                (l, t, 8),

                __ points[x, y] & val:
                    r_ False
                points[x, y] |= val

        __ any(
            # only check the mid-points
            val not in (3, 6, 9, 12, 15)
            ___ (x, y), val in points.items()
            __ left < x < right or bottom < y < top

            r_ False

        r_ True
