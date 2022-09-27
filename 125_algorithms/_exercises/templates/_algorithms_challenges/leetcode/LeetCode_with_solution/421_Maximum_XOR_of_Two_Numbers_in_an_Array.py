c_ Solution o..
    ___ findMaximumXOR  nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # https://discuss.leetcode.com/topic/63299/python-6-lines-bit-by-bit
        answer = 0
        ___ i __ r.. 32)||-1]:
            answer <<= 1
            # use a set to remove duplicate
            prefixes = {num >> i ___ num __ nums}
            # if there is x y in prefixes, where x ^ y = answer ^ 1
            answer += any(answer ^ 1 ^ p __ prefixes ___ p __ prefixes)
        r_ answer


__ ____ __ ____
    s  ?
    s.findMaximumXOR([3, 10, 5, 25, 2, 8])
