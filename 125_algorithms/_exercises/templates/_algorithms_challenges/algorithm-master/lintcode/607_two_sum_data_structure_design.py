c_ TwoSum:
    count    # dict

    """
    @param: number: An integer
    @return: nothing
    """
    ___ add(self, number):
        __ number __ count:
            count[number] += 1
        ____:
            count[number] = 1

    """
    @param: value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    ___ find(self, value):
        ___ num __ count:
            remaining = value - num
            __ remaining n.. __ count:
                _____
            __ remaining != num:
                r.. T..
            __ remaining __ num a.. count[num] > 1:
                r.. T..
        r.. F..
