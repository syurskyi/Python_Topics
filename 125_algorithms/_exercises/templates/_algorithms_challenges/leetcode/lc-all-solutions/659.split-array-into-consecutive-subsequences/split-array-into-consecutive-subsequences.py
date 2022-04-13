c_ Solution(o..
  ___ isPossible  nums
    """
    :type nums: List[int]
    :rtype: bool
    """
    d c...d.. l..
    ___ num __ nums:
      __ d[num - 1]:
        h__.heappush(d[num], h__.heappop(d[num - 1]) + 1)
      ____
        h__.heappush(d[num], 1)
    r.. n.. a__(length < 3 ___ length __ s..(d.v.., []
