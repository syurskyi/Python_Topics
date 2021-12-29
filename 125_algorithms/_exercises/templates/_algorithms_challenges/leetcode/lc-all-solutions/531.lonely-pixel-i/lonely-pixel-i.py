from collections import defaultdict

class Solution(object):
  
  ___ findLonelyPixel(self, picture):

      col = defaultdict(int)
      row = defaultdict(int)

      for i, r in enumerate(picture):
        for j, pixel in enumerate(r):
          __ pixel == "B":
            row[i] += 1
            col[j] += 1

      return sum(
          1 for i, r in enumerate(picture) 
          for j, pixel in enumerate(r) 
          __ col[j] == row[i] == 1 and pixel == 'B'
      )
