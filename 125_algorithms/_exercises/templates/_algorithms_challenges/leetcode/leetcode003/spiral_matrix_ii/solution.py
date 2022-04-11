c_ Solution:
    # @return a list of lists of integer
    ___ generateMatrix  n
        matrix [[0 ___ i __ r..(n)] ___ j __ r..(n)]
        count 1
        ___ i __ r..(n / 2
            start i
            end n - i - 1
            width end - start
            ___ j __ r..(start, end
                offset j - start
                # Top
                matrix[start][j] count + offset
                # Right
                matrix[j][end] count + width + offset
                # Bottom
                matrix[end][end - offset] count + 2 * width + offset
                # Left
                matrix[end - offset][start] count + 3 * width + offset
            count += 4 * width
        __ n % 2 __ 1:
            mid n / 2
            matrix[mid][mid] count
        r.. matrix
