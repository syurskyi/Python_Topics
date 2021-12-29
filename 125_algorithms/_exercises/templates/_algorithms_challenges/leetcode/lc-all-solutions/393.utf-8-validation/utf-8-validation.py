class Solution(object):
  ___ validUtf8(self, data):
    """
    :type data: List[int]
    :rtype: bool
    """
    features = {0x00: 0, 0xc0: 1, 0xe0: 2, 0xf0: 3}
    masks = [0xf8, 0xf0, 0xe0, 0x80]
    new = True
    followed = 0
    i = 0
    while i < len(data):
      __ new:
        followed = -1
        for mask in masks:
          __ (data[i] & mask) in features:
            followed = features[data[i] & mask]
            break
        __ followed == -1:
          return False
        elif followed != 0:
          new = False
        else:
          new = True
      else:
        __ (data[i] & 0xc0) != 0x80:
          return False
        followed -= 1
        __ followed == 0:
          new = True
      i += 1

    return followed == 0
