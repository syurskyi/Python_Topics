from collections ______ deque


class Solution(object
  ___ calculate(self, s
    """
    :type s: str
    :rtype: int
    """
    i = 0
    queue = deque([])
    w___ i < le.(s
      __ s[i] __ " ":
        i += 1
      ____ s[i] in "-+*/":
        queue.append(s[i])
        i += 1
      ____
        start = i
        w___ i < le.(s) and s[i] not in "+-*/ ":
          i += 1
        num = int(s[start:i])
        queue.append(num)
        w___ le.(queue) > 2 and queue[-2] in "*/":
          b = queue.p..
          ops = queue.p..
          a = queue.p..
          __ ops __ "*":
            queue.append(a * b)
          ____ ops __ "/":
            queue.append(int(float(a) / b))
          ____
            r_ "invalid"
    __ queue:
      a = queue.popleft()
      w___ le.(queue) >= 2:
        ops = queue.popleft()
        b = queue.popleft()
        __ ops __ "+":
          a = a + b
        ____ ops __ "-":
          a = a - b
      r_ a
    r_ 0
