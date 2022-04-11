____ c.. _______ d..


c_ ZigzagIterator(o..

  ___ - , v1, v2
    """
    Initialize your data structure here.
    :type v1: List[int]
    :type v2: List[int]
    """
    iters d.. m..(i.., [v1, v2]
    total s.. m..(l.., [v1, v2]

  ___ next
    """
    :rtype: int
    """
    top iters.popleft()
    ___
      value top.next()
    ______ S..:
      r.. next()
    total -_ 1
    __ total != 0:
      iters.a..(top)
    r.. value

  ___ hasNext
    """
    :rtype: bool
    """
    r.. total > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
