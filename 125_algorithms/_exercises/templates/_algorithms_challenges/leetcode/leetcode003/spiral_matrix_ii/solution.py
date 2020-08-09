class Solution:
    # @return a list of lists of integer
    ___ generateMatrix(self, n
        matrix = [[0 ___ i in range(n)] ___ j in range(n)]
        count = 1
        ___ i in range(n / 2
            start = i
            end = n - i - 1
            width = end - start
            ___ j in range(start, end
                offset = j - start
                # Top
                matrix[start][j] = count + offset
                # Right
                matrix[j][end] = count + width + offset
                # Bottom
                matrix[end][end - offset] = count + 2 * width + offset
                # Left
                matrix[end - offset][start] = count + 3 * width + offset
            count += 4 * width
        __ n % 2 __ 1:
            mid = n / 2
            matrix[mid][mid] = count
        r_ matrix
