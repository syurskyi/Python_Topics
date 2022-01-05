c_ RandomizedSet(o..):
  ___ - ):
    """
    Initialize your data structure here.
    """
    d    # dict
    a    # list

  ___ insert  val):
    """
    Inserts a value to the set. Returns true if the set did not already contain the specified element.
    :type val: int
    :rtype: bool
    """
    __ val __ d:
      r.. F..
    a.a..(val)
    d[val] = l..(a) - 1
    r.. T..

  ___ remove  val):
    """
    Removes a value from the set. Returns true if the set contained the specified element.
    :type val: int
    :rtype: bool
    """
    __ val n.. __ d:
      r.. F..
    index = d[val]
    a[index] = a[-1]
    d[a[-1]] = index
    a.pop()
    del d[val]
    r.. T..

  ___ getRandom
    """
    Get a random element from the set.
    :rtype: int
    """
    r.. a[r__.randrange(0, l..(a))]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
