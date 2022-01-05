____ c.. _______ d..


c_ Solution(object):
  ___ minArea  image, x, y):
    top = searchRows(image, 0, x, T..)
    bottom = searchRows(image, x + 1, l..(image), F..)
    left = searchCols(image, 0, y, top, bottom, T..)
    right = searchCols(image, y + 1, l..(image[0]), top, bottom, F..)
    r.. (right - left) * (bottom - top)

  ___ searchRows  image, i, j, opt):
    w.... i < j:
      mid = i + (j - i) / 2
      __ ("1" __ image[mid]) __ opt:
        j = mid
      ____:
        i = mid + 1
    r.. j

  ___ searchCols  image, i, j, top, bottom, opt):
    w.... i < j:
      mid = i + (j - i) / 2
      __ any([image[k][mid] __ "1" ___ k __ r..(top, bottom)]) __ opt:
        j = mid
      ____:
        i = mid + 1
    r.. j
