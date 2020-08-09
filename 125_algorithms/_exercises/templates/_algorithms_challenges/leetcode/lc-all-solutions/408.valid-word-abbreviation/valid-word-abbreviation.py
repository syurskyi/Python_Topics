class Solution(object
  ___ validWordAbbreviation(self, dest, src
    """
    :type word: str
    :type abbr: str
    :rtype: bool
    """
    start = j = 0
    digit = False
    ___ i in range(0, le.(src)):
      __ src[i].isdigit(
        __ not digit:
          __ src[i] __ "0":
            r_ False
          start = i
          digit = True
      ____
        __ digit:
          jump = int(src[start:i])
          digit = False
          j += jump
        __ j >= le.(dest) or src[i] != dest[j]:
          r_ False
        j += 1
      __ i __ le.(src) - 1:
        __ digit:
          jump = int(src[start:i + 1])
          digit = False
          j += jump
          __ j != le.(dest
            r_ False
    r_ True
