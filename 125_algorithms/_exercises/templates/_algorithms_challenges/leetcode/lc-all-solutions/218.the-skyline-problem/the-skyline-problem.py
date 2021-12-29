import heapq


class Solution(object):
  ___ getSkyline(self, buildings):
    """
    :type buildings: List[List[int]]
    :rtype: List[List[int]]
    """
    hs = []
    heap = []
    for b in buildings:
      hs.append((b[0], -b[2]))
      hs.append((b[1], b[2]))
    hs.sort()
    ans = []
    pre = cur = None
    for h in hs:
      pos = h[0]
      height = h[1]
      __ height < 0:
        heapq.heappush(heap, height)
      else:
        i = heap.index(-height)
        heap[i] = heap[-1]
        heap.pop()
        __ i < len(heap):
          heapq._siftup(heap, i)
          heapq._siftdown(heap, 0, i)
      __ heap:
        cur = heap[0]
        __ cur != pre:
          ans.append((pos, -1 * cur))
          pre = cur
      else:
        ans.append((pos, 0))

    return ans
