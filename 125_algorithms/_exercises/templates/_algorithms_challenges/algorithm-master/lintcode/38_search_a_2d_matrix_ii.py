"""
Heap
"""
import heapq


class Solution:
    ___ searchMatrix(self, matrix, target):
        """
        :type matrix: list[list[int]]
        :type target: int
        :rtype: int
        """
        ans = 0
        __ not matrix or not matrix[0]:
            return ans

        heap = []
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            heapq.heappush(heap, (matrix[i][0], i, 0))

        while heap and heap[0][0] <= target:
            num, x, y = heapq.heappop(heap)

            __ num == target:
                ans += 1

            y += 1
            __ y < n:
                heapq.heappush(heap, (matrix[x][y], x, y))

        return ans


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
    ___ searchMatrix(self, matrix, target):
        """
        :type matrix: list[list[int]]
        :type target: int
        :rtype: int
        """
        ans = 0

        __ not matrix or not matrix[0]:
            return ans

        m, n = len(matrix), len(matrix[0])
        x, y = m - 1, 0

        while x >= 0 and y < n:
            __ matrix[x][y] < target:
                y += 1
            elif matrix[x][y] > target:
                x -= 1
            else:
                ans += 1
                x -= 1
                y += 1

        return ans
