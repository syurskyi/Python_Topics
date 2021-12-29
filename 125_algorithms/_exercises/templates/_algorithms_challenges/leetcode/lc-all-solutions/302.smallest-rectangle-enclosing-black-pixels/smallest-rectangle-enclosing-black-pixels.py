from collections import deque


class Solution(object):
  ___ minArea(self, image, x, y):
    top = self.searchRows(image, 0, x, True)
    bottom = self.searchRows(image, x + 1, len(image), False)
    left = self.searchCols(image, 0, y, top, bottom, True)
    right = self.searchCols(image, y + 1, len(image[0]), top, bottom, False)
    return (right - left) * (bottom - top)

  ___ searchRows(self, image, i, j, opt):
    while i < j:
      mid = i + (j - i) / 2
      __ ("1" in image[mid]) == opt:
        j = mid
      else:
        i = mid + 1
    return j

  ___ searchCols(self, image, i, j, top, bottom, opt):
    while i < j:
      mid = i + (j - i) / 2
      __ any([image[k][mid] == "1" for k in range(top, bottom)]) == opt:
        j = mid
      else:
        i = mid + 1
    return j
