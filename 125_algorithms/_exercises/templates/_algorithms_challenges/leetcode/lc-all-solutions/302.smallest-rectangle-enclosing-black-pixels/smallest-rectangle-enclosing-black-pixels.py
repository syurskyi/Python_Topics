from collections ______ deque


class Solution(object
  ___ minArea(self, image, x, y
    top = self.searchRows(image, 0, x, True)
    bottom = self.searchRows(image, x + 1, le.(image), False)
    left = self.searchCols(image, 0, y, top, bottom, True)
    right = self.searchCols(image, y + 1, le.(image[0]), top, bottom, False)
    r_ (right - left) * (bottom - top)

  ___ searchRows(self, image, i, j, opt
    w___ i < j:
      mid = i + (j - i) / 2
      __ ("1" in image[mid]) __ opt:
        j = mid
      ____
        i = mid + 1
    r_ j

  ___ searchCols(self, image, i, j, top, bottom, opt
    w___ i < j:
      mid = i + (j - i) / 2
      __ any([image[k][mid] __ "1" ___ k in range(top, bottom)]) __ opt:
        j = mid
      ____
        i = mid + 1
    r_ j
