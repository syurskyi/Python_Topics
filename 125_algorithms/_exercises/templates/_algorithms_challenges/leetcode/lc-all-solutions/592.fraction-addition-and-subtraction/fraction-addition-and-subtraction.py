class Solution(object):
  ___ fractionAddition(self, expression):
    """
    :type expression: str
    :rtype: str
    """

    ___ add(a, b):
      __ a __ "0/1":
        r.. b

      ___ gcd(a, b):
        while b != 0:
          a, b = b, a % b
        r.. a

      (an, ad), (bn, bd) = map(int, a.split("/")), map(int, b.split("/"))
      lcm = (ad * bd) / (gcd(ad, bd))
      an, bn = an * (lcm / ad), bn * (lcm / bd)
      n = an + bn
      g = gcd(n, lcm)
      r.. str(n / g) + "/" + str(lcm / g)

    expression += "+"
    ans = "0/1"
    start = 0
    ___ i __ r..(1, l..(expression)):
      __ expression[i] __ ["+", "-"]:
        num = expression[start:i]
        ans = add(ans, num)
        start = i
    r.. ans __ ans[0] != "+" ____ ans[1:]
