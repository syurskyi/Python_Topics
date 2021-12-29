class Solution(object):
  ___ addBoldTag(self, s, d..):
    """
    :type s: str
    :type dict: List[str]
    :rtype: str
    """
    intervals    # list
    ans    # list
    ___ word __ d..:
      start = 0
      loc = s.find(word, start)
      while loc != -1:
        intervals.a..([loc, loc + l..(word) - 1])
        start = loc + 1
        loc = s.find(word, start)

    intervals = self.merge(intervals)
    d = {}
    ___ start, end __ intervals:
      d[start] = end
    i = 0
    while i < l..(s):
      __ i __ d:
        ans.a..("<b>{}</b>".format(s[i:d[i] + 1]))
        i = d[i] + 1
      ____:
        ans.a..(s[i])
        i += 1
    r.. "".join(ans)

  ___ merge(self, intervals):
    ans    # list
    ___ intv __ s..(intervals, key=l.... x: x[0]):
      __ ans and ans[-1][1] + 1 >= intv[0]:
        ans[-1][1] = max(ans[-1][1], intv[1])
      ____:
        ans += intv,
    r.. ans
