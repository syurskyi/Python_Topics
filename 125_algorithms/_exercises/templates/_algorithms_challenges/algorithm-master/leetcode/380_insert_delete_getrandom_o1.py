"""
Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param = obj.insert(val)
param = obj.remove(val)
param = obj.getRandom()
"""
______ random


class RandomizedSet:
    ___ __init__(self
        self.nums = []
        self.val2idx = {}

    ___ insert(self, val
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.val2idx[val] = le.(self.nums)
        self.nums.append(val)

    ___ remove(self, val
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        __ val not in self.val2idx:
            r_ False

        i = self.val2idx[val]
        key = self.nums[-1]

        self.val2idx[key] = i
        self.nums[i] = self.nums[-1]

        self.nums.pop()
        del self.val2idx[val]
        r_ True

    ___ getRandom(self
        """
        Get a random element from the set.
        :rtype: int
        """
        i = random.randrange(le.(self.nums))
        r_ self.nums[i]
