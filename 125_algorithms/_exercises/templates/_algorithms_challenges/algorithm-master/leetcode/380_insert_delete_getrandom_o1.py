"""
Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param = obj.insert(val)
param = obj.remove(val)
param = obj.getRandom()
"""
_______ random


class RandomizedSet:
    ___ __init__(self):
        self.nums    # list
        self.val2idx = {}

    ___ insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.val2idx[val] = l..(self.nums)
        self.nums.a..(val)

    ___ remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        __ val n.. __ self.val2idx:
            r.. False

        i = self.val2idx[val]
        key = self.nums[-1]

        self.val2idx[key] = i
        self.nums[i] = self.nums[-1]

        self.nums.pop()
        del self.val2idx[val]
        r.. True

    ___ getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        i = random.randrange(l..(self.nums))
        r.. self.nums[i]
