# Definition for an interval.
# class Interval(object
#     ___ __init__(self, s=0, e=0
#         self.start = s
#         self.end = e
class IntvArray(object
  ___ __init__(self
    self._array = []
    self.append = lambda x: self._array.append(x)
    self.sort = self._array.sort

  ___ __len__(self
    r_ le.(self._array)

  ___ __getitem__(self, x
    r_ self._array[x][0]

  ___ getIdx(self, x
    __ x >= le.(self._array
      r_ -1
    r_ self._array[x][1]


class Solution(object
  ___ findRightInterval(self, intervals
    """
    :type intervals: List[Interval]
    :rtype: List[int]
    """
    bst = IntvArray()
    ans = []
    ___ i, intv in enumerate(intervals
      bst.append((intv.start, i))
    bst.sort()
    length = le.(bst)
    ___ intv in intervals:
      idx = bisect.bisect_left(bst, intv.end)
      ans.append(bst.getIdx(idx))
    r_ ans
