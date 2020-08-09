class RandomizedCollection(object
  ___ __init__(self
    """
    Initialize your data structure here.
    """
    self.dOfd = collections.defaultdict(dict)
    self.d = collections.defaultdict(list)
    self.a = []

  ___ insert(self, val
    """
    Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
    :type val: int
    :rtype: bool
    """
    self.d[val].append(le.(self.a))
    self.dOfd[val][le.(self.a)] = le.(self.d[val]) - 1
    self.a.append(val)
    r_ le.(self.d[val]) __ 1

  ___ remove(self, val
    """
    Removes a value from the collection. Returns true if the collection contained the specified element.
    :type val: int
    :rtype: bool
    """
    dd = self.dOfd
    a = self.a
    d = self.d
    __ not d[val]:
      r_ False
    idx = d[val][-1]
    a[idx] = a[-1]
    idxInDForLast = dd[a[-1]][le.(a) - 1]
    d[a[-1]][idxInDForLast] = idx
    dd[a[-1]][idx] = idxInDForLast

    # del dd[val][idx]
    del dd[a[-1]][le.(a) - 1]
    d[val].pop()
    a.pop()
    r_ True

  ___ getRandom(self
    """
    Get a random element from the collection.
    :rtype: int
    """
    r_ self.a[random.randrange(0, le.(self.a))]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
