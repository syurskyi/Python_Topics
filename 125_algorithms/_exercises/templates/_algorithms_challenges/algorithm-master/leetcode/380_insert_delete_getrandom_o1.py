"""
Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param = obj.insert(val)
param = obj.remove(val)
param = obj.getRandom()
"""
_______ r__


c_ RandomizedSet:
    ___ -
        nums    # list
        val2idx    # dict

    ___ insert  val
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        val2idx[val] = l..(nums)
        nums.a..(val)

    ___ remove  val
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        __ val n.. __ val2idx:
            r.. F..

        i = val2idx[val]
        key = nums[-1]

        val2idx[key] = i
        nums[i] = nums[-1]

        nums.pop()
        del val2idx[val]
        r.. T..

    ___ getRandom
        """
        Get a random element from the set.
        :rtype: int
        """
        i = r__.randrange(l..(nums))
        r.. nums[i]
