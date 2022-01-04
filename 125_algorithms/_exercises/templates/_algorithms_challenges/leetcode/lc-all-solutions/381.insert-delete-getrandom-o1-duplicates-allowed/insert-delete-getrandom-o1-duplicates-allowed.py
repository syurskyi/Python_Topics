c_ RandomizedCollection(object):
  ___ - ):
    """
    Initialize your data structure here.
    """
    dOfd = collections.defaultdict(d..)
    d = collections.defaultdict(l..)
    a    # list

  ___ insert(self, val):
    """
    Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
    :type val: int
    :rtype: bool
    """
    d[val].a..(l..(a))
    dOfd[val][l..(a)] = l..(d[val]) - 1
    a.a..(val)
    r.. l..(d[val]) __ 1

  ___ remove(self, val):
    """
    Removes a value from the collection. Returns true if the collection contained the specified element.
    :type val: int
    :rtype: bool
    """
    dd = dOfd
    a = a
    d = d
    __ n.. d[val]:
      r.. F..
    idx = d[val][-1]
    a[idx] = a[-1]
    idxInDForLast = dd[a[-1]][l..(a) - 1]
    d[a[-1]][idxInDForLast] = idx
    dd[a[-1]][idx] = idxInDForLast

    # del dd[val][idx]
    del dd[a[-1]][l..(a) - 1]
    d[val].pop()
    a.pop()
    r.. T..

  ___ getRandom
    """
    Get a random element from the collection.
    :rtype: int
    """
    r.. a[r__.randrange(0, l..(a))]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
