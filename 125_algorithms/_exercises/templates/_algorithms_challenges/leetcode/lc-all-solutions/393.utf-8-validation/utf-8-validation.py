c_ Solution(o..
  ___ validUtf8  data
    """
    :type data: List[int]
    :rtype: bool
    """
    features = {0x00: 0, 0xc0: 1, 0xe0: 2, 0xf0: 3}
    masks = [0xf8, 0xf0, 0xe0, 0x80]
    new = T..
    followed = 0
    i = 0
    w.... i < l..(data
      __ new:
        followed = -1
        ___ mask __ masks:
          __ (data[i] & mask) __ features:
            followed = features[data[i] & mask]
            _____
        __ followed __ -1:
          r.. F..
        ____ followed != 0:
          new = F..
        ____
          new = T..
      ____
        __ (data[i] & 0xc0) != 0x80:
          r.. F..
        followed -_ 1
        __ followed __ 0:
          new = T..
      i += 1

    r.. followed __ 0
