class TwoSum:
    count = {}

    """
    @param: number: An integer
    @return: nothing
    """
    ___ add(self, number):
        __ number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1

    """
    @param: value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    ___ find(self, value):
        for num in self.count:
            remaining = value - num
            __ remaining not in self.count:
                continue
            __ remaining != num:
                return True
            __ remaining == num and self.count[num] > 1:
                return True
        return False
