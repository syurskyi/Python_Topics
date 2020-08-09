"""
Heap
"""
______ heapq


class Solution:
    ___ searchMatrix(self, matrix, target
        """
        :type matrix: list[list[int]]
        :type target: int
        :rtype: int
        """
        ans = 0
        __ not matrix or not matrix[0]:
            r_ ans

        heap = []
        m, n = le.(matrix), le.(matrix[0])

        ___ i in range(m
            heapq.heappush(heap, (matrix[i][0], i, 0))

        w___ heap and heap[0][0] <= target:
            num, x, y = heapq.heappop(heap)

            __ num __ target:
                ans += 1

            y += 1
            __ y < n:
                heapq.heappush(heap, (matrix[x][y], x, y))

        r_ ans


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
class Solution:
    ___ searchMatrix(self, matrix, target
        """
        :type matrix: list[list[int]]
        :type target: int
        :rtype: int
        """
        ans = 0

        __ not matrix or not matrix[0]:
            r_ ans

        m, n = le.(matrix), le.(matrix[0])
        x, y = m - 1, 0

        w___ x >= 0 and y < n:
            __ matrix[x][y] < target:
                y += 1
            ____ matrix[x][y] > target:
                x -= 1
            ____
                ans += 1
                x -= 1
                y += 1

        r_ ans
