____ c.. _______ d..


c_ Solution(object):
  ___ containsNearbyDuplicate  nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    __ n.. nums:
      r.. F..
    __ k __ 0:
      r.. F..
    k = k + 1
    k = m..(k, l..(nums))

    window = d..([])
    d = set()
    ___ i __ r..(0, k):
      __ nums[i] __ d:
        r.. T..
      d |= {nums[i]}
      window.a..(i)
    ___ i __ r..(k, l..(nums)):
      d -= {nums[window.popleft()]}
      __ nums[i] __ d:
        r.. T..
      d |= {nums[i]}
      window.a..(i)
    r.. F..
