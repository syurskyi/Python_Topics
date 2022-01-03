c_ Solution(object):
  ___ evalRPN(self, tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack    # list
    ___ token __ tokens:
      __ token __ ["+", "-", "*", "/"]:
        b, a = stack.pop(), stack.pop()
        __ token __ "+":
          res = a + b
        __ token __ "-":
          res = a - b
        __ token __ "*":
          res = a * b
        __ token __ "/":
          res = int(float(a) / float(b))
        stack.a..(res)
      ____:
        stack.a..(int(token))
    r.. stack.pop()
