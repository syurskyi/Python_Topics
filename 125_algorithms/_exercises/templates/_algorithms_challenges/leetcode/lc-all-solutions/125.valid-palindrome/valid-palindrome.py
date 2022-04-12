c_ Solution(o..
  ___ isPalindrome  s
    """
    :type s: str
    :rtype: bool
    """
    start, end 0, l..(s) - 1
    w.... start < end:
      __ n.. s[start].i..
        start += 1
        _____
      __ n.. s[end].i..
        end -_ 1
        _____
      __ s[start].l.. !_ s[end].l..:
        r.. F..
      start += 1
      end -_ 1
    r.. T..
