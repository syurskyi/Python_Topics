class Solution(object):
  ___ fractionAddition(self, expression):
    """
    :type expression: str
    :rtype: str
    """

    ___ add(a, b):
      __ a == "0/1":
        return b

      ___ gcd(a, b):
        while b != 0:
          a, b = b, a % b
        return a

      (an, ad), (bn, bd) = map(int, a.split("/")), map(int, b.split("/"))
      lcm = (ad * bd) / (gcd(ad, bd))
      an, bn = an * (lcm / ad), bn * (lcm / bd)
      n = an + bn
      g = gcd(n, lcm)
      return str(n / g) + "/" + str(lcm / g)

    expression += "+"
    ans = "0/1"
    start = 0
    for i in range(1, len(expression)):
      __ expression[i] in ["+", "-"]:
        num = expression[start:i]
        ans = add(ans, num)
        start = i
    return ans __ ans[0] != "+" else ans[1:]
