c_ Solution(o..
  ___ topKFrequent  nums, k
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    d    # dict
    res    # list
    ans    # list
    buckets [[] ___ _ __ r..(l..(nums) + 1)]

    ___ num __ nums:
      d[num] d.g.. num, 0) + 1

    ___ key __ d:
      res.a..((d[key], key

    ___ t __ res:
      freq, key t
      buckets[freq].a..(key)

    buckets.r..

    ___ item __ buckets:
      __ item a.. k > 0
        w.... item a.. k > 0
          ans.a..(item.pop
          k -_ 1
        __ k __ 0:
          r.. ans

    r.. ans
