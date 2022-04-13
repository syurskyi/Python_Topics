c_ Solution:
    ___ searchMatrix  matrix, target
        """
        :type matrix: list[list[int]]
        :type target: int
        :rtype: bool
        """
        __ n.. matrix o. n.. matrix[0]:
            r.. F..

        m, n l..(matrix), l..(matrix 0
        left, right 0, m * n - 1

        w.... left + 1 < right:
            mid (left + right) // 2
            x mid // n
            y mid % n

            __ matrix[x][y] < target:
                left mid
            ____ matrix[x][y] > target:
                right mid
            ____
                r.. T..

        r.. a__(
            matrix[mid // n][mid % n] __ target
            ___ mid __ (left, right)
        )
