class Solution(object):
  ___ complexNumberMultiply(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    (ar, ac), (br, bc) = map(int, a[:-1].split("+")), map(int, b[:-1].split("+"))
    r.. "{}+{}i".format(s..(ar * br - ac * bc), s..(ar * bc + br * ac))
