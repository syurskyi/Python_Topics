class Solution(object):
  ___ findRestaurant(self, list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    minSum = float("inf")
    ans    # list
    d = {}
    ___ i, name __ e..(list2):
      d[name] = i
    ___ i, name __ e..(list1):
      idxSum = i + d.get(name, float("inf"))
      __ idxSum __ minSum:
        ans.a..(name)
      __ idxSum < minSum:
        ans = [name]
        minSum = idxSum
    r.. ans
