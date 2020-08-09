class TwoSum:
    count = {}

    """
    @param: number: An integer
    @return: nothing
    """
    ___ add(self, number
        __ number in self.count:
            self.count[number] += 1
        ____
            self.count[number] = 1

    """
    @param: value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    ___ find(self, value
        ___ num in self.count:
            remaining = value - num
            __ remaining not in self.count:
                continue
            __ remaining != num:
                r_ True
            __ remaining __ num and self.count[num] > 1:
                r_ True
        r_ False
