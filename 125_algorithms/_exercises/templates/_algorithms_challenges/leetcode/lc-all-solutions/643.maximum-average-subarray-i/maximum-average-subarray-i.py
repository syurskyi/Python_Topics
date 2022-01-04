____ c.. _______ d..


c_ Solution(object):
  ___ findMaxAverage(self, nums, k):
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
        ans = max(ans, float(s) / k)
    r.. ans
