# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
c_ IntvArray(o..
  ___ -
    _array    # list
    a.. l.... x: _array.a..(x)
    s.. _array.s..

  ___ -l
    r.. l..(_array)

  ___ __getitem__  x
    r.. _array[x][0]

  ___ getIdx  x
    __ x >_ l..(_array
      r.. -1
    r.. _array[x][1]


c_ Solution(o..
  ___ findRightInterval  intervals
    """
    :type intervals: List[Interval]
    :rtype: List[int]
    """
    bst IntvArray()
    ans    # list
    ___ i, intv __ e..(intervals
      bst.a..((intv.start, i
    bst.s..()
    length l..(bst)
    ___ intv __ intervals:
      idx b__.bisect_left(bst, intv.end)
      ans.a..(bst.getIdx(idx
    r.. ans
