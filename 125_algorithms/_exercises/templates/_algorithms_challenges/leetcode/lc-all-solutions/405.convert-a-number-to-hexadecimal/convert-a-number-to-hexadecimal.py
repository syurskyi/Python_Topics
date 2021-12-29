class Solution(object):
  ___ toHex(self, num):
    """
    :type num: int
    :rtype: str
    """
    d = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "a", 11: "b", 12: "c",
         13: "d", 14: "e", 15: "f"}
    ans = ""
    mask = 0xf0000000
    flag = False
    ___ i __ r..(0, 8):
      halfb = (num & mask) >> 28
      __ halfb != 0:
        flag = True
      __ flag:
        ans = ans + d[(num & mask) >> 28]
      num = num << 4
    __ ans __ "":
      r.. "0"
    r.. ans
