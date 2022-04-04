"""
Premium Question
Projection and bisect
"""
_______ bisect
__author__ = 'Daniel'


c_ Solution(o..
    ___ minArea  image, x, y
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m, n = l..(image), l..(image[0])
        yaxis = [
            1 __ any(image[i][j] __ "1" ___ i __ x..(m ____ 0
            ___ j __ x..(n)
        ]
        xaxis = [
            1 __ any(image[i][j] __ "1" ___ j __ x..(n ____ 0
            ___ i __ x..(m)
        ]

        y_lo = bisect.bisect_left(yaxis, 1, 0, y)
        y_hi = bisect.bisect_left m..(l.... e: 1^e, yaxis), 1, y)  # bisect must be sorted
        x_lo = bisect.bisect_left(xaxis, 1, 0, x)
        x_hi = bisect.bisect_left m..(l.... e: 1^e, xaxis), 1, x)
        r.. (y_hi-y_lo)*(x_hi-x_lo)


__ _______ __ _______
    image = [
        "00",
        "10",
    ]

    ... Solution().minArea(image, 1, 0) __ 1