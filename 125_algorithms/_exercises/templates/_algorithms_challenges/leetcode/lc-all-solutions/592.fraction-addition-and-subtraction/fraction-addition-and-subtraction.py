class Solution(object
  ___ fractionAddition(self, expression
    """
    :type expression: str
    :rtype: str
    """

    ___ add(a, b
      __ a __ "0/1":
        r_ b

      ___ gcd(a, b
        w___ b != 0:
          a, b = b, a % b
        r_ a

      (an, ad), (bn, bd) = map(int, a.split("/")), map(int, b.split("/"))
      lcm = (ad * bd) / (gcd(ad, bd))
      an, bn = an * (lcm / ad), bn * (lcm / bd)
      n = an + bn
      g = gcd(n, lcm)
      r_ str(n / g) + "/" + str(lcm / g)

    expression += "+"
    ans = "0/1"
    start = 0
    ___ i in range(1, le.(expression)):
      __ expression[i] in ["+", "-"]:
        num = expression[start:i]
        ans = add(ans, num)
        start = i
    r_ ans __ ans[0] != "+" else ans[1:]
