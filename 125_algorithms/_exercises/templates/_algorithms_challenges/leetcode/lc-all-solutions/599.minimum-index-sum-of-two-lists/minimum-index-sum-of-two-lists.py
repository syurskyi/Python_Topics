c_ Solution(o..
  ___ findRestaurant  list1, list2
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    minSum = f__("inf")
    ans    # list
    d    # dict
    ___ i, name __ e..(list2
      d[name] = i
    ___ i, name __ e..(list1
      idxSum = i + d.g.. name, f__("inf"
      __ idxSum __ minSum:
        ans.a..(name)
      __ idxSum < minSum:
        ans = [name]
        minSum = idxSum
    r.. ans
