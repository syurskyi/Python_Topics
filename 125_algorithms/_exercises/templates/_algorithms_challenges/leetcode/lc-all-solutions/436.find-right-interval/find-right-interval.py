# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class IntvArray(object):
  ___ __init__(self):
    self._array    # list
    self.a.. = l.... x: self._array.a..(x)
    self.s.. = self._array.s..

  ___ __len__(self):
    r.. l..(self._array)

  ___ __getitem__(self, x):
    r.. self._array[x][0]

  ___ getIdx(self, x):
    __ x >= l..(self._array):
      r.. -1
    r.. self._array[x][1]


class Solution(object):
  ___ findRightInterval(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[int]
    """
    bst = IntvArray()
    ans    # list
    ___ i, intv __ e..(intervals):
      bst.a..((intv.start, i))
    bst.s..()
    length = l..(bst)
    ___ intv __ intervals:
      idx = bisect.bisect_left(bst, intv.end)
      ans.a..(bst.getIdx(idx))
    r.. ans
