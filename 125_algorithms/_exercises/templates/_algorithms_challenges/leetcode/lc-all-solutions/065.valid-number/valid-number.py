c_ States(object):
  ___ - ):
    init = 0
    decimal = 1
    decpoint = 2
    afterdp = 3
    e = 4
    aftere = 5
    sign = 6
    nullpoint = 7
    esign = 8
    afteresign = 9


c_ Solution(object):
  ___ isNumber(self, s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.s..
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
          r.. F..
      ____ state __ states.sign:
        __ c __ decimals:
          state = states.decimal
        ____ c __ ".":
          state = states.nullpoint
        ____:
          r.. F..
      ____ state __ states.esign:
        __ c n.. __ decimals:
          r.. F..
        state = states.afteresign
      ____ state __ states.afteresign:
        __ c n.. __ decimals:
          r.. F..
      ____ state __ states.nullpoint:
        __ c n.. __ decimals:
          r.. F..
        state = states.decpoint
      ____ state __ states.decimal:
        __ c __ decimals:
          _____
        ____ c __ "e":
          state = states.e
        ____ c __ ".":
          state = states.decpoint
        ____:
          r.. F..
      ____ state __ states.decpoint:
        __ c __ decimals:
          state = states.afterdp
        ____ c __ "e":
          state = states.e
        ____:
          r.. F..
      ____ state __ states.afterdp:
        __ c __ decimals:
          _____
        ____ c __ "e":
          state = states.e
        ____:
          r.. F..
      ____ state __ states.e:
        __ c __ decimals:
          state = states.aftere
        ____ c __ ["+", "-"]:
          state = states.esign
        ____:
          r.. F..
      ____ state __ states.aftere:
        __ c n.. __ decimals:
          r.. F..
      ____:
        r.. F..
    r.. state n.. __ [states.init, states.e, states.nullpoint, states.sign, states.esign]
