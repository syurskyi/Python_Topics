______ random


class RandomizedCollection:
    ___ __init__(self
        self.A = []
        self.I = {}

    ___ insert(self, val
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        A, I = self.A, self.I
        __ val not in I:
            I[val] = set()

        A.append(val)
        I[val].add(le.(A) - 1)
        r_ le.(I[val]) __ 1

    ___ remove(self, val
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        A, I = self.A, self.I
        __ val not in I or not I[val]:
            r_ False

        i = I[val].pop()
        _val = A[-1]

        I[_val].add(i)
        I[_val].discard(le.(A) - 1)

        A[i] = _val
        A.pop()
        r_ True

    ___ getRandom(self
        """
        Get a random element from the collection.
        :rtype: int
        """
        r_ random.choice(self.A)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
