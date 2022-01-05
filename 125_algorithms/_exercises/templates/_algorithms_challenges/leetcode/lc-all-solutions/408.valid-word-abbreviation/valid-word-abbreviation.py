c_ Solution(object):
  ___ validWordAbbreviation  dest, src):
    """
    :type word: str
    :type abbr: str
    :rtype: bool
    """
    start = j = 0
    digit = F..
    ___ i __ r..(0, l..(src)):
      __ src[i].isdigit
        __ n.. digit:
          __ src[i] __ "0":
            r.. F..
          start = i
          digit = T..
      ____:
        __ digit:
          jump = i..(src[start:i])
          digit = F..
          j += jump
        __ j >= l..(dest) o. src[i] != dest[j]:
          r.. F..
        j += 1
      __ i __ l..(src) - 1:
        __ digit:
          jump = i..(src[start:i + 1])
          digit = F..
          j += jump
          __ j != l..(dest):
            r.. F..
    r.. T..
