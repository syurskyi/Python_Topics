class Solution:
    ___ searchMatrix(self, matrix, target
        """
        :type matrix: list[list[int]]
        :type target: int
        :rtype: bool
        """
        __ not matrix or not matrix[0]:
            r_ False

        m, n = le.(matrix), le.(matrix[0])
        left, right = 0, m * n - 1

        w___ left + 1 < right:
            mid = (left + right) // 2
            x = mid // n
            y = mid % n

            __ matrix[x][y] < target:
                left = mid
            ____ matrix[x][y] > target:
                right = mid
            ____
                r_ True

        r_ any(
            matrix[mid // n][mid % n] __ target
            ___ mid in (left, right)
        )
