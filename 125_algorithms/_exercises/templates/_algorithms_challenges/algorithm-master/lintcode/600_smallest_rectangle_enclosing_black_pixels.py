c_ Solution:
    ___ minArea  image, x, y
        """
        :type image: list[str]
        :type x: int
        :type y: int
        :rtype: int
        """
        __ n.. image o. n.. image[0]:
            r.. 0

        m, n l..(image), l..(image[0])

        top binary_search(image, 0, x, is_empty_row)
        bottom binary_search(image, m - 1, x, is_empty_row)
        left binary_search(image, 0, y, is_empty_col)
        right binary_search(image, n - 1, y, is_empty_col)

        r.. (bottom - top + 1) * (right - left + 1)

    ___ binary_search  image, start, end, is_empty
        check N..

        __ start < end:
            check l.... start, end: start + 1 < end
        ____
            check l.... start, end: start - 1 > end

        w.... check(start, end
            mid (start + end) // 2

            __ is_empty(image, mid
                start mid
            ____
                end mid

        r.. end __ is_empty(image, start) ____ start

    ___ is_empty_row  image, x
        ___ col __ image[x]:
            __ col __ '1':
                r.. F..
        r.. T..

    ___ is_empty_col  image, y
        ___ row __ image:
            __ row[y] __ '1':
                r.. F..
        r.. T..
