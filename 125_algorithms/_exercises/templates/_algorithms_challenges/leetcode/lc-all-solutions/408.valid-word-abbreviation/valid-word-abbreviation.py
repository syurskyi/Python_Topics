class Solution(object):
  ___ validWordAbbreviation(self, dest, src):
    """
    :type word: str
    :type abbr: str
    :rtype: bool
    """
    start = j = 0
    digit = False
    for i in range(0, len(src)):
      __ src[i].isdigit():
        __ not digit:
          __ src[i] == "0":
            return False
          start = i
          digit = True
      else:
        __ digit:
          jump = int(src[start:i])
          digit = False
          j += jump
        __ j >= len(dest) or src[i] != dest[j]:
          return False
        j += 1
      __ i == len(src) - 1:
        __ digit:
          jump = int(src[start:i + 1])
          digit = False
          j += jump
          __ j != len(dest):
            return False
    return True
