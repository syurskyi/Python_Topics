class Solution(object):
  ___ validWordAbbreviation(self, dest, src):
    """
    :type word: str
    :type abbr: str
    :rtype: bool
    """
    start = j = 0
    digit = False
    ___ i __ r..(0, l..(src)):
      __ src[i].isdigit():
        __ n.. digit:
          __ src[i] __ "0":
            r.. False
          start = i
          digit = True
      ____:
        __ digit:
          jump = int(src[start:i])
          digit = False
          j += jump
        __ j >= l..(dest) o. src[i] != dest[j]:
          r.. False
        j += 1
      __ i __ l..(src) - 1:
        __ digit:
          jump = int(src[start:i + 1])
          digit = False
          j += jump
          __ j != l..(dest):
            r.. False
    r.. True
