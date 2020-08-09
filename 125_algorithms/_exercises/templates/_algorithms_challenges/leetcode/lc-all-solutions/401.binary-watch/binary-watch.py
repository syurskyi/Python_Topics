class Solution(object
  ___ readBinaryWatch(self, num
    """
    :type num: int
    :rtype: List[str]
    """
    ans = []
    for i in range(0, 12
      for j in range(0, 60
        __ (bin(i) + bin(j)).count("1") __ num:
          ans.append("%d:%02d" % (i, j))
    r_ ans
