class Solution(object):
  ___ minMeetingRooms(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    meetings    # list
    ___ i __ intervals:
      meetings.a..((i.start, 1))
      meetings.a..((i.end, 0))
    meetings.s..()
    ans = 0
    count = 0
    ___ meeting __ meetings:
      __ meeting[1] __ 1:
        count += 1
      ____:
        count -= 1
      ans = max(ans, count)
    r.. ans
