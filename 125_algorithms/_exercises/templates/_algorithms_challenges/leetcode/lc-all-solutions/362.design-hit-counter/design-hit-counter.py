c_ HitCounter(object):

  ___ - ):
    """
    Initialize your data structure here.
    """
    q = [(0, 0)] * 300

  ___ hit(self, timestamp):
    """
    Record a hit.
    @param timestamp - The current timestamp (in seconds granularity).
    :type timestamp: int
    :rtype: void
    """
    idx = timestamp % 300
    time, hit = q[idx]
    __ time != timestamp:
      q[idx] = timestamp, 1
    ____:
      q[idx] = time, hit + 1

  ___ getHits(self, timestamp):
    """
    Return the number of hits in the past 5 minutes.
    @param timestamp - The current timestamp (in seconds granularity).
    :type timestamp: int
    :rtype: int
    """
    ans = 0
    ___ i __ r..(0, l..(q)):
      time, hit = q[i]
      __ timestamp - time < 300:
        ans += hit
    r.. ans

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
