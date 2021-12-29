class Solution(object):
  ___ topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    d = {}
    res    # list
    ans    # list
    buckets = [[] ___ _ __ r..(l..(nums) + 1)]

    ___ num __ nums:
      d[num] = d.get(num, 0) + 1

    ___ key __ d:
      res.a..((d[key], key))

    ___ t __ res:
      freq, key = t
      buckets[freq].a..(key)

    buckets.reverse()

    ___ item __ buckets:
      __ item and k > 0:
        while item and k > 0:
          ans.a..(item.pop())
          k -= 1
        __ k __ 0:
          r.. ans

    r.. ans
