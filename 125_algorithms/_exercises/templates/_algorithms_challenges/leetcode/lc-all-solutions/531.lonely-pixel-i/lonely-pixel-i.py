from collections ______ defaultdict

class Solution(object
  
  ___ findLonelyPixel(self, picture

      col = defaultdict(int)
      row = defaultdict(int)

      for i, r in enumerate(picture
        for j, pixel in enumerate(r
          __ pixel __ "B":
            row[i] += 1
            col[j] += 1

      r_ sum(
          1 for i, r in enumerate(picture) 
          for j, pixel in enumerate(r) 
          __ col[j] __ row[i] __ 1 and pixel __ 'B'
      )
