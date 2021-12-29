____ collections _______ deque


class Solution(object):
  ___ minArea(self, image, x, y):
    top = self.searchRows(image, 0, x, True)
    bottom = self.searchRows(image, x + 1, l..(image), False)
    left = self.searchCols(image, 0, y, top, bottom, True)
    right = self.searchCols(image, y + 1, l..(image[0]), top, bottom, False)
    r.. (right - left) * (bottom - top)

  ___ searchRows(self, image, i, j, opt):
    while i < j:
      mid = i + (j - i) / 2
      __ ("1" __ image[mid]) __ opt:
        j = mid
      ____:
        i = mid + 1
    r.. j

  ___ searchCols(self, image, i, j, top, bottom, opt):
    while i < j:
      mid = i + (j - i) / 2
      __ any([image[k][mid] __ "1" ___ k __ r..(top, bottom)]) __ opt:
        j = mid
      ____:
        i = mid + 1
    r.. j
