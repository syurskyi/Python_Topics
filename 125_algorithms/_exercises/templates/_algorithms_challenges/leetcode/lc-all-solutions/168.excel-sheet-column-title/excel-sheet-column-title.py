c_ Solution(o..
  ___ convertToTitle  n
    """
    :type n: int
    :rtype: str
    """
    ans = ""
    w.... n > 0:
      y = n % 26
      __ y __ 0:
        char = "Z"
        n -= 26
      ____:
        char = chr(o..("A") + y - 1)
      ans += char
      n = n / 26
    r.. ans[::-1]
