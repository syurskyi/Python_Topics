class States(object
  ___ __init__(self
    self.init = 0
    self.decimal = 1
    self.decpoint = 2
    self.afterdp = 3
    self.e = 4
    self.aftere = 5
    self.sign = 6
    self.nullpoint = 7
    self.esign = 8
    self.afteresign = 9


class Solution(object
  ___ isNumber(self, s
    """
    :type s: str
    :rtype: bool
    """
    s = s.strip()
    states = States()
    state = states.init
    decimals = "01234567890"

    ___ c in s:
      __ state __ states.init:
        __ c __ ".":
          state = states.nullpoint
        ____ c in decimals:
          state = states.decimal
        ____ c in ["+", "-"]:
          state = states.sign
        ____
          r_ False
      ____ state __ states.sign:
        __ c in decimals:
          state = states.decimal
        ____ c __ ".":
          state = states.nullpoint
        ____
          r_ False
      ____ state __ states.esign:
        __ c not in decimals:
          r_ False
        state = states.afteresign
      ____ state __ states.afteresign:
        __ c not in decimals:
          r_ False
      ____ state __ states.nullpoint:
        __ c not in decimals:
          r_ False
        state = states.decpoint
      ____ state __ states.decimal:
        __ c in decimals:
          continue
        ____ c __ "e":
          state = states.e
        ____ c __ ".":
          state = states.decpoint
        ____
          r_ False
      ____ state __ states.decpoint:
        __ c in decimals:
          state = states.afterdp
        ____ c __ "e":
          state = states.e
        ____
          r_ False
      ____ state __ states.afterdp:
        __ c in decimals:
          continue
        ____ c __ "e":
          state = states.e
        ____
          r_ False
      ____ state __ states.e:
        __ c in decimals:
          state = states.aftere
        ____ c in ["+", "-"]:
          state = states.esign
        ____
          r_ False
      ____ state __ states.aftere:
        __ c not in decimals:
          r_ False
      ____
        r_ False
    r_ state not in [states.init, states.e, states.nullpoint, states.sign, states.esign]
