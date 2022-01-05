c_ Solution(o..):
  ___ fractionAddition  expression):
    """
    :type expression: str
    :rtype: str
    """

    ___ add(a, b):
      __ a __ "0/1":
        r.. b

      ___ gcd(a, b):
        w.... b != 0:
          a, b = b, a % b
        r.. a

      (an, ad), (bn, bd) = map(i.., a.s..("/")), map(i.., b.s..("/"))
      lcm = (ad * bd) / (gcd(ad, bd))
      an, bn = an * (lcm / ad), bn * (lcm / bd)
      n = an + bn
      g = gcd(n, lcm)
      r.. s..(n / g) + "/" + s..(lcm / g)

    expression += "+"
    ans = "0/1"
    start = 0
    ___ i __ r..(1, l..(expression)):
      __ expression[i] __ ["+", "-"]:
        num = expression[start:i]
        ans = add(ans, num)
        start = i
    r.. ans __ ans[0] != "+" ____ ans[1:]
