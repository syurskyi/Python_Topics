c_ Solution o..
    ___ twoSum  numbers, target
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Two Points
        begin, end = 0, l.. numbers) - 1
        w.. begin < end:
            curr = numbers[begin] + numbers[end]
            __ curr __ target:
                r_ [begin + 1, end + 1]
            ____ curr < target:
                begin += 1
            ____
                end -= 1

