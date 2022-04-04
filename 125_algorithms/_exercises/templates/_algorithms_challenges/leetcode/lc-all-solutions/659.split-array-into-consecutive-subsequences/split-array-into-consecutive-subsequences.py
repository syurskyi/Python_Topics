c_ Solution(o..
  ___ isPossible  nums
    """
    :type nums: List[int]
    :rtype: bool
    """
    d = c...d..(l..)
    ___ num __ nums:
      __ d[num - 1]:
        heapq.heappush(d[num], heapq.heappop(d[num - 1]) + 1)
      ____
        heapq.heappush(d[num], 1)
    r.. n.. any(length < 3 ___ length __ s..(d.v.., []
