c_ Solution(object):
  ___ evalRPN  tokens):
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
          res = i..(float(a) / float(b))
        stack.a..(res)
      ____:
        stack.a..(i..(token))
    r.. stack.pop()
