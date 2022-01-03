____ heapq _______ heappop, heappush


c_ Solution:
    """
    @param: G: k sorted integer arrays
    @return: a sorted array
    """
    ___ mergekSortedArrays(self, G):
        ans    # list
        __ n.. G:
            r.. ans

        heap    # list
        ___ i __ r..(l..(G)):
            __ n.. G[i]:
                continue

            heappush(heap, (G[i][0], i, 0))

        w.... heap:
            num, x, y = heappop(heap)
            ans.a..(num)
            __ y + 1 < l..(G[x]):
                heappush(heap, (G[x][y + 1], x, y + 1))

        r.. ans
