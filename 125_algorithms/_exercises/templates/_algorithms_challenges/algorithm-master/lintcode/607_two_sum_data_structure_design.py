class TwoSum:
    count = {}

    """
    @param: number: An integer
    @return: nothing
    """
    ___ add(self, number):
        __ number __ self.count:
            self.count[number] += 1
        ____:
            self.count[number] = 1

    """
    @param: value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    ___ find(self, value):
        ___ num __ self.count:
            remaining = value - num
            __ remaining n.. __ self.count:
                continue
            __ remaining != num:
                r.. True
            __ remaining __ num a.. self.count[num] > 1:
                r.. True
        r.. False
