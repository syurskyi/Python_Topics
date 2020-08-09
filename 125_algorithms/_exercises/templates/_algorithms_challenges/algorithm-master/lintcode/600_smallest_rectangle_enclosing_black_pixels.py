class Solution:
    ___ minArea(self, image, x, y
        """
        :type image: list[str]
        :type x: int
        :type y: int
        :rtype: int
        """
        __ not image or not image[0]:
            r_ 0

        m, n = le.(image), le.(image[0])

        top = self.binary_search(image, 0, x, self.is_empty_row)
        bottom = self.binary_search(image, m - 1, x, self.is_empty_row)
        left = self.binary_search(image, 0, y, self.is_empty_col)
        right = self.binary_search(image, n - 1, y, self.is_empty_col)

        r_ (bottom - top + 1) * (right - left + 1)

    ___ binary_search(self, image, start, end, is_empty
        check = None

        __ start < end:
            check = lambda start, end: start + 1 < end
        ____
            check = lambda start, end: start - 1 > end

        w___ check(start, end
            mid = (start + end) // 2

            __ is_empty(image, mid
                start = mid
            ____
                end = mid

        r_ end __ is_empty(image, start) else start

    ___ is_empty_row(self, image, x
        ___ col in image[x]:
            __ col __ '1':
                r_ False
        r_ True

    ___ is_empty_col(self, image, y
        ___ row in image:
            __ row[y] __ '1':
                r_ False
        r_ True
