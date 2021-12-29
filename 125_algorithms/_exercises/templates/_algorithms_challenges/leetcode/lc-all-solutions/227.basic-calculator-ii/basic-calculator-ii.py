____ collections _______ deque


class Solution(object):
  ___ calculate(self, s):
    """
    :type s: str
    :rtype: int
    """
    i = 0
    queue = deque([])
    w.... i < l..(s):
      __ s[i] __ " ":
        i += 1
      ____ s[i] __ "-+*/":
        queue.a..(s[i])
        i += 1
      ____:
        start = i
        w.... i < l..(s) a.. s[i] n.. __ "+-*/ ":
          i += 1
        num = int(s[start:i])
        queue.a..(num)
        w.... l..(queue) > 2 a.. queue[-2] __ "*/":
          b = queue.pop()
          ops = queue.pop()
          a = queue.pop()
          __ ops __ "*":
            queue.a..(a * b)
          ____ ops __ "/":
            queue.a..(int(float(a) / b))
          ____:
            r.. "invalid"
    __ queue:
      a = queue.popleft()
      w.... l..(queue) >= 2:
        ops = queue.popleft()
        b = queue.popleft()
        __ ops __ "+":
          a = a + b
        ____ ops __ "-":
          a = a - b
      r.. a
    r.. 0
