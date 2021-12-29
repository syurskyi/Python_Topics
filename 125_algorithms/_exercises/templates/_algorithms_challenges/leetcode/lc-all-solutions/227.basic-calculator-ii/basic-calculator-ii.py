from collections import deque


class Solution(object):
  ___ calculate(self, s):
    """
    :type s: str
    :rtype: int
    """
    i = 0
    queue = deque([])
    while i < len(s):
      __ s[i] == " ":
        i += 1
      elif s[i] in "-+*/":
        queue.append(s[i])
        i += 1
      else:
        start = i
        while i < len(s) and s[i] not in "+-*/ ":
          i += 1
        num = int(s[start:i])
        queue.append(num)
        while len(queue) > 2 and queue[-2] in "*/":
          b = queue.pop()
          ops = queue.pop()
          a = queue.pop()
          __ ops == "*":
            queue.append(a * b)
          elif ops == "/":
            queue.append(int(float(a) / b))
          else:
            return "invalid"
    __ queue:
      a = queue.popleft()
      while len(queue) >= 2:
        ops = queue.popleft()
        b = queue.popleft()
        __ ops == "+":
          a = a + b
        elif ops == "-":
          a = a - b
      return a
    return 0
