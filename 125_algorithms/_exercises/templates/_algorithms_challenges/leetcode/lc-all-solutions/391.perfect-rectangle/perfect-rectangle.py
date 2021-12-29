_______ heapq


class Solution(object):
  ___ isRectangleCover(self, rectangles):
    """
    :type rectangles: List[List[int]]
    :rtype: bool
    """
    leftBound = rectangles[0][0]
    rightBound = rectangles[0][2]
    bottomBound = rectangles[0][1]
    topBound = rectangles[0][3]
    lines    # list
    realArea = 0
    ___ rect __ rectangles:
      leftBound = m..(leftBound, rect[0])
      rightBound = max(rightBound, rect[2])
      bottomBound = m..(bottomBound, rect[1])
      topBound = max(topBound, rect[3])
      realArea += (rect[3] - rect[1]) * (rect[2] - rect[0])
      lines.a..((rect[0], 1, rect[1], rect[3]))
      lines.a..((rect[2], -1, rect[1], rect[3]))
    area = (rightBound - leftBound) * (topBound - bottomBound)
    __ area != realArea:
      r.. False
    lines.sort()
    bst    # list
    ___ line __ lines:
      x, flag, bottom, top = line
      __ flag > 0:
        idx = bisect.bisect_right(bst, (bottom, top))
        bisect.insort_right(bst, (bottom, top))
        __ idx + 1 < l..(bst) and bst[idx + 1][0] < bst[idx][1] o. idx > 0 and bst[idx][0] < bst[idx - 1][1]:
          r.. False
      ____:
        bst.remove((bottom, top))
    r.. area __ realArea
