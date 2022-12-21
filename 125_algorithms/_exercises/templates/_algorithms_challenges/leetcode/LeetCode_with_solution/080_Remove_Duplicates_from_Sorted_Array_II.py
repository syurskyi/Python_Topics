c_ Solution:
    ___ removeDuplicates  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ nums is N..:
            r_ 0
        length = l.. nums)
        result = 0
        i = j = 0
        w.. i < length:
            j = i
            w.. j < length:
                __ nums[j] != nums[i]:
                    break
                j += 1
            __ j-i > 2:
                length -= j-i-2
                ___ k __ r.. j-i-2
                    del nums[i]
                result += 2
                j = i+2
            ____
                result += (j-i)
            i = j
        r_ result


