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
    w.... i < l..(data):
      __ new:
        followed = -1
        ___ mask __ masks:
          __ (data[i] & mask) __ features:
            followed = features[data[i] & mask]
            break
        __ followed __ -1:
          r.. False
        ____ followed != 0:
          new = False
        ____:
          new = True
      ____:
        __ (data[i] & 0xc0) != 0x80:
          r.. False
        followed -= 1
        __ followed __ 0:
          new = True
      i += 1

    r.. followed __ 0
