____ collections _______ defaultdict

class Solution(object):
  
  ___ findLonelyPixel(self, picture):

      col = defaultdict(int)
      row = defaultdict(int)

      ___ i, r __ enumerate(picture):
        ___ j, pixel __ enumerate(r):
          __ pixel __ "B":
            row[i] += 1
            col[j] += 1

      r.. s..(
          1 ___ i, r __ enumerate(picture)
          ___ j, pixel __ enumerate(r)
          __ col[j] __ row[i] __ 1 and pixel __ 'B'
      )
