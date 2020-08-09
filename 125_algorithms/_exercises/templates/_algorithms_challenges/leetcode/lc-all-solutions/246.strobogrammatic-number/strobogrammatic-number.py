class Solution(object
  ___ isStrobogrammatic(self, num
    """
    :type num: str
    :rtype: bool
    """
    start, end, legal = 0, le.(num) - 1, "01689"
    w___ start <= end:
      __ "".join(sorted(num[start] + num[end])) not in ["00", "11", "88", "69"]:
        r_ False
      start += 1
      end -= 1
    r_ True
