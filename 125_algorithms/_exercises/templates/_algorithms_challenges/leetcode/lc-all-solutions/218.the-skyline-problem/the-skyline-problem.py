_______ heapq


c_ Solution(object):
  ___ getSkyline  buildings):
    """
    :type buildings: List[List[int]]
    :rtype: List[List[int]]
    """
    hs    # list
    heap    # list
    ___ b __ buildings:
      hs.a..((b[0], -b[2]))
      hs.a..((b[1], b[2]))
    hs.s..()
    ans    # list
    pre = cur = N..
    ___ h __ hs:
      pos = h[0]
      height = h[1]
      __ height < 0:
        heapq.heappush(heap, height)
      ____:
        i = heap.index(-height)
        heap[i] = heap[-1]
        heap.pop()
        __ i < l..(heap):
          heapq._siftup(heap, i)
          heapq._siftdown(heap, 0, i)
      __ heap:
        cur = heap[0]
        __ cur != pre:
          ans.a..((pos, -1 * cur))
          pre = cur
      ____:
        ans.a..((pos, 0))

    r.. ans
