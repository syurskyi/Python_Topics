class Solution(object
  ___ minMeetingRooms(self, intervals
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    meetings = []
    for i in intervals:
      meetings.append((i.start, 1))
      meetings.append((i.end, 0))
    meetings.sort()
    ans = 0
    count = 0
    for meeting in meetings:
      __ meeting[1] __ 1:
        count += 1
      ____
        count -= 1
      ans = max(ans, count)
    r_ ans
