_______ r__


c_ RandomizedCollection:
    ___ - ):
        A    # list
        I    # dict

    ___ insert  val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        A, I = A, I
        __ val n.. __ I:
            I[val] = s..()

        A.a..(val)
        I[val].add(l..(A) - 1)
        r.. l..(I[val]) __ 1

    ___ remove  val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        A, I = A, I
        __ val n.. __ I o. n.. I[val]:
            r.. F..

        i = I[val].pop()
        _val = A[-1]

        I[_val].add(i)
        I[_val].discard(l..(A) - 1)

        A[i] = _val
        A.pop()
        r.. T..

    ___ getRandom
        """
        Get a random element from the collection.
        :rtype: int
        """
        r.. r__.choice(A)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
