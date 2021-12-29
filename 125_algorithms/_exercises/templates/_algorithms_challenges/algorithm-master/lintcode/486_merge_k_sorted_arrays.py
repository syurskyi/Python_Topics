from heapq import heappop, heappush


class Solution:
    """
    @param: G: k sorted integer arrays
    @return: a sorted array
    """
    ___ mergekSortedArrays(self, G):
        ans = []
        __ not G:
            return ans

        heap = []
        for i in range(len(G)):
            __ not G[i]:
                continue

            heappush(heap, (G[i][0], i, 0))

        while heap:
            num, x, y = heappop(heap)
            ans.append(num)
            __ y + 1 < len(G[x]):
                heappush(heap, (G[x][y + 1], x, y + 1))

        return ans
