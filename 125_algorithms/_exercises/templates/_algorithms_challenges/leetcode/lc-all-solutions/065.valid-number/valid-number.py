class States(object):
  ___ __init__(self):
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


class Solution(object):
  ___ isNumber(self, s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.strip()
    states = States()
    state = states.init
    decimals = "01234567890"

    ___ c __ s:
      __ state __ states.init:
        __ c __ ".":
          state = states.nullpoint
        ____ c __ decimals:
          state = states.decimal
        ____ c __ ["+", "-"]:
          state = states.sign
        ____:
          r.. False
      ____ state __ states.sign:
        __ c __ decimals:
          state = states.decimal
        ____ c __ ".":
          state = states.nullpoint
        ____:
          r.. False
      ____ state __ states.esign:
        __ c n.. __ decimals:
          r.. False
        state = states.afteresign
      ____ state __ states.afteresign:
        __ c n.. __ decimals:
          r.. False
      ____ state __ states.nullpoint:
        __ c n.. __ decimals:
          r.. False
        state = states.decpoint
      ____ state __ states.decimal:
        __ c __ decimals:
          continue
        ____ c __ "e":
          state = states.e
        ____ c __ ".":
          state = states.decpoint
        ____:
          r.. False
      ____ state __ states.decpoint:
        __ c __ decimals:
          state = states.afterdp
        ____ c __ "e":
          state = states.e
        ____:
          r.. False
      ____ state __ states.afterdp:
        __ c __ decimals:
          continue
        ____ c __ "e":
          state = states.e
        ____:
          r.. False
      ____ state __ states.e:
        __ c __ decimals:
          state = states.aftere
        ____ c __ ["+", "-"]:
          state = states.esign
        ____:
          r.. False
      ____ state __ states.aftere:
        __ c n.. __ decimals:
          r.. False
      ____:
        r.. False
    r.. state n.. __ [states.init, states.e, states.nullpoint, states.sign, states.esign]
