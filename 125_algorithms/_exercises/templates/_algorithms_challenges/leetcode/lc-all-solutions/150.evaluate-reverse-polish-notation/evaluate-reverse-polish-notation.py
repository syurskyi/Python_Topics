class Solution(object
  ___ evalRPN(self, tokens
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    ___ token in tokens:
      __ token in ["+", "-", "*", "/"]:
        b, a = stack.p.., stack.p..
        __ token __ "+":
          res = a + b
        __ token __ "-":
          res = a - b
        __ token __ "*":
          res = a * b
        __ token __ "/":
          res = int(float(a) / float(b))
        stack.append(res)
      ____
        stack.append(int(token))
    r_ stack.p..
