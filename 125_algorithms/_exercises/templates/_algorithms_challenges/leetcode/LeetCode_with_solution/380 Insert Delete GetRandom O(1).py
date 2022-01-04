"""
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of
being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 1 is the only number in the set, getRandom always return 1.
randomSet.getRandom();
"""
_______ r__

__author__ = 'Daniel'


c_ RandomizedSet(object):
    ___ - ):
        """
        1. Use List of numbers to support O(1) getRandom
        2. need an efficient way to find and delete an element
        3. Use Map to get the location, move to end and pop
        Initialize your data structure here.
        """
        lst    # list
        pos    # dict

    ___ insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        __ val __ pos:
            r.. F..

        lst.a..(val)
        pos[val] = l..(lst) - 1

        r.. T..

    ___ remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        __ val n.. __ pos:
            r.. F..

        idx, last = pos[val], l..(lst) - 1

        __ idx != last:
            lst[idx], lst[last] = lst[last], lst[idx]
            pos[lst[idx]] = idx

        del pos[val]
        lst.pop()

        r.. T..

    ___ getRandom
        """
        Gets a random element from the set.
        :rtype: int
        """
        r.. r__.choice(lst)


c_ RandomizedSetTLE(object):
    ___ - ):
        """
        Initialize your data structure here.
        """
        set = set()

    ___ insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        ret = val n.. __ set
        set.add(val)
        r.. ret

    ___ remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        ret = val __ set
        set.discard(val)
        r.. ret

    ___ getRandom
        """
        Get a random element from the set.
        :rtype: int
        """
        r.. r__.sample(set, 1)[0]  # O(N), equivalent to random.choice(tuple(allLetters))



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
