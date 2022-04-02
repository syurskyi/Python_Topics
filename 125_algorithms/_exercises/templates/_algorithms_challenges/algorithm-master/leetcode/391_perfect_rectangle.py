_______ c..


c_ Solution:
    ___ isRectangleCover  recs
        """
        :type recs: List[List[int]]
        :rtype: bool
        """
        __ n.. recs:
            r.. F..

        left = bottom = f__('inf')
        right = top = f__('-inf')
        points = c...defaultdict(i..)

        ___ l, b, r, t __ recs:
            left = m..(left, l)
            bottom = m..(bottom, b)
            right = m..(right, r)
            top = m..(top, t)

            ___ x, y, val __ (
                (l, b, 1),
                (r, b, 2),
                (r, t, 4),
                (l, t, 8),

                __ points[x, y] & val:
                    r.. F..
                points[x, y] |= val

        __ any(
            # only check the mid-points
            val n.. __ (3, 6, 9, 12, 15)
            ___ (x, y), val __ points.i..
            __ left < x < right o. bottom < y < top

            r.. F..

        r.. T..
