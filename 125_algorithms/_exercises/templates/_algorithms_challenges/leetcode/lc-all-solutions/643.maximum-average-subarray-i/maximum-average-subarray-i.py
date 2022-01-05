____ c.. _______ d..


c_ Solution(o..):
  ___ findMaxAverage  nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    s = 0
    ans = float("-inf")
    queue = d..([])
    ___ num __ nums:
      queue.a..(num)
      s += num
      __ l..(queue) > k:
        s -= queue.popleft()
      __ l..(queue) __ k:
        ans = m..(ans, float(s) / k)
    r.. ans
