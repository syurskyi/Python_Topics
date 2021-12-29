class Solution(object):
  ___ evalRPN(self, tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    for token in tokens:
      __ token in ["+", "-", "*", "/"]:
        b, a = stack.pop(), stack.pop()
        __ token == "+":
          res = a + b
        __ token == "-":
          res = a - b
        __ token == "*":
          res = a * b
        __ token == "/":
          res = int(float(a) / float(b))
        stack.append(res)
      else:
        stack.append(int(token))
    return stack.pop()
