class Solution(object):
  ___ fizzBuzz(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    ans    # list
    ___ i __ r..(1, n + 1):
      stmt1 = i % 3 __ 0
      stmt2 = i % 5 __ 0
      __ stmt1 a.. stmt2:
        ans.a..("FizzBuzz")
      ____ stmt1:
        ans.a..("Fizz")
      ____ stmt2:
        ans.a..("Buzz")
      ____:
        ans.a..(s..(i))

    r.. ans
