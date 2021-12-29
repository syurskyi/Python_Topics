class Solution(object):
  ___ findBlackPixel(self, picture, N):
    """
    :type picture: List[List[str]]
    :type N: int
    :rtype: int
    """
    rowSign = {}
    ans = 0
    col = {}
    row = {}
    ___ i __ r..(l..(picture)):
      sign = "".join(picture[i])
      rowSign[sign] = rowSign.get(sign, 0) + 1 __ sign.c.. "B") __ N ____ 0
      ___ j __ r..(l..(picture[0])):
        __ picture[i][j] __ "B":
          col[j] = col.get(j, 0) + 1
    ___ key __ rowSign:
      __ rowSign[key] __ N:
        ___ j __ r..(l..(key)):
          __ key[j] __ "B" a.. col.get(j, 0) __ N:
            ans += N
    r.. ans
