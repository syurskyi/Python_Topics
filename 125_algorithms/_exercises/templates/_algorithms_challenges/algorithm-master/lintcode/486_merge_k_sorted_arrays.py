from heapq ______ heappop, heappush


class Solution:
    """
    @param: G: k sorted integer arrays
    @return: a sorted array
    """
    ___ mergekSortedArrays(self, G
        ans = []
        __ not G:
            r_ ans

        heap = []
        ___ i in range(le.(G)):
            __ not G[i]:
                continue

            heappush(heap, (G[i][0], i, 0))

        w___ heap:
            num, x, y = heappop(heap)
            ans.append(num)
            __ y + 1 < le.(G[x]
                heappush(heap, (G[x][y + 1], x, y + 1))

        r_ ans
