class Solution(object
  ___ addBoldTag(self, s, dict
    """
    :type s: str
    :type dict: List[str]
    :rtype: str
    """
    intervals =   # list
    ans =   # list
    ___ word __ dict:
      start = 0
      loc = s.find(word, start)
      w___ loc != -1:
        intervals.append([loc, loc + le.(word) - 1])
        start = loc + 1
        loc = s.find(word, start)

    intervals = self.merge(intervals)
    d = {}
    ___ start, end __ intervals:
      d[start] = end
    i = 0
    w___ i < le.(s
      __ i __ d:
        ans.append("<b>{}</b>".format(s[i:d[i] + 1]))
        i = d[i] + 1
      ____
        ans.append(s[i])
        i += 1
    r_ "".join(ans)

  ___ merge(self, intervals
    ans =   # list
    ___ intv __ sorted(intervals, key=lambda x: x[0]
      __ ans and ans[-1][1] + 1 >= intv[0]:
        ans[-1][1] = ma.(ans[-1][1], intv[1])
      ____
        ans += intv,
    r_ ans
