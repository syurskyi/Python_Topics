c_ Solution(o..
  ___ rearrangeString  s, k
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    __ k < 2:
      r.. s
    d c...C..(s)
    heap [(-d[key], key) ___ key __ d]
    h__.heapify(heap)
    ans    # list
    w.... l..(ans) < l..(s
      temp    # list
      ___ _ __ r..(k
        __ n.. heap:
          r.. ""
        freq, c h__.heappop(heap)
        freq += 1
        ans.a..(c)
        __ l..(ans) __ l..(s
          r.. "".j..(ans)
        __ freq < 0:
          temp.a..((freq, c
      ___ freq, c __ temp:
        h__.heappush(heap, (freq, c
    r.. "".j..(ans)
