"""
Heap
"""
_______ heapq


c_ Solution:
    ___ searchMatrix  matrix, target
        """
        :type matrix: list[list[int]]
        :type target: int
        :rtype: int
        """
        ans = 0
        __ n.. matrix o. n.. matrix[0]:
            r.. ans

        heap    # list
        m, n = l..(matrix), l..(matrix[0])

        ___ i __ r..(m
            heapq.heappush(heap, (matrix[i][0], i, 0

        w.... heap a.. heap[0][0] <_ target:
            num, x, y = heapq.heappop(heap)

            __ num __ target:
                ans += 1

            y += 1
            __ y < n:
                heapq.heappush(heap, (matrix[x][y], x, y

        r.. ans


"""
Iteration

start from bottom-left of matrix

if `G[x][y] > target`:
    need to check `x - 1`
    all cells before `y - 1` are confirmed in last iteration
else:
    all cells before `x + 1` are confirmed in last iteration
    need to check `y + 1`
"""
c_ Solution:
    ___ searchMatrix  matrix, target
        """
        :type matrix: list[list[int]]
        :type target: int
        :rtype: int
        """
        ans = 0

        __ n.. matrix o. n.. matrix[0]:
            r.. ans

        m, n = l..(matrix), l..(matrix[0])
        x, y = m - 1, 0

        w.... x >_ 0 a.. y < n:
            __ matrix[x][y] < target:
                y += 1
            ____ matrix[x][y] > target:
                x -= 1
            ____
                ans += 1
                x -= 1
                y += 1

        r.. ans
