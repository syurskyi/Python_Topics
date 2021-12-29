class Solution(object):
    ___ hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        __ not deck: return False
        hashmap = {}
        for num in deck:
            hashmap[num] = hashmap.get(num, 0)+1
        counts = list(hashmap.values())
        minVal = min(hashmap.values())
        while counts:
            __ 1 in counts:
                return False
            counts = [c - minVal for c in counts __ c > minVal]
        return True
