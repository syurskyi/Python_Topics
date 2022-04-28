c_ Solution o..
    ___ longestConsecutive  nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ___ longestConsecutive  num):
            # Pop adjacency O(n) and O(n)
            num = set(num)
            maxLen = 0
            w.. num:
                n = num.pop()
                i = n + 1
                l1 = 0
                l2 = 0
                w.. i __ num:
                    num.remove(i)
                    i += 1
                    l1 += 1
                i = n - 1
                w.. i __ num:
                    num.remove(i)
                    i -= 1
                    l2 += 1
                maxLen = max(maxLen, l1 + l2 + 1)
            r_ maxLen