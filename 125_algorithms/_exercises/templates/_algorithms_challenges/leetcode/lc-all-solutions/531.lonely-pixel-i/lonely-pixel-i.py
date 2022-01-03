____ collections _______ defaultdict

c_ Solution(object):
  
  ___ findLonelyPixel(self, picture):

      col = defaultdict(int)
      row = defaultdict(int)

      ___ i, r __ e..(picture):
        ___ j, pixel __ e..(r):
          __ pixel __ "B":
            row[i] += 1
            col[j] += 1

      r.. s..(
          1 ___ i, r __ e..(picture)
          ___ j, pixel __ e..(r)
          __ col[j] __ row[i] __ 1 a.. pixel __ 'B'
      )
