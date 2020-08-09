class Solution(object
  ___ fizzBuzz(self, n
    """
    :type n: int
    :rtype: List[str]
    """
    ans = []
    ___ i in range(1, n + 1
      stmt1 = i % 3 __ 0
      stmt2 = i % 5 __ 0
      __ stmt1 and stmt2:
        ans.append("FizzBuzz")
      ____ stmt1:
        ans.append("Fizz")
      ____ stmt2:
        ans.append("Buzz")
      ____
        ans.append(str(i))

    r_ ans
