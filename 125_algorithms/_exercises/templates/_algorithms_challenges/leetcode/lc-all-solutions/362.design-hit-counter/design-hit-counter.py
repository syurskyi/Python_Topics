c_ HitCounter(o..

  ___ -
    """
    Initialize your data structure here.
    """
    q [(0, 0)] * 300

  ___ hit  timestamp
    """
    Record a hit.
    @param timestamp - The current timestamp (in seconds granularity).
    :type timestamp: int
    :rtype: void
    """
    idx timestamp % 300
    t__, hit q[idx]
    __ t__ != timestamp:
      q[idx] timestamp, 1
    ____
      q[idx] t__, hit + 1

  ___ getHits  timestamp
    """
    Return the number of hits in the past 5 minutes.
    @param timestamp - The current timestamp (in seconds granularity).
    :type timestamp: int
    :rtype: int
    """
    ans 0
    ___ i __ r..(0, l..(q:
      t__, hit q[i]
      __ timestamp - t__ < 300:
        ans += hit
    r.. ans

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
