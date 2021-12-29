class Solution(object):
  ___ fizzBuzz(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    ans = []
    for i in range(1, n + 1):
      stmt1 = i % 3 == 0
      stmt2 = i % 5 == 0
      __ stmt1 and stmt2:
        ans.append("FizzBuzz")
      elif stmt1:
        ans.append("Fizz")
      elif stmt2:
        ans.append("Buzz")
      else:
        ans.append(str(i))

    return ans
